from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class SatConnectorConfig:
    rfc: str
    cer_path: Path
    key_path: Path
    output_dir: Path = Path("sat_data")
    state_path: Path = Path("sat_data/state.json")

    @classmethod
    def from_env(cls) -> "SatConnectorConfig":
        rfc = os.environ.get("SAT_RFC", "").strip().upper()
        cer = os.environ.get("SAT_CER_PATH", "").strip()
        key = os.environ.get("SAT_KEY_PATH", "").strip()

        missing = [
            name
            for name, value in {
                "SAT_RFC": rfc,
                "SAT_CER_PATH": cer,
                "SAT_KEY_PATH": key,
            }.items()
            if not value
        ]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

        return cls(rfc=rfc, cer_path=Path(cer), key_path=Path(key))

    def validate_paths(self) -> None:
        for label, path in (("certificate", self.cer_path), ("private key", self.key_path)):
            if not path.exists():
                raise FileNotFoundError(f"SAT {label} file not found: {path}")
