import discord
from discord.ext import commands

import os

client = commands.Bot(command_prefix= "pon!")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Pontes'))

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
        if message.content.startswith('pon!help'):
            embed=discord.Embed(title="Dit zijn mijn commando's", url="", color=0x3498db)
            embed.set_author(name="Pontes bot", icon_url="https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            embed.add_field(name="test", value="^^^^^^^^^^^^^^^^^^^^^^", inline=False)
            embed.set_footer(text="test",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.channel, embed=embed)

client.run(os.environ["BOT_TOKEN"])
