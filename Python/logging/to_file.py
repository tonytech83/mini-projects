import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(fmt)

file = RotatingFileHandler(
    "./logging/app.log",
    maxBytes=2_000_000,  # 2 MB
    backupCount=5,
    encoding="utf-8",
)
file.setLevel(logging.DEBUG)
file.setFormatter(fmt)

logger.addHandler(console)
logger.addHandler(file)

# Test messages
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
