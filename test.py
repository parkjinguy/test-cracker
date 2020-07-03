import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(status=discord.Status.online)
@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("할말")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
