import logging

from celery import Celery

from src.conf import celeryconfig
from src.conf.apiconf import vk_api_login, vk_api_password, tg_api_token
from src.api.tg_api import TelegramAPI
from src.api.vk_api import VkAPI

logger = logging.getLogger(__name__)

worker = Celery("feed-elity")
worker.config_from_object(celeryconfig)

vk_api_handler = VkAPI(vk_api_login, vk_api_password)
tg_api_handler = TelegramAPI(tg_api_token)

def run():
    pass
