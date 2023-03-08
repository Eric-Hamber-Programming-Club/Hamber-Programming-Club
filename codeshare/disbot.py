import discord

_TOKEN = "PUT_YOUR_TOKEN_HERE"

intents = discord.Intents(messages=True, message_content=True)
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    """Confirm when the bot is active."""
    print(f"{bot.user} is ready and online!")


## An example of a command where the bot just says something
@bot.slash_command(name="hello", description="Greet your robotic comrade")
async def hello(ctx):
    await ctx.respond(f"HELLO THERE {ctx.author.mention}! It is me, your robotic comrade ;)")


## An example of a command that takes arguments
@bot.slash_command(name="percent", description="Enter a fraction and get your percentage!")
async def get_percent(ctx, numerator: int, denominator: int):
    percent = f"{numerator/denominator:.1%}"
    await ctx.respond(f"As percent: {percent}")


## Example of actions triggered by somebody's message
@bot.event
async def on_message(message):
    # Don't do things triggered by the bot's own messages
    if message.author.bot:
        return
    
    # Send a message based on the content of a message
    if "pasta" in message.content.lower():
        await message.channel.send("Pasta? PASTAA???\n...I LOOOOOVE PASTA!!!")

    # React to a message based on the content
    if "cool" in message.content.lower():
        await message.add_reaction("😎")


# run the bot using your token
bot.run(_TOKEN)