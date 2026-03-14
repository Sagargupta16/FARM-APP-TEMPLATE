from __future__ import annotations

import logging
import logging.config
from pathlib import Path

import yaml

config_path = Path(__file__).parent / "logging.yml"
with open(config_path) as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))

logger = logging.getLogger("farm_app")
