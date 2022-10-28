#───────────────────────────────────────────────────────────────────────────────────────
# ╔╦╗┌─┐┌┐┌┌┬┐  ╔═╗┬┌─┬┌┬┐                                                                                   
#  ║║│ ││││ │   ╚═╗├┴┐│ ││                                                                                   
# ═╩╝└─┘┘└┘ ┴   ╚═╝┴ ┴┴─┴┘                                                                                   
#                  ╔═╗┌─┐┌┬┐┌─┐  ╔╦╗┬ ┬┬┌─┐                                                                 
#                  ║  │ │ ││├┤    ║ ├─┤│└─┐                                                                 
#                  ╚═╝└─┘─┴┘└─┘   ╩ ┴ ┴┴└─┘                                                                 
#                                  ╦┌┬┐┌─┐  ┌┬┐┌─┐  ┬  ┌─┐┌─┐┬─┐┌┐┌                                         
#                                  ║ │ └─┐   │ │ │  │  ├┤ ├─┤├┬┘│││                                         
#                                  ╩ ┴ └─┘   ┴ └─┘  ┴─┘└─┘┴ ┴┴└─┘└┘                                         
#                                                      ┌─┐┌─┐┌┬┐┌─┐┌┬┐┬ ┬┬┌┐┌┌─┐  ┌┬┐┬ ┬┌┬┐┌┐   ┌─┐┬ ┬┌─┐┬┌─
#                                                      └─┐│ ││││├┤  │ ├─┤│││││ ┬   │││ ││││├┴┐  ├┤ │ ││  ├┴┐
#                                                      └─┘└─┘┴ ┴└─┘ ┴ ┴ ┴┴┘└┘└─┘  ─┴┘└─┘┴ ┴└─┘  └  └─┘└─┘┴ ┴
#   Discord : pick#0628
#   
#   Github : https://github.com/8zj
#
#   Tiktok :  pick
#
#   My Server : https://discord.gg/v8GWsN5GjH
#
#  Again idk some commands i listed are not made by me idk who made them but i left whatever it had for credits so yea
#
#  i am Still learning python yay me 
#
#  this was made about 1-2 years ago from me when i was learning basic 
#
#  Don't remove my credits please and thank you <3
#
#───────────────────────────────────────────────────────────────────────────────────────



import discord,time,os,datetime,json,random
from discord.ext import commands
from os import system
from datetime import datetime
from discord.ext.commands.errors import MissingAnyRole, MissingPermissions, MissingRole #idk why discord for me makes me use this shit 

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

bot = commands.Bot(
	command_prefix = prefix, 
	intents = discord.Intents.all(),
	status=discord.Status.dnd
	)


@bot.event
async def on_rady():
	print(f"Working\nLogged In As : {bot.user}\nBot Id : {bot.id}")


@bot.command() # simple Way of Slowmode For Chats
@commands.has_permissions(administrator=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set The Slowmode Delay in This Channel To **{seconds}** seconds! **{ctx.author}** ")



@bot.command() #locks the channel you mention
@commands.has_permissions(administrator=True)
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(ctx.channel.mention + "Chat Is Now On Lockdown.")



@bot.command()
@commands.has_permissions(administrator=True)
@commands.has_permissions(manage_channels = True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + "Chat Is Now On Unlock.")

@bot.command()#This Will Spam A User With Alot Of This 
async def dm(ctx, user: discord.User): 
    for i in range(99999): #amout of times it sent 
        Crash = (" ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽  ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽  ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽  ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽  ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽")
        await user.send(Crash)


@bot.command() #should not have to explain this
async def ascii(ctx, *, text): 
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")



@bot.command(aliases=['pfp', 'avatar']) #simple way to steal someone pfp
async def av(ctx, *, user: discord.Member=None): #10
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.botSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))   



@bot.command(pass_content=True)#simple way to nickname someone from bot 
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'NickName Was Changed For {member.mention}')

@bot.command() #simple way to make bot get info about server
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

#───────────────────────────────────────────────────────────────────────────────────────
# ╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐                                
# ║  │ │││││││├─┤│││ ││└─┐                                
# ╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘└─┘                                
#                      ╔╗╔┌─┐┌┬┐                         
#                      ║║║│ │ │                          
#                      ╝╚╝└─┘ ┴                          
#                            ╔╦╗┌─┐┌┬┐┌─┐  ╔╗ ┬ ┬  ╔╦╗┌─┐
#                            ║║║├─┤ ││├┤   ╠╩╗└┬┘  ║║║├┤ 
#                            ╩ ╩┴ ┴─┴┘└─┘  ╚═╝ ┴   ╩ ╩└─┘
#
#───────────────────────────────────────────────────────────────────────────────────────


@bot.command()  
async def feed(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=f"{ctx.author.mention} Just Slaped : {user.mention}")
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def coinflip(ctx):
    choicse = ["Heads", "Talls"]
    rancoin = random.choice(choicse)
    await ctx.send(rancoin)

@bot.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@bot.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
@cooldown(1, 60, BucketType.user)
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")



@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + "You win Lets Go!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's A Tie Yall Dog Shit!")


                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn Fucking Dumb Ass.")
    else:
        await ctx.send("Please Start A New Game And Tpye .tictactoe @your self & @user")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


@bot.command()
async def dog(ctx): #2
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@bot.command() 
async def fox(ctx): #3
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image']) 
                                                                                   
#───────────────────────────────────────────────────────────────────────────────────────
#╔═╗┬┌┬┐┌─┐┬  ┌─┐                           
#╚═╗││││├─┘│  ├┤                            
#╚═╝┴┴ ┴┴  ┴─┘└─┘                           
#        ╔═╗┬─┐┬─┐┌─┐┬─┐                    
#        ║╣ ├┬┘├┬┘│ │├┬┘                    
#        ╚═╝┴└─┴└─└─┘┴└─                    
#              ╔╦╗┌─┐┌┐┌┌┬┐  ╔╦╗┌─┐┬ ┬┌─┐┬ ┬
#               ║║│ ││││ │    ║ │ ││ ││  ├─┤
#              ═╩╝└─┘┘└┘ ┴    ╩ └─┘└─┘└─┘┴ ┴
#    It's All Ready set why touch it dumb fuck
#───────────────────────────────────────────────────────────────────────────────────────
@lockdown.error
async def lockdown_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Please Ask A Admin To Unlock Channel {user} You Dont Have Perms...")
    elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")


@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"You Dont Have Commands To Run Command Please Speak To Admins/Owners{user}")


@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Please Ask A Admin {user} You Dont Have Perms...")
    elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")



@nick.error
async def nick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions, MissingAnyRole):
        await ctx.send(f"You Dont Have Perms To Use This Command Only Admins/Owners {user}")



#simple way to run bot from using config and not aways down here...
bot.run(token)