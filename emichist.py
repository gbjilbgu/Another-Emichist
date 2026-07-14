import discord
from discord.ext import commands
from MorseCodePy import encode,decode
from flask import Flask
from threading import Thread
import os
# Khởi tạo bot với tất cả quyền (Intents)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Make "+bot.user.name+" moaned successfully!")

@bot.event
async def on_message(message):
    #dica = {" ":"mmhmm","a":"mh",}
    if message.author == bot.user:
        return
    mes = message.content.lower()
    #print(mes)
    if mes == "ahola":
        await message.channel.send("mmmm m mhmm mhmm hhh mmhmm hh hmhh mmhmm hmm m mh mhm mmhmm m hh mm hmhm mmmm mm mmm h mmhmm mmhm mhm mm m hm hmm mmhmm mmmm hhh mhh mhhhhm mmm mmhmm hhm hhh mm hm hhm mmhhmm")
    elif mes[0:3] == "aen":
        if mes[-1] != "c":
            adi = encode(mes[4:-1]+mes[-1],language = 'english')
        else:
            adi = encode(mes[4:-1],language = 'english')+" -.-."
        #print(adi)
        cou = 0
        an = ""
        #adi = adi.split()
        for x in adi:
            if x == ".":
                an = an + "m"
            elif x == "-":
                an = an + "h"
            elif x == "/":
                an = an + "mmhmm"
            elif x == " ":
                an = an + " "
            try:
                if len(an)>= 6:
                    if an[len(an)-6:len(an)] == " hhhh ":
                        an = an[0:len(an)-6]
                        an = an + " hmhm mmmm "
                elif len(an) == 5:
                    if an[0:5] == "hhhh ":
                        an = ""
                        an = an + "hmhm mmmm "
            except:
                continue
        if an[len(an)-5:len(an)] == " hhhh":
            an = an[0:len(an)-5]
            an = an + " hmhm mmmm"
        await message.channel.send(an)
    elif mes[0:3] == "ade":
        adi = mes[4:-1]+mes[-1]
        mes = adi.split()
        an = ""
        #print(mes)
        for x in mes:
            if x != "mmhmm":
                for i in x:
                    if i == "m":
                        an = an + "."
                    elif i == "h":
                        an = an + "-"
                an = an + " "
            else:
                an = an + "/ "
        #raise ValueError(an)
        an = decode(an,language = 'english').lower()
        await message.channel.send(an)
    elif mes[0:3] == "aus":
        await message.channel.send("""# Here are some frequently-used lines:
**Mhm**""")
        await message.channel.send("hh mmmm hh")
        await message.channel.send("## **Praying**")
        await message.channel.send("mh mmm mmhmm mh hm mmhmm m hh mm hmhm mmmm mm mmm h mmhmm mm mmhmm hhh hmmm m hmhh mmhmm m hh mm hmhm mmmm mm mmm hh")
        await message.channel.send("## **Agree/Disagree**")
        await message.channel.send("### Yeah")
        await message.channel.send("hmhh m mh mmmm")
        await message.channel.send("### Aight")
        await message.channel.send("mh mm hhm mmmm h")
        await message.channel.send("hm mh mmmm")
        await message.channel.send("## **Expressing skibidi emotion**")
        await message.channel.send("### Holy")
        await message.channel.send("mmmm hhh mhmm hmhh")
        await message.channel.send("### Wow")
        await message.channel.send("mhh hhh mhh")
        await message.channel.send("## Bow")
        await message.channel.send("hmmm hhh mhh")
        await message.channel.send("### Aight ima bow abit")
        await message.channel.send("mh mm hhm mmmm h mmhmm mm hh mh mmhmm hmmm hhh mhh mmhmm mh hmmm mm h")
        await message.channel.send("### Sadly, i have to bow now, bow")
        await message.channel.send("mmm mh hmm mhmm hmhh hhmmhh mmhmm mm mmhmm mmmm mh mmmh m mmhmm h hhh mmhmm hmmm hhh mhh mmhmm hm hhh mhh hhmmhh mmhmm hmmm hhh mhh")
    elif mes[0:5] == "ahelp":
        await message.channel.send("""### ----Hello my dear emichist, I am your assistant helping you on the road to the glorious mhm heaven----
        ### Bot commands:
        aen [text]: Transform normal text to emiscript
        ade [text]: Translate emiscript to normal text
        aus       : Show frequenly-used lines""")
    await bot.process_commands(message)
app = Flask('')

@app.route('/')
def home():
    return "Make "+bot.user.name+" moaned successfully!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
keep_alive()
bot.run(os.environ.get("DISCORD_TOKEN")) #Actually in this run() contains a bot token
