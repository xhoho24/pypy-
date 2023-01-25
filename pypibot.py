from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from SafoneAPI import SafoneAPI
import random, json, requests

api = SafoneAPI()


bot = Client(
    "PyPiBot",
    api_hash="578d2817642f3aa3a283efaf49f4ef4e",
    api_id=int(12845924),
    bot_token="5972476937:AAH1IGo_8r_2Ss362Z8VEsi_EUm6YRCozwA",
)

@bot.on_message()
async def msg_handler(client, message: Message):
    word = message.text

    if word == "/start":
        await message.reply_text("Hello, I'm a bot that searches for people in Safone, support \nhttps://t.me/+AeGtX3FeftE3ZTEx ")
    elif word == "/help":
        await message.reply_text("/start - Starts the bot.\n/help - Shows this message.")
    elif message.text:

        # resp = await api.pypi(word) # se puede hacer asi o directametne leyendo el json
        # name_p = resp['title']
        # ver_p = resp['version']
        # link_p = resp['link']
        # desc = resp['description']
        # lic_p = resp['license']
        # auth_p = resp['author']
        # homepage = resp['homePage']

        
        resp = requests.get(f"https://api.safone.me/pypi?query={word}")
        text = resp.text
        data = json.loads(text)
        alld = data
 
        # # print(resp)
        try:
            photo_p = ["https://telegra.ph/file/bbf42a8fca1d6929eedf4.png", "https://pbs.twimg.com/media/Ek8HiWJVcAAuJzo.jpg", "https://i.pinimg.com/736x/90/6c/04/906c04cb852f20fad832f1bcdf0730d8.jpg", "https://miro.medium.com/max/1027/1*Ud_bNdeWPf4iN1EcydaDFA.png", "https://64.media.tumblr.com/0b46d69c48c1cb1b79e7d53bf833c4c5/tumblr_ple9w8tU7L1qgros1_1280.png", "https://memezila.com/saveimage/I-need-a-network-specialist-with-some-python-experience-meme-1014", "https://i.pinimg.com/originals/f6/2e/4d/f62e4d513d72d64f0dc1ad346a48c4fc.jpg", "https://res.cloudinary.com/practicaldev/image/fetch/s--JNykQRzX--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x3l1zomu6ll1bnajfudo.png", "https://pbs.twimg.com/media/Dj0-wpfVAAEyAEj.jpg", "https://miro.medium.com/max/300/0*Z7zq0nZPcE5yNuHq.png", "https://telegra.ph/file/1b592c748bfef091effa1.png", "https://telegra.ph/file/9c3a6e9858aab2f77f712.png", "https://telegra.ph/file/631efc43d70f3358d4e76.png", "https://telegra.ph/file/5b8ac9cb294fbbf0e6323.png", "https://telegra.ph/file/a778f2cc82a4043612a66.png", "https://telegra.ph/file/9679195efeab6d3e43995.png", "https://telegra.ph/file/9e1a06f3a2670485bb44b.png"]
            name_p = alld['title']
            ver_p = alld['version']
            link_p = alld['link']
            desc = alld['description']
            lic_p = alld['license']
            auth_p = alld['author']
            homepage = alld['homePage']
            await message.reply_photo(photo=random.choice(photo_p), caption=f'Nombre: {name_p}\n\n Link: {link_p}\n\n Version: {ver_p}\n\n Descripcion: {desc}\n\n Licencia: {lic_p}\n\n Autor: {auth_p}\n\n Link principal: {homepage}')
        except Exception as e:
            await message.reply_text("El Modulo que intenta buscar no existe")
    elif message.video:
        await message.reply_text("manda texto xd no videos ")
    elif message.photo:
        await message.reply_text("manda texto xd no fotos")
    elif message.sticker:
        await message.reply_text("manda texto xd no stikers XD")
    elif message.document:
        await message.reply_text("manda texto no documentos ekisde")
    elif message.audio:
        await message.reply_text("eres tonto? no te quiero escuchar manda texto")

if __name__ == "__main__":
    print("Bot is running...")
    bot.run()
