import message,app,converter
import telegram
import os
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import CommandHandler,MessageHandler,filters,ApplicationBuilder,CallbackQueryHandler
with open("token.bot","r",encoding="utf-8") as file:
    bot=ApplicationBuilder().token(file.read()).build()
async def text(update,contextt):
    info=update.effective_user
    if not os.path.exists("cach/" + str(info.id)):
        os.makedirs("cach/" + str(info.id))
    HTML=converter.markdown(update.message.text,extras=["markdown-in-html"])    
    fName=["new HTML document"]
    with open("cach/" + str(info.id) + "/" + ".".join(fName) + ".html","w",encoding="utf-8") as SAve:
        SAve.write(HTML)
    await contextt.bot.send_document(chat_id=info.id, document=open("cach/" + str(info.id) + "/" + ".".join(fName) + ".html","rb"),caption="made by {}".format(str(info.id)))
    os.remove("cach/" + str(info.id) + "/" + ".".join(fName) + ".html")

async def File(update,contextt):
    info=update.effective_user
    file=update.message.document
    name=file.file_name
    get_file=await update.message.effective_attachment.get_file()
    if not os.path.exists("cach/" + str(info.id)):
        os.makedirs("cach/" + str(info.id))
    await get_file.download_to_drive("cach/" + str(info.id) + "/" + name)
    with open("cach/" + str(info.id) + "/" + name,"r",encoding="utf-8") as markdown:
        HTML=converter.markdown(markdown.read(),extras=["markdown-in-html"])
    os.remove("cach/" + str(info.id) + "/" + name)
    fName=name.split(".")
    fName.pop(-1)
    with open("cach/" + str(info.id) + "/" + ".".join(fName) + ".html","w",encoding="utf-8") as SAve:
        SAve.write(HTML)
    await contextt.bot.send_document(chat_id=info.id, document=open("cach/" + str(info.id) + "/" + ".".join(fName) + ".html","rb"),caption="made by {}".format(str(info.id)))
    os.remove("cach/" + str(info.id) + "/" + ".".join(fName) + ".html")
async def start(update,contextt):
    info=update.effective_user
    keyboard=InlineKeyboardMarkup([[InlineKeyboardButton("donate",url="https://www.paypal.me/AMohammed231")],[InlineKeyboardButton("help",callback_data="help")]])
    await message.Sendmessage(chat_id=info.id,text="welcome " + str(info.first_name) + "to this bot. this bot make you converting markdown files (.md) to html files(.html). please send markdown file or text message ",reply_markup=keyboard)
async def helb(update,contextt):
    links="""<a href="https://t.me/mesteranasm">telegram</a>

<a href="https://t.me/tprogrammers">telegram channel</a>

<a href="https://x.com/mesteranasm">x</a>

<a href="https://Github.com/mesteranas">Github</a>

email:
anasformohammed@gmail.com

<a href="https://Github.com/mesteranas/markdownToHTML_telegram_bot">visite project on Github</a>
"""
    info=update.effective_user
    await message.Sendmessage(info.id,"""name: {}\nversion: {}\ndescription: {}\n developer: {}\n contect us {}""".format(app.name,str(app.version),app.description,app.developer,links))
async def callBake(update,contextt):
    q=update.callback_query
    q.answer()
    if q.data=="help":
        await helb(update,contextt)

print("running")
bot.add_handler(CommandHandler("start",start))
bot.add_handler(CommandHandler("help",helb))
bot.add_handler(CallbackQueryHandler(callBake))
bot.add_handler(MessageHandler(filters.Document.ALL,File))
bot.add_handler(MessageHandler(filters.TEXT,text))
bot.run_polling()