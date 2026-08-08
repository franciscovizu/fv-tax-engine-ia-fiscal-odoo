from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass
class SyncState:
    last_successful_sync_utc: str | None = None
    last_requested_from: str | None = None
    last_requested_to: str | None = None
    downloaded_packages: list[str] | None = None
    processed_uuids: list[str] | None = None

    def __post_init__(self) -> None:
        if self.downloaded_packages is None:
            self.downloaded_packages = []
        if self.processed_uuids is None:
            self.processed_uuids = []

    @classmethod
    def load(cls, path: Path) -> "SyncState":
        if not path.exists():
            return cls()
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(**data)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(self), indent=2, ensure_ascii=False), encoding="utf-8")

    def mark_success(self, requested_from: str, requested_to: str) -> None:
        self.last_successful_sync_utc = datetime.now(timezone.utc).isoformat()
        self.last_requested_from = requested_from
        self.last_requested_to = requested_to

    def add_package(self, package_id: str) -> None:
        if package_id not in self.downloaded_packages:
            self.downloaded_packages.append(package_id)

    def add_uuid(self, uuid: str) -> bool:
        normalized = uuid.strip().upper()
        if normalized in self.processed_uuids:
            return False
        self.processed_uuids.append(normalized)
        return True
