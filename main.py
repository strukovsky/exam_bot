import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from Bot import Bot
import time
vk_session = vk_api.VkApi(token="here token appears")

b = Bot(vk_session)
INTERVAL_LENGTH = 10
MAX_INTERVALS = 180
CURRENT_INTERVAL = 0
while 1:
    b.handle_messages()
    CURRENT_INTERVAL += 1
    if CURRENT_INTERVAL == MAX_INTERVALS:
        CURRENT_INTERVAL = 0
        b.notify_users()
    time.sleep(INTERVAL_LENGTH)



