import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import json

# list
Buttons_back = ['keyboard', 'назад', 'главное меню', 'back','начать', 'menu', 'привет']
f = []
#funcs
def get_button(label, color, payload = ''):
	return {
		"action": {
		'type': 'text',
		'payload': json.dumps(payload),
		'label': label

		},
		'color': color

	}
def write_msg(id, message, keyboard=None, sticker_id=None):
    vk.method('messages.send', {'peer_id': id, 'sticker_id': sticker_id,'message': message,'keyboard': keyboard, 'random_id': random.randint(1, 100000000)})
def writeinconv(id, message, sticker_id=None):
    vk.method('messages.send', {'peer_id': id, 'sticker_id': sticker_id,'message': message, 'sticker_id': sticker_id, 'random_id': random.randint(1, 100000000)})


#keyboards
keyboard = {
	'one_time': False,
	'buttons': [
	[get_button(label = 'Погода', color = 'primary'),
	get_button(label = 'Расписание', color = 'positive')]
	]
}

keyboard_rasp = {
	'one_time': False,
	'buttons': [
    [get_button(label = 'Звонки', color = 'primary'), get_button(label = 'Уроки', color = 'positive')],



	]
}

keyboard_yroki = {
	'one_time': False,
	'buttons': [
    [get_button(label = 'Понедельник', color = 'positive'), get_button(label = 'Вторник', color = 'negative'), get_button(label = 'Среда', color = 'positive')],
    [get_button(label = 'Четверг', color = 'positive'), get_button(label = 'Пятница', color = 'positive'), get_button(label = 'Суббота', color = 'positive')],
    [get_button(label = 'Назад', color = 'secondary')],
	]
}



vk = vk_api.VkApi(token='')
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, '187254286')

#json
keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
keyboard_rasp = json.dumps(keyboard_rasp, ensure_ascii = False).encode('utf-8')
keyboard_rasp = str(keyboard_rasp.decode('utf-8'))
keyboard_yroki = json.dumps(keyboard_yroki, ensure_ascii = False).encode('utf-8')
keyboard_yroki = str(keyboard_yroki.decode('utf-8'))

