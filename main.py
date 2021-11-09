import discord
from discord.ext import commands, tasks
import music
from itertools import cycle
import fun
from random import choice

prefixValue = '-'
status = ['forg drip', 'best bot']
@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
cogs = [music, fun]
client = commands.Bot(command_prefix=prefixValue, intents = discord.Intents.all())
client.remove_command('help')
@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')
    print('Welcome to happyForg Bot!!!')
@client.command()
async def prefix(self, ctx):
    await ctx.send("prefix je" + prefixValue + "ty skurveny hnusak")
@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
      title = 'Help',
      colour = discord.Colour.purple()
    )
    embed.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='General', value='`introduce`, `ping`, `floppa`, `clear`', inline=False)
    embed.add_field(name='Music', value='`join`, `disconnect`, `play`', inline=False)
 
    await ctx.send('help for you! :3', embed=embed)

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run('import token here :3')