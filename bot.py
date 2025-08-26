import discord
from discord.ext import commands
import os

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Add more commands here...

# Run the bot
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
