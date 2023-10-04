import discord
import requests
from discord.ext import commands

# Define your desired intents
intents = discord.Intents.default()
intents.typing = False  # Disable typing event
intents.presences = False  # Disable presence update event

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, traveler!')


@bot.event
async def on_message(message):
    # Check if the message is from a user & not the bot itself
    if message.author == bot.user:
        return

    if message.content.lower() == 'hello':
        # Respond to the user with a greeting
        await message.channel.send(f'Hello, {message.author.mention}!')

# Run the bot
bot.run('MTE1ODg1OTU5NTcxMjg0Mzg0Ng.GMU5PM.KBpi-n7kskR0OUzTgdZvXv_Hq6DYVGEqQlNtSE')
