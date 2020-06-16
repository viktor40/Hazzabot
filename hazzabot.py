import discord
from discord.ext import commands
import time

TOKEN = ''
bot = commands.Bot(command_prefix='haz')

hazzabot_id = 694445660765945897
hazza_id = 466302344729198623
viktor_id = 234257395910443008
blanc_id = 676536088512299019


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            greeting = f'o/\n' \
                       f'hows the family?\n' \
                       f'dont forget to apply!'
            time.sleep(1)
            await channel.send(greeting)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.mention_everyone:
        if message.author.id == viktor_id:
            response = "Thank you for letting everyone know of your awesome existence"
        elif message.author.id == blanc_id:
            response = 'what the actual fuck have you done you fucking ape shit retard'
        else:
            response = 'Ping grrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr'
        await message.channel.send(response)

    if bot.get_user(hazza_id) in message.mentions:
        if message.author.id == viktor_id:
            response = "uwu ping me daddy"
        elif message.author.id == blanc_id:
            response = "leave me alone retard, stop pinging me"
        else:
            response = 'grrrrrrrrrrrrrrrrrrr'
        await message.channel.send(response)

    if bot.get_user(hazzabot_id) in message.mentions:
        response = 'grrr'
        await message.channel.send(response)

    bad_os = ('O', 'Ò', 'Ó', 'Ô', 'Ö', 'Ø', 'Ȯ', 'Õ', 'Ȍ', 'Ő', 'Ō', 'Ŏ', 'Ǒ', 'Ơ', 'Ǫ', 'Ǭ')
    for o in bad_os:
        if o + '/' or '\\' + o in message.content:
            response = 'remove that capital'
            await message.channel.send(response)

    if '0/' in message.content:
        if message.content.startswith('0/'):
            response = '^that\'s how many friends you have'
            await message.channel.send(response)
        else:
            response = 'stop using it wrong its o/ idiot'
            await message.channel.send(response)

    await bot.process_commands(message)


bot.add_cog(Greetings(bot))
bot.run(TOKEN)