for event in longpoll.listen():

    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.object.peer_id != event.object.from_id:
            if event.object.peer_id not  in f:
                f.append(event.object.peer_id)
            if 'пидор' in event.object.text.lower():
                vk.method('messages.send', {'peer_id': event.object.peer_id, 'message': 'сам пидор блять, уебище', 'random_id': random.randint(1,100000000)})
            elif '!понедельник' in event.object.text.lower():
                vk.method('messages.send', {'peer_id': event.object.peer_id, 'message': '1-2: Физика (𝔂𝖗𝒶 𝒻ιչʀå)\n3-4: Какая-то херня\n5-6: Алгебра ( у Козлодоя)\n7: Псих тренинг (для психов)\n8-9: Геометрия',
                                            'random_id': random.randint(1, 1000000000)})
            elif '!среда' in event.object.text.lower():
                vk.method('messages.send', {'peer_id': event.object.peer_id, 'message': '1: География\n2-3: Спецмат\n4: Химия (ʞɐʞ ʌɐɹıʇq ɯǝɟ)\n5-6: Литература\n7-8: Геометрия\n9: Беседа алкашей\n10: География (石人牙ть ⺁具🝗 牙)',
                                            'random_id': random.randint(1, 10000000)})
            elif '!четверг' in event.object.text.lower():
                writeinconv(event.object.peer_id,'1: Англ\n2:Физра (у̸̢̼͉̒́̒р̸̡̙̐̒͐а̸͍͚́͛̈́͜ ф̸͍̠̼̀͠͝и̵͍͇̝́͋̕з̵͎͍͚͐̕и̴̠͔̦̓͐͠к̵̡͍̦̀̓̕а̴̺͖͐͊͒͜)\n3: МХК\n4. Биология\n5-6: Алгебра, 406\n7: Англ\n8: Опять беседы с батюшкой, 304\n9: Физра')
            elif '!пятница' in event.object.text.lower():
                writeinconv(event.object.peer_id, '1-2: Инфа, 502/401 м̵̙̻͋͌͐͜а̴̠͓̘͆͊̚ч̵̫͖̠̾̕͝н̸̟̞͔̈́́̚ё̴͔̟͍̽́͊в̸̢̡̼͊̀͝ к̵̞̫͕͒̔̒ д̴̙̘̓͌͘о̵̪͙͇̔͒̈́с̴͇͖͙͊̓͠к̵͍̫̐͑͋͜е̸͙̟͉́̀̿\n3-4: Руссек, 203\n5-6: Физика, 308\n7: Общество, 207\nАнгл (₥¥ êñg ï§ †hê ¢åþï†åł ð£ ñðr†h kðrêå)')
            elif '!суббота' in event.object.text.lower():
                writeinconv(event.object.peer_id, '1-2: История, 207\n3-4: Опять параша кая-то\n5: ОБЖ, 404\n6: Беседы с алкашами\n7: Физра\n8-9: Электив по физике, 308')

        elif event.object.peer_id == event.object.from_id:
            if event.object.peer_id not in f:
                f.append(event.object.peer_id)
            if event.object.text.lower() in Buttons_back:

                if event.object.text.lower() == 'привет' or event.object.text.lower() == 'начать':
                    a = vk.method('users.get', {'user_ids': event.object.peer_id})[0]['first_name']
                    write_msg(event.object.peer_id, 'Дарова, '+str(a), keyboard=keyboard_rasp)
                else:
                    write_msg(event.object.peer_id,'234', sticker_id=163, keyboard=keyboard_rasp)
            elif event.object.text.lower() == 'расписание':
                write_msg(event.object.peer_id, 'lol', keyboard_rasp)
            elif event.object.text.lower() == 'звонки':
                write_msg(event.object.peer_id, '1. 9:00 - 9:45\n2. 9:50 - 10:35\n3. 10:45 - 11:30\n4. 11:50 - 12:35\n5. 12:45 - 13:30\n6. 13:40 - 14:25\n7. 14:45 - 15:30\n8. 15:40 - 16:25\n9. 16:30 - 17:15\n10. 17:20 - 18:05')
            elif event.object.text.lower() == 'уроки':
                write_msg(event.object.peer_id, 'choose', keyboard_yroki)
            elif event.object.text.lower() == 'понедельник':
                write_msg(event.object.peer_id, '1-2: Физика (𝔂𝖗𝒶 𝒻ιչʀå), 308\n3-4: Какая-то херня\n5-6: Алгебра ( у Козлодоя), 403\n7: Псих тренинг (для психов), 304\n8-9: Геометрия, 307')
            elif event.object.text.lower() == 'вторник':
                write_msg(event.object.peer_id, 'У тебя все хорошо ебланище?\nТебе вчерашняя беседа алкоголиков не помогла?')
            elif event.object.text.lower() == 'среда':
                write_msg(event.object.peer_id, '1: География, 205\n2-3: Спецмат, 403/405\n4: Химия, 208 (ʞɐʞ ʌɐɹıʇq ɯǝɟ)\n5-6: Литература, 307\n7-8: Геометрия, 406\n9: Беседа алкашей, 304\n10: География, 205 (石人牙ть ⺁具🝗 牙)')
            elif event.object.text.lower() == 'четверг':
                write_msg(event.object.peer_id, '1: Англ\n2:Физра (у̸̢̼͉̒́̒р̸̡̙̐̒͐а̸͍͚́͛̈́͜ ф̸͍̠̼̀͠͝и̵͍͇̝́͋̕з̵͎͍͚͐̕и̴̠͔̦̓͐͠к̵̡͍̦̀̓̕а̴̺͖͐͊͒͜)\n3: МХК, 405\n4. Биология, 407\n5-6: Алгебра, 406\n7: Англ\n8: Опять беседы с батюшкой, 304\n9: Физра')
            elif event.object.text.lower() == 'пятница':
                write_msg(event.object.peer_id, '1-2: Инфа, 502/401 м̵̙̻͋͌͐͜а̴̠͓̘͆͊̚ч̵̫͖̠̾̕͝н̸̟̞͔̈́́̚ё̴͔̟͍̽́͊в̸̢̡̼͊̀͝ к̵̞̫͕͒̔̒ д̴̙̘̓͌͘о̵̪͙͇̔͒̈́с̴͇͖͙͊̓͠к̵͍̫̐͑͋͜е̸͙̟͉́̀̿\n3-4: Руссек, 203\n5-6: Физика, 308\n7: Общество, 207\nАнгл (₥¥ êñg ï§ †hê ¢åþï†åł ð£ ñðr†h kðrêå)')
            elif event.object.text.lower() == 'суббота':
                write_msg(event.object.peer_id, '1-2: История, 207\n3-4: Опять параша кая-то\n5: ОБЖ, 404\n6: Беседы с алкашами\n7: Физра\n8-9: Электив по физике, 308')
                write_msg(event.object.peer_id, 'wikipedia: Элективный курс – это обязательный курс по выбору учащегося. Элективный курс (курс по выбору) обязателен для учащихся. Он играет важную роль в структуре профильного образования Элективные курсы направлены на развитие индивидуальных интересов и потребностей учащегося.')

