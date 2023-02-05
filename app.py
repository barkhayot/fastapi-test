

import telebot
from pytube import YouTube  
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

link = "https://www.youtube.com/watch?v=w9TcErzdoTg"

def get_audio(link):
    yt = YouTube(link)  

    try:
        stream = yt.streams.filter(only_audio=True).first(). download(output_path = "./", filename = "eee.mp3")
    except:
        print("Some Error!")
    print('Task Completed!')

bot = telebot.TeleBot("5635788651:AAE3ao8is0t2uajf-hteINZoeptPfhtSByg")
bot.set_webhook()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def echo_all(message):
        data = get_audio(message.text)
        if data == False:
            bot.reply_to(message, "The link that you have shared is on Privet Account! We have no Access !")
        else:
            print(message.text)
            file = open("eee.mp3", "rb")
            bot.send_audio(message.chat.id, file, timeout=10000)
if __name__ == "__main__":
    bot.infinity_polling()
