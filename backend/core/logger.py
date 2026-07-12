"""
Logging Configuration
"""

import logging
from pathlib import Path

LOG_DIR = Path("backend/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "jarvis.log"


def setup_logger():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    logging.info("=" * 60)
    logging.info("Starting J.A.R.V.I.S AI OS")