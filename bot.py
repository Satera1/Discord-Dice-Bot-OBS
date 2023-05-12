import discord
import random
from discord.ext import commands
from obs_helper import create_dice_source
import json

import logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)


#Variables
intents = discord.Intents(messages=True, guilds=True, members=True)
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#Commands
#Dice rolling command
@bot.command(name='r', help='Simulates rolling dice. Uses d notation. ex: 3d6')
async def roll(ctx, roll):
    try:
        num_dice, num_sides = map(int, roll.split('d'))
        if num_dice < 1 or num_sides < 2:
            raise ValueError
    except ValueError:
        await ctx.send('Invalid roll. Must be in the format of NdM, where N is the number of dice and M is the number of sides on each die.')
        return

    r = 1
    dice_results = [random.randint(1, num_sides) for _ in range(num_dice)]
    results_string = ' , '.join(str(result) for result in dice_results)
    resultado = '@' + str(dice_results[0])
    for x in dice_results[1:]:
        resultado=resultado+'%2'+str(dice_results[r]).zfill(2)
        r=r+1
        total_sum = sum(dice_results)
    await ctx.send('🎲 '+results_string+' 🎲'f'\n_**(Total: {total_sum})**_')
    await create_dice_source(str(num_dice)+'d'+str(num_sides)+resultado) #Result

#Bot latency
@bot.command(name='pong', help='Returns the bot latency in miliseconds')
async def ping(ctx):
    print('Pong!')
    latency = round(bot.latency * 1000)
    await ctx.send(f'Ping! {latency}ms')

#Run bot
with open('config.json') as config:
    data = json.load(config)
    TOKEN = data['TOKEN']
bot.run(TOKEN)