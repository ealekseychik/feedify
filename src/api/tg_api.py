import logging

import telegram

logger = logging.getLogger(__name__)


class TelegramAPI:
    def __init__(self, token: str) -> None:
        logger.info("Signing into Telegram with token")
        self.bot = telegram.Bot(token)
