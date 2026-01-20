import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

log = logging.getLogger("myapp")


def run(user_id):
    log.info("request id=%s", user_id)

    if user_id == 0:
        raise ValueError("bad id")

    log.info("ok id=%s", user_id)


for uid in [1, 0, 2]:
    try:
        run(uid)
    except ValueError:
        log.exception("failed id=%s: bad input", uid)
