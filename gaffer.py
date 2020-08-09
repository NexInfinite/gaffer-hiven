#Hiven Bot Named Gaffer

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
            ctx.send(f"The id of `{user.username}` is `{user.id}`")

    if ctx.author.id != bot.user.id:
        if message.content == "!hello":
            ctx.send(f"Hey! This is the gaffer bot. One day, I'll be on a bot account. Until then, this is me.")



bot.login()



bot.login()
