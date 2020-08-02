import discord
import random
import asyncio
from random import randrange
from discord import utils
from discord.utils import get
from discord.ext import commands

cat_url = 'https://cdn.discordapp.com/avatars/737244048196370482/7735697349fd235d7b52b84dfaa0ff35.webp?size=128'
client = commands.Bot(command_prefix = 'm.')
client.remove_command('help')

@client.event
async def on_ready():
	print('Master#5837 готов к обороне')

	await client.change_presence(status = discord.Status.online, activity = discord.Game('m.help'))

@client.event
async def on_member_join(member):
	channel = client.get_channel(MyChannelID)

	role = discord.utils.get(member.guild.roles, id = RoleID)
	await member.add_roles(role)
	embed=discord.Embed(title="Добро пожаловать, удачного времяпровождения!", color=0xfb0404)
	embed.set_author(name=f"{member.name} присоединился к нашему серверу!")
	embed.set_thumbnail(url=f"https://priscree.ru/img/746b01b8261c63.jpg")
	embed.add_field(name="Выдана роль", value=f"{role}", inline=True)
	embed.set_footer(text="Новый участник")
	await channel.send(embed=embed)

#commands

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount: int):
	await ctx.message.delete()
	await ctx.channel.purge(limit = amount)
	# await ctx.send(f'Удалено {amount} сообщений')

