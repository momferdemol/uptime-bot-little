import os
import time
from urllib import request

from libs.logger import log


def uptime_bot(url: str, retries: int = 3) -> None:
    debug = bool(os.getenv("DEBUG", False))
    fails = 0
    while fails < retries:
        try:
            request.urlopen(url)
        except Exception as err:
            fails += 1
            log.error(f"{err}: for {url}", exc_info=debug)
        else:
            log.info(f"{url} is up")
        time.sleep(10)
