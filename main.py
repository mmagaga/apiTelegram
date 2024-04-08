import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7158227562:AAF6goTkKY2gQN1vBAPUc4nuKQOanVhrs8M'

# Константы с сообщениями
TEXT_MESSAGE = 'Ого! ты мне прислал текст!'
TEXT_PHOTO = 'Ого! ты мне прислал фото!'
TEXT_STICKER = 'Ого! ты мне прислал стикер!'
TEXT_VIDEO = 'Ого! ты мне прислал видео!'
TEXT_VOICE = 'Ого! ты мне прислал голосовое сообщение!'

MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет


    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()


    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            type_message = result['message']

            if type_message.get('text'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_MESSAGE}')
            elif type_message.get('sticker'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_STICKER}')
            elif type_message.get('photo'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_PHOTO}')
            elif type_message.get('video'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_VIDEO}')
            elif type_message.get('voice'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT_VOICE}')
    time.sleep(1)
    counter += 1