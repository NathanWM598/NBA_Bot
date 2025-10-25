from discord.ext import tasks
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

channel = None

@client.event
async def on_ready():
    print(f'NBA Bot is ready!')
    fetch_game.start()

@client.event
async def on_message(message: discord.Message):
    if(message.content.startswith('$hello')):
        await message.channel.send('Hello!')

@tasks.loop(seconds=10.0)
async def fetch_game():
    channel = client.get_channel(1178948192872710194)
    games = [
        {'home' : 'Lakers'}
    ]
    await channel.send(games)
