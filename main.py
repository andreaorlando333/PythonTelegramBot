import telepot
import sys, time
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
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
	
	bot.sendMessage(chat_id, "Utilizza la inline keyboard", reply_markup=keyboard)

def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
	print("Callback Query: ", query_id, from_id, query_data)
	
	bot.answerCallbackQuery(query_id, text="Ok!")

	
bot.message_loop({'chat': on_chat_message,
		  'callback_query': on_callback_query})

response = bot.getUpdates()
pprint(response)

while 1:
	time.sleep(3)

