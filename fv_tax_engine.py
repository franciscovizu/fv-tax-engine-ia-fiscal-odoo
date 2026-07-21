"""FV Tax Engine: demostración anonimizada de semáforo fiscal CFDI."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


REQUIRED = ("tipo", "metodo_pago", "forma_pago", "fecha", "proveedor", "uuid")


def evaluate(row: dict[str, str]) -> tuple[str, str]:
    missing = [field for field in REQUIRED if not row.get(field, "").strip()]
    if missing:
        return "ROJO", f"Faltan campos obligatorios: {', '.join(missing)}"

    method = row["metodo_pago"].strip().upper()
    payment_form = row["forma_pago"].strip().zfill(2)
    has_payment = row.get("tiene_complemento", "").strip().upper() in {"SI", "SÍ", "TRUE", "1"}

    if method == "PUE" and payment_form == "99":
        return "ROJO", "PUE no debe utilizar forma de pago 99"
    if method == "PPD" and not has_payment:
        return "AMARILLO", "PPD pendiente de complemento de pago"
    return "VERDE", "Validación básica sin incidencias"


def run(source: Path, target: Path) -> None:
    with source.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    target.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys()) + ["semaforo", "resultado"] if rows else [*REQUIRED, "semaforo", "resultado"]
    with target.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            row["semaforo"], row["resultado"] = evaluate(row)
            writer.writerow(row)

    print(f"Procesados: {len(rows)} CFDI | Resultado: {target}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Uso: python src/fv_tax_engine.py entrada.csv salida.csv")
    run(Path(sys.argv[1]), Path(sys.argv[2]))
