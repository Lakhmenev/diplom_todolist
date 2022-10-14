from bot.tg.client import TgClient
from django.core.management import BaseCommand
from todolist import settings


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tg_client = TgClient(settings.BOT_TOKEN)

    def handle(self, *args, **options):
        """
        Функция в бесконечном цикле создает оповещения о новых сообщениях юзеров, для каждого нового
        сообщения передается ответ в зависимости от инструкций функции self.handle_message
        :param args:
        :param options:
        """
        offset = 0
        while True:
            res = self.tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                self.tg_client.send_message(chat_id=item.message.chat.id, text=item.message.text)
