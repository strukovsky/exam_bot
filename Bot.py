from Database import Database
from vk_api.utils import get_random_id
import Keyboards


class Bot:
    def __init__(self, vk_session):
        self.db = Database()
        self.vk_session = vk_session
        self.vk = vk_session.get_api()

    def hello_user(self, user_id):
        self.db.add_user(user_id)
        self.send_message(user_id=user_id, message="Привет! Спасибо за участие в развитии бота!\n Он обязательно "
                                                   "поможет тебе подготовиться к сессии, напоминая раз\n  в полчаса"
                                                   "что надо чучуть поботать :)", keyboard=Keyboards.active())

    def activate_user(self, user_id):
        self.db.add_user(user_id)
        self.send_message(user_id=user_id, message="С возвращением!", keyboard=Keyboards.active())

    def deactivate_user(self, user_id):
        self.db.deactivate_user(user_id)
        self.send_message(user_id=user_id, message="Очень жаль, тебя не будет хватать :(",
                          keyboard=Keyboards.inactive())

    def thanks_user(self, user_id):
        self.send_message(user_id=user_id, message="Тебе спасибо :)", keyboard=Keyboards.after_thanks())

    def notify_users(self):
        active = self.db.get_active()
        if len(active) == 0:
            print("Notify: no active users")
            return

        online = self.vk_session.method('users.get', {
            'user_ids': ','.join(map(str, active)),
            'fields': 'online'
        })
        resulting_ids = []
        for person in online:
            if person['online']:
                resulting_ids.append(person['id'])
        if len(resulting_ids) == 0:
            print("Notify: no online users")
            return
        result = ','.join(map(str, resulting_ids))

        self.vk_session.method('messages.send', {
            'message': 'Обязательно поботай!',
            'random_id': get_random_id(),
            'user_ids': result,
            'keyboard': Keyboards.active()
        })

    def send_message(self, user_id, message, keyboard):
        self.vk_session.method('messages.send', {
            'message': message,
            'random_id': get_random_id(),
            'user_ids': user_id,
            'keyboard': keyboard
        })

    def handle_messages(self):
        convs = self.vk_session.method('messages.getConversations',
                                       {
                                           'count': 200,
                                           'filter': 'unread'
                                       })
        if convs['count'] == 0:
            return

        for conv in convs['items']:
            user_id = conv['conversation']['peer']['id']
            text = conv['last_message']['text'].lower()
            if 'начать' in text:
                self.hello_user(user_id)
            elif 'отписаться' in text:
                self.deactivate_user(user_id)
            elif 'включить' in text:
                self.activate_user(user_id)
            elif 'спасибо' in text:
                self.thanks_user(user_id)
