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
            embed.add_field(name="type 'pon!klassen' om een lijst te krijgen van de klassen waar ik het rooster van kan laten zien")
            embed.add_field(name="type 'pon![je klas]' om het rooster van je klas te krijgen (als ik het heb).")
            embed.add_field(name="type 'pon!help' om dit bericht te tonen!", value="^^^^^^^^^^^^^^^^^^^^^^", inline=False)
            embed.set_footer(text="test",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            embed.set_footer(text="Pontes bot © 2018 | all rights reserved",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.channel, embed=embed)

        elif message.content.startswith('pon!klassen'):
              embed=discord.Embed(title="dit is de lijst met klassen waar ik het rooster van heb!", url="", color=0x3498db)
              embed.set_author(name="Pontes bot", icon_url="https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
              embed.add_field(name="H3RB", value="test", url="https://google.com", inline=False)
              embed.set_footer(text="Pontes bot © 2018 | all rights reserved",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
              await client.send_message(message.channel, embed=embed)

client.run(os.environ["BOT_TOKEN"])
