"""A testing and example script."""

import logging
import asyncio
from pycourseprogress import CourseProgress

_LOGGER = logging.getLogger(__name__)


async def main():
    """Running function"""
    login = True
    while login:
        try:
            instance = input("Enter instance: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            control = await CourseProgress.create(instance, username, password)
            _LOGGER.info("Logged in, ready.")
            login = False
        except Exception as err:
            _LOGGER.critical(err)

    while True:
        _LOGGER.debug("ping")
        await asyncio.sleep(15)
        _LOGGER.debug("pong")
        await control.update()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
