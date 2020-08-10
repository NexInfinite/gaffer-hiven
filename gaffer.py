#Hiven Bot Named Gaffer

import math
from Hiven.client import Bot, events

bot = Bot("074eN8vD36T0trTRooDpI0A3HH0ltxEuDq2iWuk4wd784mwb4jYJJZCqW44NHvx04peZr8ugJ59Ii19b48FidoILnV0jBvZ0SmyLDfIccyVFC391Fa4W8pebwoqcN8F0")


@events.event
def on_ready():
    print(f"Logged in as {bot.user.name}")


@events.event
def on_message(ctx):
    message = ctx.message
    if ctx.author.id != bot.user.id:
        if message.content == "!id":
            user = bot.get_user(ctx.author.username)
            ctx.send(f"Hey `{user.username}`, your ID is `{user.id}`")

        elif message.content == "!hello":
            ctx.send(f"Hey! This is the gaffer bot. One day, I'll be on a bot account. Until then, this is me.")

        elif message.content == "!giggl":
            ctx.send(f"Giggl (https://giggl.app/) is a really neat service you should sign up for ;)")

        elif message.content == "!giggl":
            ctx.send(f"Giggl (https://giggl.app/) is a really neat service you should sign up for ;)")

        elif message.content == "!hiven":
            ctx.send(f"Bro")

        elif message.content == "!ping":
            ctx.send(f"Pong! + `{math.floor(bot.ping())}`")

        elif message.content == "!pog":
            ctx.send(f"pog")

        elif message.content == "!help":
            ctx.send(f"I don't have many commands at the moment, but I'm getting there. Here's what I can currently do: \n `!id` - I'll reply with your Hiven user ID \n `!hello` - I'll beg for someone to host me on a bot account.\n `!giggl` - I'll talk about how cool Giggl is\n `!ping` - Pong \n `!pog` - pog \n That's all for now, check back soon for more! Thanks to the creators of Hivenpy for making me possible!")



bot.login()
