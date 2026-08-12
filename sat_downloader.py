"""FV® & IA SAT Downloader — fase 1 segura.

Esta versión NO autentica todavía contra el SAT. Prepara el almacenamiento privado,
registra archivos descargados y evita duplicados por SHA-256 y UUID.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from zipfile import ZipFile, BadZipFile

UUID_RE = re.compile(
    rb"UUID=[\"']([0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})[\"']"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_uuid(xml_bytes: bytes) -> str | None:
    match = UUID_RE.search(xml_bytes)
    return match.group(1).decode("ascii").upper() if match else None


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {"files": {}}
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def save_manifest(path: Path, manifest: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)
    tmp.replace(path)


def register_xml(xml_path: Path, manifest: dict) -> tuple[bool, str]:
    data = xml_path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    uuid = extract_uuid(data)
    key = uuid or digest

    if key in manifest["files"]:
        return False, key

    manifest["files"][key] = {
        "uuid": uuid,
        "sha256": digest,
        "filename": xml_path.name,
        "size": len(data),
    }
    return True, key


def ingest_zip(zip_path: Path, private_dir: Path, manifest_path: Path) -> dict[str, int]:
    private_dir.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(manifest_path)
    stats = {"xml_nuevos": 0, "duplicados": 0, "otros": 0}

    try:
        with ZipFile(zip_path) as archive:
            for member in archive.infolist():
                if member.is_dir():
                    continue
                if not member.filename.lower().endswith(".xml"):
                    stats["otros"] += 1
                    continue

                data = archive.read(member)
                digest = hashlib.sha256(data).hexdigest()
                uuid = extract_uuid(data)
                key = uuid or digest

                if key in manifest["files"]:
                    stats["duplicados"] += 1
                    continue

                safe_name = Path(member.filename).name
                target = private_dir / safe_name
                if target.exists():
                    target = private_dir / f"{target.stem}_{digest[:12]}{target.suffix}"
                target.write_bytes(data)
                manifest["files"][key] = {
                    "uuid": uuid,
                    "sha256": digest,
                    "filename": target.name,
                    "size": len(data),
                    "source_package": zip_path.name,
                }
                stats["xml_nuevos"] += 1
    except BadZipFile as exc:
        raise SystemExit(f"Paquete ZIP inválido: {zip_path}") from exc

    save_manifest(manifest_path, manifest)
    return stats


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Uso: python sat_downloader.py paquete_sat.zip /ruta/privada")

    zip_path = Path(sys.argv[1]).expanduser().resolve()
    private_dir = Path(sys.argv[2]).expanduser().resolve()
    manifest_path = private_dir / "manifest.json"

    stats = ingest_zip(zip_path, private_dir / "xml", manifest_path)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
