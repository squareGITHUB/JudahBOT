import discord
import os

from dotenv import load_dotenv
from discord.ext import commands
from re import match

class JudahBOT(discord.Client):
    extensions = [
        'cogs.events.events'
    ]

    if __name__ == "__main__":
        try:
            #[map(discord.Client.load_extension(), extensions)]
            commands.Bot.load_extension()
        except Exception as err:
            print(f"Loading Error: {err}")
            
    async def on_message(self,message):
        if message.author.id == client.user.id:
            return
        channel = message.channel
        if match("<@!?788091175197999158>", message.content) is not None:
            await channel.send("Why?")
            print(f"{message.author} mentioned SquarePY in {channel}: {message.content}")

            
client = JudahBOT(prefix=os.getenv('prefix'))
load_dotenv()

client.run(os.getenv('token'))
