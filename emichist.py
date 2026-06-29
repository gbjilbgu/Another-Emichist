import discord
from discord.ext import commands
import morse_talk as mt
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
        adi = mt.encode(mes[4:-1]+mes[-1])
        #print(adi)
        cou = 0
        an = ""
        for x in adi:
            if x != " ":
                if cou == 7:
                    an = an + " mmhmm "
                    #await mem.edit(content = an)
                    cou = 0
                elif cou == 3:
                    cou = 0
                    an = an + " "
                    #await mem.edit(content = an)
                if x == ".":
                    an = an + "m"
                    #await mem.edit(content = an)
                elif x == "-":
                    an = an + "h"
                    #await mem.edit(content = an)
            else:
                cou += 1
        await message.channel.send(an)
    elif mes[0:3] == "ade":
        adi = mes[4:-1]+mes[-1]
        mes = adi.split()
        an = ""
        #print(mes)
        for x in range(0,len(mes)):
            if mes[x] != "mmhmm":
                for i in mes[x]:
                    if i == "m":
                        an = an + "."
                    elif i == "h":
                        an = an + "-"
                #if x>0 and x<len(mes):
                try:
                    if mes[x+1] != "mmhmm":
                        an = an + "   "
                except:
                    an = an
            else:
                an = an+"       "
        raise ValueError(an)
        an = mt.decode(an).lower()
        await message.channel.send(an)
    elif mes[0:3] == "aus":
        await message.channel.send("""# Here are some frequently-used line:
**Mhm**""")
        await message.channel.send("hh mmmm hh")
        await message.channel.send("**Praying**")
        await message.channel.send("mh mmm mmhmm mh hm mmhmm m hh mm hmhm mmmm mm mmm h mmhmm mm mmhmm hhh hmmm m hmhh mmhmm m hh mm hmhm mmmm mm mmm hh")
        await message.channel.send("**Agree/Disagree**")
        await message.channel.send("hmhh m mh mmmm")
        await message.channel.send("hm mh mmmm")
        await message.channel.send("**Holy**")
    await bot.process_commands(message)
app = Flask('')

@app.route('/')
def home():
    return "Bot đang chạy!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
keep_alive()
bot.run(os.environ.get("DISCORD_TOKEN")) #Actually in this run() contains a bot token
