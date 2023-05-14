import logging
import vk_api

logger = logging.getLogger(__name__)


class VkAPI:
    def __init__(self, login: str, password: str) -> None:
        logger.info("Signing into VK with password")
        vk_session = vk_api.VkApi(login, password)
        try:
            vk_session.auth()
        except vk_api.AuthError as msg:
            logger.exception(msg)
            return
