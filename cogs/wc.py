import discord
from discord import File
from discord.ext import commands
from discord.utils import get
from easy_pil import Editor, load_image_async, Font

class wc(commands.Cog, name='Wc'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
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

        background = Editor("assets/pic1.jpeg")
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
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"[INFO][SERVER]: Recognised that a member called {member.name}#{member.discriminator} left.")
        channel = member.guild.system_channel
        e = discord.Embed(title=f"{member.name}#{member.discriminator} has left the server", description=f"We will miss you...", color=discord.Color.red())
        await channel.send(embed=e)

def setup(bot):
    bot.add_cog(wc(bot))