# banner: https://patorjk.com/software/taag/#p=display&f=Colossal

import discord, sys, os, platform
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from settings import token, prefix

__author__ = "@ivwy (3468#3468)"
__version__ = "v1.1.0"

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = prefix, help_command = None, intents = intents)

def banner():
    sys.stdout.buffer.write(f'''
Author: {__author__}
Version: {__version__} 
                                                                    
  ,ad88PPP88ba,   88                                                
 d8"  .ama.a "8a  ""                                                
d8'  ,8P"88"  88                                                    
88  .8P  8P   88  88  8b       d8  8b      db      d8  8b       d8  
88  88   8'   8P  88  `8b     d8'  `8b    d88b    d8'  `8b     d8'  
88  8B ,d8 ,ad8'  88   `8b   d8'    `8b  d8'`8b  d8'    `8b   d8'   
"8a "88P"888P"    88    `8b,d8'      `8bd8'  `8bd8'      `8b,d8'    
 `Y8aaaaaaaad8P   88      "8"          YP      YP          Y88'     
    """""""""                                              d8'      
                                                          d8'       
'''.encode('utf-8'))

@client.event
async def on_ready():
    banner()
    print(f"[INFO][SYSTEM]: You have logged in as {client.user.name}.")
    print(f"[INFO][SYSTEM]: With ID {client.user.id}.")
    print(f"[INFO][SYSTEM]: Total {len(client.guilds)} servers connected.")
    print(f"[INFO][SYSTEM]: Running on {platform.system()} {platform.release()} ({os.name})")
    print(f"[INFO][SYSTEM]: API version {discord.__version__}.")
    print(f"[INFO][SYSTEM]: Python version {platform.python_version()}.\n")

    await client.change_presence(
    status = discord.Status.idle,
    activity = discord.Activity(
        type = discord.ActivityType.streaming,
        name = f"in {len(client.guilds)} servers. | {prefix}help"))

@client.event 
async def on_member_join(member):
    print(f"[INFO][SERVER]: Recognised that a member called {member.name}#{member.discriminator} joined.")

    channel = member.guild.system_channel
    position = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)

    if position == 1:
        ordinal = "st"
    elif position == 2:
        ordinal = "nd"
    elif position == 3:
        ordinal = "rd"
    else: ordinal = "th"

    background = Editor("assets/pic1.jpg")
    profile_image = await load_image_async(str(member.avatar.url))
    profile = Editor(profile_image).resize((150, 150)).circle_image()
    poppins = Font.poppins(size=50, variant="bold")
    poppins_small = Font.poppins(size=23, variant="light")
    background.paste(profile, (325, 90))
    background.ellipse((325, 90), 150, 150, outline="white", stroke_width=5)
    background.text((400, 260), f"Welcome to {member.guild.name}", color="white", font=poppins, align="center")
    background.text((400, 320), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
    background.text((400, 350), f"You are the {position}{ordinal} Member Joined", color="#0BE7F5", font=poppins_small, align="center")
    file = File(fp=background.image_bytes, filename="welcome.jpg")
    await channel.send(file=file)

@client.event
async def on_member_remove(member):
    print(f"[INFO][SERVER]: Recognised that a member called {member.name}#{member.discriminator} left.")
    channel = member.guild.system_channel
    e = discord.Embed(title=f"{member.name}#{member.discriminator} has left the server", description=f"We will miss you...", color=discord.Color.red())
    await channel.send(embed=e)

for file in os.listdir(f"./cogs"):
    if file.endswith(".py"):
        extension = file[:-3]
        try:
            client.load_extension(f"cogs.{extension}")
            print(f"[INFO][SYSTEM]: Succesfully loaded {extension}.")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(f"[INFO][SYSTEM]: Failed to load extension {extension}\n{exception}")

try:
    client.run(token)
except Exception as error:
    print(f"[INFO][SYSTEM]: Error when logging in: {error}.")