@client.command(pass_context = True)
async def help(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Настоятельная рекомендация администраторам:", description="Пропишите команду `m.важно`!", color=0x1b27d0)
	embed.set_author(name="Master-бот", icon_url=cat_url)
	embed.set_thumbnail(url=cat_url)
	embed.add_field(name="🤖 Для администраторов", value="`m.kick`, `m.ban`, `m.unban`, `m.важно`", inline=True)
	embed.add_field(name="👨‍⚖️ Для модераторов", value="`m.clear`, `m.mute`, `m.unmute`, `m.tempmute`", inline=False)
	embed.add_field(name="😀 Базовые команды", value="`m.help`, `m.info`, `m.ping`", inline=False)
	embed.add_field(name="🥳 Фан-команды", value="`m.rate`", inline=False)
	embed.add_field(name="📼 Ссылки", value='''`Сервер бота (помощь, идеи и т.п.):` https://discord.gg/Jf3ZBYh
	`Пригласить бота на сервер:` https://discord.com/api/oauth2/authorize?client_id=737244048196370482&permissions=2147483647&scope=bot''', inline=False)
	embed.set_footer(text=f"Команда m.help | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(pass_context = True)
async def rate(ctx, member: discord.Member):
	await ctx.message.delete()
	embed=discord.Embed(title=f"{ctx.author.name}, хорошо, я оценю пользователя {member.name} 😉", color=0xf29a36)
	embed.add_field(name="☹️ Минимальная оценка:", value="0 баллов", inline=True)
	embed.add_field(name="🤖 Моя оценка:", value=f"{randrange(101)}", inline=False)
	embed.add_field(name="😃 Максимальная оценка:", value="100 баллов", inline=True)
	embed.set_footer(text=f"Команда m.rate | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member, *, reason = 'Остутствует'):
	await ctx.message.delete()

	await member.kick(reason = reason)
	await member.send(f'''Ты был кикнут с сервера пользователем `{ctx.author.name}`
Причина: `{reason}`''')
	await ctx.send(f'{ctx.author.name}, пользователь `{member.name}` успешно кикнут! ')

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ban(ctx, member: discord.Member, *, reason = 'Остутствует'):
	await ctx.message.delete()

	await member.ban(reason = reason)
	await member.send(f'''Ты был забанен пользователем `{ctx.author.name}`
Причина: `{reason}`''')
	await ctx.send(f'{ctx.author.name}, пользователь `{member.name}` успешно забанен!')

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
	await ctx.message.delete()

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'{user.mention} успешно разбанен!')
		await user.send(f'Ты был разбанен пользователем `{ctx.author.name}`!')

		return

@client.command(pass_context = True)
async def info(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Информация о боте Master", color=0xf2eb1c)
	embed.set_thumbnail(url=cat_url)
	embed.add_field(name="Основная", value='''Бот - `Master#5837`
Дата создания - `27.07.2020, 12:44:38`
Библиотека - `discord.py`
Python - `v3.8.5`
Версия бота - `v2.1.5`''', inline=True)
	embed.add_field(name="Системная", value='ОС - `Windows 10`', inline=True)
	embed.add_field(name="Другое", value='Создатели: <@644260697194233856>, <@688333564617555998>, <@679388978989760596>', inline=False)
	embed.set_footer(text=f"Команда m.info | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def важно(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title=f"Рад что вы запросили эту команду, {ctx.author.name}!", description="Прочитайте пункты ниже", color=0x980cca)
	embed.add_field(name="Важная информация о командах!", value='''	1. Команда `m.mute` устроена по принципу выдачи роли, в связи с этим оповещаю то что обязательно нужно создать роль с именем `Muted` и выдать этой роли права соответствующие муту!
2. Команда `m.clear` удаляет сообщения частями, поэтому не советую указывать очень большое кол-во сообщений, которые нужно удалить, если вам это не нужно.
3. Команда `m.tempmute` работает также как `m.mute`, только перед причиной вам нужно указать время и оно должно быть в СЕКУНДАХ. Например: m.tempmute <@737244048196370482> 60 тест, это мут на 1 минуту по причине тест.''', inline=True)
	embed.set_footer(text=f"Команда m.важно | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member, *, reason = 'Отсутствует'):
	await ctx.message.delete()

	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')

	await member.add_roles(mute_role, reason = reason)
	embed=discord.Embed(title=f"Причина: `{reason}`", color=0xfb0404)
	embed.set_author(name=f"Модератор {ctx.author.name} замутил пользователя {member.name}!")
	embed.set_thumbnail(url="https://images.discordapp.net/avatars/653176856035721270/371bdaa0d44478e76b23929559750651.png?size=512")
	embed.set_footer(text="Команда m.mute")
	await ctx.send(embed=embed)

@client.command(pass_context = True)
async def ping(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Статистика по пингу:", description=f'''🏓 Пинг: `{randrange(248)}ms`
🏓 Задержка API: `{randrange()}ms`''', color=0x980cca)
	embed.set_footer(text=f"Команда m.ping | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def unmute(ctx, member: discord.Member):
	await ctx.message.delete()

	unmute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')

	await member.remove_roles(unmute_role)
	await ctx.send(f'Модератор `{ctx.author.name}` размутил пользователя `{member.name}!`')

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def tempmute(ctx, member: discord.Member, amount: int, *, reason = 'Отсутствует'):
	await ctx.message.delete()

	tempmute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')

	await member.add_roles(tempmute_role)
	embed=discord.Embed(title=f"Причина: `{reason}`", color=0xfb0404)
	embed.set_author(name=f"Модератор {ctx.author.name} замутил пользователя {member.name} на {amount} секунд!")
	embed.set_thumbnail(url="https://images.discordapp.net/avatars/653176856035721270/371bdaa0d44478e76b23929559750651.png?size=512")
	embed.set_footer(text="Команда m.tempmute")
	await ctx.send(embed=embed)

	await asyncio.sleep(amount)
	await member.remove_roles(tempmute_role)


@client.command(pass_context = True)
@commands.is_owner()
async def банан(ctx, member: discord.Member, *, reason = 'Остутствует'):
	await ctx.message.delete()

	await member.ban(reason = reason)
	await member.send(f'''Ты был забанен пользователем `{ctx.author.name}`
Причина: `{reason}`''')
	await ctx.send(f'{ctx.author.name}, пользователь `{member.name}` успешно забанен!')

@client.command(pass_context = True)
@commands.is_owner()
async def разбанан(ctx, *, member):
	await ctx.message.delete()

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'{user.mention} успешно разбанен!')
		await user.send(f'Ты был разбанен пользователем `{ctx.author.name}`!')

		return

@client.command(pass_context = True)
@commands.is_owner()
async def пинок(ctx, member: discord.Member, *, reason = 'Остутствует'):
	await ctx.message.delete()

	await member.kick(reason = reason)
	await member.send(f'''Ты был кикнут с сервера пользователем `{ctx.author.name}`
Причина: `{reason}`''')
	await ctx.send(f'{ctx.author.name}, пользователь `{member.name}` успешно кикнут! ')

#errors

@client.event
async def on_command_error(ctx, error):
	pass

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, прав нету, куда полез?')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, ты не указал сколько сообщений хочешь удалить!')

@важно.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, прав нету, куда полез?')

@mute.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, прав нету, куда полез?')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, ты не указал какого пользователя замутить!')

@kick.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, прав нету, куда полез?')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, ты не указал какого пользователя кикнуть!')

@ban.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, прав нету, куда полез?')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, ты не указал какого пользователя забанить!')

@unban.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, прав нету, куда полез?')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, ты не указал какого пользователя разбанить!')

@rate.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		embed=discord.Embed(title=f"Хорошо, я оценю тебя, {ctx.author.name} 😉", color=0xf29a36)
		embed.add_field(name="☹️ Минимальная оценка:", value="0 баллов", inline=True)
		embed.add_field(name="🤖 Моя оценка:", value=f"{randrange(101)} баллов", inline=False)
		embed.add_field(name="😃 Максимальная оценка:", value="100 баллов", inline=True)
		embed.set_footer(text="Команда m.оценка")
		await ctx.send(embed=embed)

#Connect

client.run(TOKEN)