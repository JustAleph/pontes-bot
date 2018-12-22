import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import time

import os

client = commands.Bot(command_prefix= "pon!")
client.remove_command('help')

chat_filter = ["PON!KLASSEN", "PON!HELP",]
bypass_list = []

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
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/393852367751086090.gif?v=1")
            embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
            sent = await client.send_message(message.channel, "Ik heb je een DM gestuurd!")
            await asyncio.sleep(6)
            await client.delete_message(sent)
 
        elif message.content.startswith('pon!klassen'):
            embed=discord.Embed(title="dit is de lijst met klassen waar ik het rooster van heb!", url="", color=0x3498db)
            embed.set_author(name="Pontes bot", icon_url="https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            embed.add_field(name="H3RB", value="type 'pon!H3RB' voor het rooster van H3RB", inline=False)
            embed.add_field(name="pon!klassen", value="krijg een lijst van alle klassen", inline=False)
            embed.add_field(name="pon!help", value="krijg meer informatie over deze bot", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/393852367751086090.gif?v=1")
            embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
            sent = await client.send_message(message.channel, "Ik heb je een DM gestuurd!")
            await asyncio.sleep(6)
            await client.delete_message(sent)

        elif message.content.startswith('pon!H3RB'):
            embed=discord.Embed(title="Klik hier voor het rooster van H3RB", url="https://cdn.discordapp.com/attachments/524321408587661334/525685520043343882/Schermafbeelding_2018-12-21_om_15.05.00.png", color=0x3498db)
            embed.set_author(name="Pontes bot", icon_url="https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            embed.add_field(name="pon!klassen", value="krijg een lijst van alle klassen", inline=False)
            embed.add_field(name="pon!help", value="krijg meer informatie over deze bot", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/393852367751086090.gif?v=1")
            embed.set_footer(text="Pontes bot © 2018 | gemaakt door @JustAleph0001",icon_url= "https://cdn.discordapp.com/avatars/231703783988527104/7012bfe50b480374b601dae2576a521c.png?size=128")
            sent = await client.send_message(message.author, embed=embed)
            await client.delete_message(message)
            sent = await client.send_message(message.channel, "Ik heb je een DM gestuurd!")
            await asyncio.sleep(6)
            await client.delete_message(sent)

client.run(os.environ["BOT_TOKEN"])
