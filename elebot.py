#Импорт самого бота
import telebot
from telebot  import types
bot = telebot.TeleBot('5971640105:AAFQsjRcLZPdH6vRNyTWFUvkJICYX4APeME')

#Отслеживание и обработка крманды старт
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, {message.from_user.first_name} {message.from_user.last_name}! Добро пожаловать в TgLibBot - твоя библиотека цифровых книг! Ввдеите /books, чтобы начать искать книги или /info, чтобы узнать больше о боте."
    bot.send_message(message.chat.id,mess)
#Отслежевание и обработка обычного текста


#Отслеживание и обработка команды букс, она открывает меню с кнопками, где можно выбрать жанр книг
@bot.message_handler(commands=['books'])
def books(message):
        markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        historyadventoures = types .KeyboardButton('Истроические приключения') 
        fantasy = types .KeyboardButton('Фэнтези')
        fantastic = types .KeyboardButton('Фантастика')
        markup.add(historyadventoures, fantasy, fantastic)
        bot.send_message(message.chat.id, 'Отлично! Вы решили приступить к поиску книг! Выберите жанр.', reply_markup=markup)
#А вот тут выодятся книги в определённых категриях
        def buttons(message):
            if message.text == 'Истроические приключения':
                markup =types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                #Сюда добавляются книги
                ostrovsokrovisch = types .KeyboardButton('Остров сокровищ. Р. Стивенсон')
                markup.add(ostrovsokrovisch)
            elif message.text == 'Фэнтези':
                #Сюда добавляются книги
                bot.send_message(message.chat.id, 'Пока ничего нет')
            elif message.text == 'Фантастика':
                #Сюда добавляются книги
                bot.send_message(message.chat.id, 'Пока ничего нет')
#Тут уже выдаются книги
def vadacha(message):
    if message.text == 'Остров сокровищ. Р. Стивенсон':
        file=open('C:/Users/pupit/Documents/Остров сокровищ. Р. Стивенсон .fb2', 'rb')
    #Добавить книги
                
#Отслежевание и обработка фото    
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Отличное фото, хоть я его не вижу, так-как я не могу распозновать картинки, ваша картинка мне действительно нравится!')

#Отслежевание и обработка аудио
@bot.message_handler(content_types=['audio'])
def get_user_audio(message):
    bot.send_message(message.chat.id, 'Отлично сказанно! Хоть я и не понимаю, что вы сказали, так-как я не могу распозновать аудио, ваша речь мне действительно нравится!')
    
#Отслежевание и обработка видео    
@bot.message_handler(content_types=['video'])
def get_user_video(message):
    bot.send_message(message.chat.id, 'Отличное видео, хоть я его не понимаю, так-как я не могу распозновать видео, ваше видео мне действительно нравится!')
    
#Отслежевание и обработка стикеров    
@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id, 'Этот стикер отлично подходит к данной ситуации!')
#Вызов бота
bot.polling(none_stop=True)
