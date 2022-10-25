# banner: https://patorjk.com/software/taag/#p=display&f=Colossal

import discord, sys, os, platform
from discord.ext import commands
from settings import token, prefix

__author__ = "@ivwy (3468#3468)"
__version__ = "v1.1.0"

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = prefix, help_command = None, intents = intents)

def banner():
    sys.stdout.buffer.write(f'''
                                                                    
  ,ad88PPP88ba,   88                         Author: {__author__}
 d8"  .ama.a "8a  ""                         Version: {__version__}
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