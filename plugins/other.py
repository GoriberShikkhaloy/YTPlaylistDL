from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):

	makup = [InlineKeyboardButton("Help", callback_data=f"helptxt_{k.message_id}"),
					InlineKeyboardButton("About", callback_data=f"abouttxt_{k.message_id}")]

	k = await client.send_message(message.chat.id, "...", reply_to_message_id=message.message_id)
	await k.edit(
		f"Hi {message.from_user.mention},If you need any help, Just click help button.\n\nProject by @Harp_Tech",
		reply_markup=makup
	)

@Client.on_callback_query()
async def cb_handler(client, message):
	cb_income_dt = int(message.data.split("_", 1)[1])
	print(cb_income_dt)
	await client.send_message(message.chat.id, "Hello")