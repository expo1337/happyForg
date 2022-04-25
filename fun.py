import discord
from discord.ext import commands, tasks
import youtube_dl
from itertools import cycle
import os
import random

class fun(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
    await ctx.send("pong!")
  @commands.command()
  async def introduce(self, ctx):
    await ctx.send("Hi! I'm a mentally retarded python bot, get more command info with *help | coded by @exp0#0001 <3")
  @commands.command()
  async def floppa(self, ctx):
        responses = [
        'https://cdn.discordapp.com/attachments/834520706410217522/834522304431259669/Floppa.jpg',
        'https://media.discordapp.net/attachments/834520706410217522/834522307913318418/Floppa1.jpg',
        'https://media.discordapp.net/attachments/834520706410217522/834522308794253383/Floppa2.jpg',
        'https://media.discordapp.net/attachments/834520706410217522/834522311767228446/Floppa3.jpg',
        'https://media.discordapp.net/attachments/834520706410217522/834522315814862928/Floppa4.jpg',
        'https://cdn.discordapp.com/attachments/834520706410217522/885119091172597810/floppa5.jpg',
        'https://media.discordapp.net/attachments/834520706410217522/885119103986200596/floppa6.jpg',
        'https://media.discordapp.net/attachments/834520706410217522/885119115105288212/floppa7.jpg']
        await ctx.send(random.choice(responses))
  @commands.command()
  async def forg(self, ctx):
    responses = [
        'https://cdn.discordapp.com/attachments/834520706410217522/907301200590958632/frog.png',
        'https://cdn.discordapp.com/attachments/834520706410217522/907301200863567942/frog1.png',
        'https://cdn.discordapp.com/attachments/834520706410217522/907301496750760027/frog2.png',
        'https://cdn.discordapp.com/attachments/834520706410217522/907301201152983051/frog3.png',
        'https://cdn.discordapp.com/attachments/834520706410217522/907301201358512188/frog4.png',
        'https://cdn.discordapp.com/attachments/834520706410217522/907301201664700416/frog5.png',
        'https://cdn.discordapp.com/attachments/592360331502944256/907364763481280562/DmTvwUvWwAAg0cs.jpg',
        'https://cdn.discordapp.com/attachments/592360331502944256/907364917630337024/avatars-c9S1Vh7Ac4ds4qsM-JzY45w-t500x500.jpg']
    await ctx.send(random.choice(responses))
def setup(client):
  client.add_cog(fun(client))    
