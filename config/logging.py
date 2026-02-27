import logging
import logging.config
import yaml
from pathlib import Path

config_path = Path(__file__).parent / "logging.yml"
with open(config_path, "r") as f:
    logging.config.dictConfig(yaml.safe_load(f.read()))

logger = logging.getLogger("farm_app")
