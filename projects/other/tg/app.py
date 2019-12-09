# import configparser
import json
import socks

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

cfg = {
	'app' : {
		'api_id' : 0,
		'api_hash' : '',
		'username' : '',
		'mtproto' : {
			'test' : '149.154.167.40:443',
			'prod' : '149.154.167.50:443',
		}
	}
}

# Считываем учетные данные
# config = configparser.ConfigParser()
# config.read("config2.ini")

# print(config['Telegram'])

# Присваиваем значения внутренним переменным
api_id   = cfg['app']['api_id']
api_hash = cfg['app']['api_hash']
username = cfg['app']['username']

proxy = (socks.HTTP, '.ru', 0000, True, '', '')

client = TelegramClient(username, api_id, api_hash, proxy = proxy, timeout = timedelta(seconds = 15))
# , connection = connection.ConnectionTcpMTProxyRandomizedIntermediate, proxy = proxy
client.start()
# client.connect()

# with client:
# 	client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

# async def main():
# 	# url = input("Введите ссылку на канал или чат: ")
# 	# channel = await client.get_entity(url)
# 	# await dump_all_participants(channel)
# 	# await dump_all_messages(channel)
# 	# pass


# with client:
# 	client.loop.run_until_complete(main())
