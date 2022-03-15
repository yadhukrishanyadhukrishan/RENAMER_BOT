
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filenameto rename it__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/Mo_Tech_Group"), 
	  InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/MoTech_YT")
          ],[
          InlineKeyboardButton("🧩 Deploy 🧩", url="https://youtu.be/7ALYUk-rYMc")
          ]]
          )
        )



