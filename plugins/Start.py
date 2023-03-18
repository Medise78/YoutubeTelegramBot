from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery
from collections import defaultdict
from pytube import YouTube
from pyrogram.enums import ParseMode


def Tree():
    return defaultdict(Tree)


user_pocket = Tree()


@Client.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text("سلام")
    await message.reply_text("لطفا لینک را ارسال کنید")
    user_pocket[message.from_user.id]['step'] = 1


@Client.on_message(filters.text & ~filters.command("start"))
async def onMessage(client: Client, message: Message):
    if user_pocket[message.from_user.id]['step'] == 1:
        await message.reply_text("دریافت شد")
        yt = YouTube(message.text)
        file_name = f"{yt.title} - {yt.author}".replace("|", "-")
        yt.streams.filter(resolution='mp4').first().download(
            output_path="/home/medise/Documents"
        )
        await client.send_video(
            chat_id=message.chat.id,
            video=open(f'{file_name}.mp4', 'rb'),
            caption=file_name,
            parse_mode=ParseMode.HTML,
        )
