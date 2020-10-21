import telepot
import sys, time
from config import TOKEN
from pprint import pprint

bot = telepot.Bot("TOKEN") #inserire il Token del bot fornito da BotFather.

print(bot.getMe())

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)

	if content_type == "text":
		bot.sendMessage(chat_id, msg["text"])

#inline keyboard:
def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	keyboard = InlineKeyboardMarkup(inline_keyboard=[
		[InlineKeyboardButton(text="Click here", callback_data='press')],
		])

	
bot.message_loop(handle)

response = bot.getUpdates()
pprint(response)

while 1:
	time.sleep(3)

