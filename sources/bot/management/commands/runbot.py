from bot.tg.client import TgClient
from django.core.management import BaseCommand

# from todolist import settings


class Command(BaseCommand):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.tg_client = TgClient(settings.BOT_TOKEN)

    def handle(self, *args, **options):
        offset = 0
        tg_client = TgClient('token')
        while True:
            res = tg_client.get_updates(offset=offset)
            for item in res.result:
                offset = item.update_id + 1
                print(item.message)
