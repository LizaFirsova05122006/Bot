import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random

TOKEN = "vk1.a.gGcbglsYl3f5Oy_32KNVYTa8V6ZpI7H8j-kJpCtem0oGJ62RbzbV1fH_eNNfXdwWJRKFH2XdJWjvkwrqrjoZ-AtyE57ufD1Z8GDVutLPPLJKjlhwXJ7CjTzUmUlitvQDsQi2NVceTa8q0OGm55fe_JTmJxzFX4WnVZfUmOCA8XEealuj2JW3BOxCjgoGBxQiDQ8XuVd7Br5qBpPek8EjHg"

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)
session_api = vk.get_api()


def send_messages(chat_id, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'chat_id':chat_id, 'message':text, 'random_id':random_id})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.from_chat:
                admin = 'https://vk.com/lizavetka0512'
                chat_id = event.chat_id
                msg = event.text
                id = event.user_id
                user_get = session_api.users.get(user_ids=(id))
                user_get = user_get[0]
                first_name = user_get['first_name']
                privet = ['привет', 'здравствуйте', 'здравствуй']
                poka = ['пока', 'до свидания']
                blogodarnost = ['спасибо', 'благодарю']
                if msg.lower() in privet:
                    send_messages(chat_id, f'Здравствуйте, {first_name}! Я Бот сайта Российского туризма и меня зовут Александр. Вот, что я могу: \n'
                                           f'* Напишите "навигатор" и я подробно расскажу, как работает сайт \n'
                                           f'* Напишите "отзыв" - чтобы оставить отзыв о сайте \n'
                                           f'* Напишите "пожелания" - чтобы передать Ваши пожелания администратору \n'
                                           f'* Напишите "информация" - и я расскажу о сайте'
                                           f'* Напишите "викторина" - и я устрою викторину по регионам РФ')
                if msg.lower() == 'навигатор':
                    send_messages(chat_id, f'Попадая на сайт, Вы можете: \n'
                                           f'* Просмотреть информацию по каждому региону \n'
                                           f'* Просмотреть карту, на которой нанесены города РФ'
                                           f'* Просмотреть вкладки "Кинотеатры РФ" и "Театры РФ"'
                                           f'* Также по любым вопросам Вы можете обратиться к моему коллеге в Телеграмм и ко мне) \n'
                                           f'О чем из этого Вы хотели бы узнать больше?')
                if msg.lower() == 'отзыв':
                    send_messages(chat_id, f'Пожалуйста, поделитесь своими впчатлениями при просмотре сайта. Ваше сообщение будет просмотрено администратором')
                if msg.lower() == 'пожелания':
                    send_messages(chat_id, f'Пожалуйста, оставьте все свои пожелания. Они будут просмотрены администратором')
                if msg.lower() == 'информация':
                    send_messages(chat_id, f'Сайт "Российский туризм" предназначен для помощи людям в выборе напрвления для путешествия. \n'
                                           f'Администратор и разработчик сайта: {admin} \n'
                                           f'На сайте собраны все города с численностью от 50000 человек. На страничке каждого региона можно увидеть вкладки: "Уникальность каждого региона", "Города", "Причины поехать именно в этот регион" и конечно "Фотографии" \n')
                if msg.lower() in blogodarnost:
                    send_messages(chat_id, f'Всегда рад помочь)')
                if msg.lower() in poka:
                    send_messages(chat_id, f'До свидания, {first_name}! Рад был с Вами вести диалог)')