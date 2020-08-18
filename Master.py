import discord
import random
import asyncio
from random import randrange
from discord import utils
from discord.utils import get
from discord.ext import commands
from Cybernator import Paginator as pag
from secret import MyChannelID, RoleID, TOKEN

cat_url = 'https://cdn.discordapp.com/avatars/737244048196370482/7735697349fd235d7b52b84dfaa0ff35.webp?size=128'
client = commands.Bot(command_prefix = 'm.')
client.remove_command('help')

@client.event
async def on_ready():
	print('Master#5837 готов к обороне')

	await client.change_presence(status = discord.Status.dnd, activity = discord.Game('m.help'))

@client.event
async def on_member_join(member):
	channel = client.get_channel(MyChannelID)

	role = discord.utils.get(member.guild.roles, id = RoleID)
	await member.add_roles(role)
	embed=discord.Embed(title="Добро пожаловать, удачного времяпровождения!", color=0xfb0404)
	embed.set_author(name=f"{member.name} присоединился к нашему серверу!")
	embed.set_thumbnail(url=f"https://priscree.ru/img/746b01b8261c63.jpg")
	embed.add_field(name="Выдана роль", value=f"{role.mention}", inline=True)
	embed.set_footer(text="Новый участник")
	await channel.send(embed=embed)

#commands

@client.command()
@commands.has_guild_permissions(manage_messages = True)
async def clear(ctx, amount: int):
	await ctx.message.delete()
	await ctx.channel.purge(limit = amount)
	clir = await ctx.send(f'Удалено {amount} сообщений(е, я)')
	await asyncio.sleep(4)
	await clir.delete()

