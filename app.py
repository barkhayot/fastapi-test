import telebot
from pytube import YouTube  
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

link = "https://www.youtube.com/watch?v=w9TcErzdoTg"

def get_audio(link):
    yt = YouTube(link)  

    try:
        # yt.streams.filter(progressive = True,  file_extension = "mp4").first().download(output_path = "./", 
        # filename = "mmmm.mp4")
        stream = yt.streams.filter(only_audio=True).first(). download(output_path = "./", filename = "eee.mp3")
    except:
        print("Some Error!")
    print('Task Completed!')

import insta
import bf
bot = telebot.TeleBot("5444195255:AAFdov1TjVD9YOHyeOn8dYIqgjqIGLlBdUs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    #if(message.text[:31] == "https://www.youtube.com/"):
        data = bf.get_audio(message.text)
        if data == False:
            bot.reply_to(message, "The link that you have shared is on Privet Account! We have no Access !")
        else:
            print(message.text)
            file = open("eee.mp3", "rb")
            bot.send_audio(message.chat.id, file, timeout=10000)
    #else:
	    #bot.reply_to(message, "Your Link is not valid! Please send Valid Link !")
bot.infinity_polling()
