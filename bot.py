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
            embed.add_field(name="pon!klassen", value="om een lijst te krijgen van de klassen waar ik het rooster van kan laten zien", inline=False)
            embed.add_field(name="pon![je klas]", value="om het rooster van je klas te krijgen (als ik het heb).", inline=False)
            embed.add_field(name="pon!help", value="toon dit bericht!", inline=False)
            embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.channel, embed=embed)

        elif message.content.startswith('pon!klassen'):
              embed=discord.Embed(title="dit is de lijst met klassen waar ik het rooster van heb!", url="", color=0x3498db)
              embed.set_author(name="Pontes bot", icon_url="https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
              embed.add_field(name="H3RB", value="type 'pon!H3RB' voor het rooster van H3RB", inline=False)
              embed.add_field(name="pon!klassen", value="krijg een lijst van alle klassen", inline=False)
              embed.add_field(name="pon!help", value="krijg meer informatie over deze bot", inline=False)
              embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
              await client.send_message(message.channel, embed=embed)

client.run(os.environ["BOT_TOKEN"])
