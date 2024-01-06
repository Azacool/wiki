import telebot
import wikipedia, re
from dotenv import load_dotenv
load_dotenv()
import os


BOT_TOKEN =os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


wikipedia.set_lang("eng")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        a=wikitext.split('.')
        a = a[:-1]
        wikitext2 = ''
        for x in a:
            if not('==' in x):    
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'Can you enter something else, cause I could not find any information on wikipedia'

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Hey there!')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))