@client.command()
async def help(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Настоятельная рекомендация администраторам:", description="Пропишите команду `m.важно`!", color=0x1b27d0)
	embed.set_author(name="Master-бот", icon_url=cat_url)
	embed.set_thumbnail(url=cat_url)
	embed.add_field(name="🤖 Для администраторов", value="`m.kick`|`m.ban`|`m.unban`|`m.важно`", inline=True)
	embed.add_field(name="👨‍⚖️ Для модераторов", value="`m.clear`|`m.mute`|`m.unmute`|`m.tempmute`|`m.warn`", inline=False)
	embed.add_field(name="📝 Информация", value="`m.help`|`m.info`|`m.ping`|`m.uinfo`|`m.idea`", inline=False)
	embed.add_field(name="🥳 Фан-команды", value="`m.rate`", inline=False)
	embed.add_field(name="📼 Ссылки", value='''`Сервер бота (помощь, идеи и т.п.):` https://discord.gg/Jf3ZBYh
	`Пригласить бота на сервер:` https://discord.com/api/oauth2/authorize?client_id=737244048196370482&permissions=1343220807&scope=bot
	`Наш top.gg:` https://top.gg/bot/737244048196370482''', inline=False)
	embed.add_field(name="⛓️ Только для создателей", value="`m.hey`|`m.say`|`m.logout`", inline=False)
	embed.set_footer(text=f"Команда m.help | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
async def rate(ctx, member: discord.Member):
	await ctx.message.delete()
	embed=discord.Embed(title=f"{ctx.author.name}, хорошо, я оценю пользователя {member.name} 😉", color=0xf29a36)
	embed.add_field(name="☹️ Минимальная оценка:", value="0 баллов", inline=True)
	embed.add_field(name="🤖 Моя оценка:", value=f"{randrange(101)}", inline=False)
	embed.add_field(name="😃 Максимальная оценка:", value="100 баллов", inline=True)
	embed.set_footer(text=f"Команда m.rate | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = 'Отсутствует'):
	await ctx.message.delete()

	await member.kick(reason = reason)
	await member.send(f'''Ты был кикнут с сервера пользователем `{ctx.author.name}`
Причина: `{reason}`''')
	await ctx.send(f'{ctx.author.name}, пользователь `{member.name}` успешно кикнут! ')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = 'Отсутствует'):
	await ctx.message.delete()

	await member.ban(reason = reason)
	await member.send(f'''Ты был забанен пользователем `{ctx.author.name}`
Причина: `{reason}`''')
	await ctx.send(f'{ctx.author.name}, пользователь `{member.name}` успешно забанен!')

@client.command()
@commands.has_permissions(manage_messages = True)
async def warn(ctx, member: discord.Member, negativ: int = 1, *, reason: str = 'Отсутствует'):
	await ctx.message.delete()

	embed=discord.Embed(title="Выдано предупреждение!", description=f"Пользователь: {member.mention}", color=0xff0000)
	embed.set_thumbnail(url="https://static8.depositphotos.com/1431107/1066/i/450/depositphotos_10665820-stock-photo-warning-stamp.jpg")
	embed.add_field(name="Уровень негативности", value=f"{negativ}", inline=True)
	embed.add_field(name="Причина", value=f"{reason}", inline=True)
	embed.set_footer(text="Команда m.warn")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
	await ctx.message.delete()

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'{user.mention} успешно разбанен!')
		await user.send(f'Ты был разбанен пользователем `{ctx.author.name}`!')

		return

@client.command()
async def info(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Информация о боте Master", color=0xf2eb1c)
	embed.set_thumbnail(url=cat_url)
	embed.add_field(name="Основная", value='''Бот - `Master#5837`
Дата создания - `27.07.2020, 12:44:38`
Библиотека - `discord.py`
Python - `v3.8.5`
Версия бота - `v1.6.2`''', inline=True)
	embed.add_field(name="Системная", value='''CPU - `Intel(R) Core(TM)`
ОС - `Windows 10`''', inline=True)
	embed.add_field(name="Другое", value='Создатели: <@644260697194233856>, <@688333564617555998>, <@679388978989760596>', inline=False)
	embed.set_footer(text=f"Команда m.info | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def важно(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title=f"Рад что вы запросили эту команду, {ctx.author.name}!", description="Прочитайте пункты ниже", color=0x980cca)
	embed.add_field(name="Важная информация о командах!", value='''	1. Команда `m.mute` устроена по принципу выдачи роли, в связи с этим оповещаю то что обязательно нужно создать роль с именем `Muted` и выдать этой роли права соответствующие муту!
2. Команда `m.clear` удаляет сообщения частями, поэтому не советую указывать очень большое кол-во сообщений, которые нужно удалить, если вам это не нужно.
3. Команда `m.tempmute` работает также как `m.mute`, только перед причиной вам нужно указать время и оно должно быть в СЕКУНДАХ. Например: m.tempmute <@737244048196370482> 60 тест, это мут на 1 минуту по причине тест.''', inline=True)
	embed.set_footer(text=f"Команда m.важно | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_roles = True)
async def mute(ctx, member: discord.Member, *, reason = 'Отсутствует'):
	await ctx.message.delete()

	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')

	await member.add_roles(mute_role, reason = reason)
	embed=discord.Embed(title=f"Причина: `{reason}`", color=0xff0000)
	embed.set_author(name=f"Модератор {ctx.author.name} замутил пользователя {member.name}!")
	embed.set_thumbnail(url="https://images.discordapp.net/avatars/653176856035721270/371bdaa0d44478e76b23929559750651.png?size=512")
	embed.set_footer(text="Команда m.mute")
	await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
	await ctx.message.delete()
	embed=discord.Embed(title="Статистика по пингу:", description=f'''🏓 Пинг: `{randrange(248)}ms`
🏓 Задержка API: `{randrange(26)}ms`''', color=0x980cca)
	embed.set_footer(text=f"Команда m.ping | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member: discord.Member):
	await ctx.message.delete()

	unmute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')

	await member.remove_roles(unmute_role)
	await ctx.send(f'Модератор `{ctx.author.name}` размутил пользователя `{member.name}!`')

@client.command()
@commands.has_permissions(manage_roles = True)
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

@client.command()
async def uinfo(ctx, member: discord.Member):
	await ctx.message.delete()

	embed=discord.Embed(title=f'Информация об участнике {member.name}', description='Без упоминания узнаешь информацию о себе', color=0xb738af)
	embed.set_thumbnail(url=f"{member.avatar_url}")
	embed.add_field(name=f"Пользователь:", value=f"{member}")
	embed.add_field(name=f"ID:", value=f"{member.id}", inline=True)
	embed.add_field(name="Ник на сервере:", value=f"{member.nick}", inline=True)
	embed.add_field(name="Nitro", value=f"{member.premium_since}", inline=True)
	embed.add_field(name="Бот:", value=f"{member.bot}", inline=True)
	embed.add_field(name="Название сервера:", value=f"{member.guild}", inline=True)
	embed.add_field(name="Статус:", value=f"{member.status}", inline=True)
	embed.add_field(name='Создал аккаунт:', value=f'{member.created_at}', inline=True)
	embed.add_field(name='Зашёл на сервер:', value=f'{member.joined_at}', inline=True)
	embed.set_footer(text=f"Команда m.uinfo | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
async def idea(ctx, *, idea):
	await ctx.message.delete()

	idea_chnl = client.get_channel(739210194575425629)

	await idea_chnl.send(f'{idea}')
	await ctx.send(f'{ctx.author.name}, ваша идея отправлена на рассмотрение.')

@client.command()
@commands.is_owner()
async def sinfo(ctx, guild: discord.Guild):
	await ctx.message.delete()

	embed=discord.Embed(title="Владелец сервера:", description=f"{guild.owner}", color=0x386fb7)
	embed.set_author(name=f"Информация о сервере {guild.name}", icon_url=f"{guild.icon_url}")
	embed.set_thumbnail(url=f"{guild.icon_url}")
	embed.add_field(name='Дата создания:', value=f'{guild.created_at}', inline=True)
	embed.add_field(name='Специальные эмодзи:', value=f'{guild.emojis}', inline=True)
	embed.add_field(name='Регион сервера:', value=f'{guild.region}', inline=True)
	embed.add_field(name='Уровень проверки сервера:', value=f'{guild.verification_level}', inline=True)
	embed.add_field(name='Уровень буста сервера:', value=f'{guild.premium_tier}', inline=True)
	embed.add_field(name='Кол-во бустов сервера:', value=f'{guild.premium_subscription_count}', inline=True)
	embed.add_field(name='Категории:', value=f'{guild.categories}', inline=True)
	embed.add_field(name='Кол-во участников:', value=f'{guild.member_count}', inline=True)
	embed.add_field(name='Роли:', value=f'{guild.roles}', inline=True)
	embed.set_footer(text=f"Команда m.sinfo | запросил {ctx.author.name}")
	await ctx.send(embed=embed)

@client.command()
@commands.is_owner()
async def hey(ctx):
	await ctx.message.delete()

	message = await ctx.send("I'm Here!)")
	await asyncio.sleep(3)
	await message.edit(content="Yes, I'm here!)")

@client.command()
@commands.is_owner()
async def say(ctx, *, sayt):
	await ctx.message.delete()

	await ctx.send(f'{sayt}')

@client.command()
@commands.is_owner()
async def logout(ctx):
	await ctx.message.delete()

	await ctx.send('Пока-пока, я отключаюсь 👋')
	await client.logout()

#errors

# @client.event
# async def on_command_error(ctx, error):
# 	pass

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, У тебя нет прав для использования это команды.')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, похоже ты не указал сколько сообщений хочешь удалить!')

@важно.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, эта команда для администраторов, ты не можешь её использовать.')

@mute.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, у тебя нет прав для того чтобы мутить пользователей.')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, похоже ты не указал какого пользователя замутить!')

@kick.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, у тебя нет прав для того чтобы кикать пользователей.')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, похоже ты не указал какого пользователя кикнуть!')

@ban.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, у тебя нет прав для того чтобы банить пользователей.')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, похоже ты не указал какого пользователя забанить!')

@unban.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, у тебя нет прав для того чтобы разбанивать пользователей.')

	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		await ctx.send(f'{ctx.author.name}, похоже ты не указал какого пользователя разбанить!')

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

@uinfo.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()

		user = ctx.message.author

		embed=discord.Embed(title=f'Информация об участнике {ctx.author.name}', description='С упоминанием узнаешь информацию о другом участнике', color=0xb738af)
		embed.set_thumbnail(url=f"{user.avatar_url}")
		embed.add_field(name=f"Пользователь:", value=f"{user}")
		embed.add_field(name=f"ID участника:", value=f"{user.id}", inline=True)
		embed.add_field(name="Ник на сервере:", value=f"{user.nick}", inline=True)
		embed.add_field(name="Nitro", value=f"{user.premium_since}", inline=True)
		embed.add_field(name="Бот:", value=f"{user.bot}", inline=True)
		embed.add_field(name="Название сервера:", value=f"{user.guild}", inline=True)
		embed.add_field(name="Статус:", value=f"{user.status}", inline=True)
		embed.add_field(name='Создал аккаунт:', value=f'{user.created_at}', inline=True)
		embed.add_field(name='Зашёл на сервер:', value=f'{user.joined_at}', inline=True)
		embed.set_footer(text=f"Команда m.uinfo | запросил {ctx.author.name}")
		await ctx.send(embed=embed)

@warn.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, похоже ты не указал какому пользователю выдать предупреждение!')

	if isinstance(error, commands.BadArgument):
		await ctx.send(f'{ctx.author.name}, похоже ты что-то указал неправильно! Вот пример: m.warn <@737244048196370482> 11 тест')

	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, у тебя нет прав чтобы давать пользователям варны.')	

#Connect

client.run(TOKEN)