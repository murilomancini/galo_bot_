import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands
from discord import FFmpegPCMAudio 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

FFMPEG_PATH = '/home/runner/galobot-1/node_modules/ffmpeg-static/ffmpeg'

bot = commands.Bot(command_prefix="ç", intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    discord.opus.load_opus("./libopus.so.0.8.0")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = member.voice.channel
        voice = member.guild.voice_client
        if member.guild.voice_client not in  bot.voice_clients:
            voice = await channel.connect()
            source = FFmpegPCMAudio('boris_boanoite.mp3', executable=FFMPEG_PATH)
            player = voice.play(source)
        else:
            voice = member.guild.voice_client
            source = FFmpegPCMAudio('boris_boanoite.mp3', executable=FFMPEG_PATH)
            player = voice.play(source)


@bot.command(pass_context=True)
async def ifan(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('ifan_aro_aro_aro.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('ifan_aro_aro_aro.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('') 

@bot.command(pass_context=True)
async def galo(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('galo_6f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('galo_6f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def galo1(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('galo_7f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('galo_7f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def galo2(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('galo_8f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('galo_8f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def galo3(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('galo_9f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('galo_9f.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def groselha(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('groselha.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('groselha.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def vovo(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('vovoGrito.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('vovoGrito.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def vovoyudi(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('YudiEscroto.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('YudiEscroto.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def silvio(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('SilvioSantosEro.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('SilvioSantosEro.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
        
@bot.command(pass_context=True)
async def tony(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('tony.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('tony.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def bl(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('blblblblblbl.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('blblblblblbl.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def mamou(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('mamou_muito_Trim.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('mamou_muito_Trim.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        

@bot.command(pass_context=True)
async def autismo(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('intro-autismo-lol (1).mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('intro-autismo-lol (1).mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')
        
@bot.command(pass_context=True)
async def autismo1(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('mano_-bibi-lindo-velho (1).mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('mano_-bibi-lindo-velho (1).mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')   

@bot.command(pass_context=True)
async def jea_pequenininho(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('jea_pequenininho.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('jea_pequenininho.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')   
        
@bot.command(pass_context=True)
async def jp(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('jp.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('jp.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')   

@bot.command(pass_context=True)
async def cachorro_primonha(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('cachorro_primonha.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('cachorro_primonha.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')   
        
@bot.command(pass_context=True)
async def ziper(ctx):
    if(ctx.voice_client):
        voice = ctx.voice_client
        source = FFmpegPCMAudio('ziper.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('ziper.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')   
        
@bot.command(pass_context=True)
async def sucrilhos_galo(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('sucrilhos_galo.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('sucrilhos_galo.mp4', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')    
        
@bot.command(pass_context=True)
async def lasier(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('September_lasier.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('September_lasier.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')    
        
@bot.command(pass_context=True)
async def gordo(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('Gordo.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Gordo.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')    
        
@bot.command(pass_context=True)
async def seucu(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('enfia_no_seu_cu_haha.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('enfia_no_seu_cu_haha.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')    
        
        
@bot.command(pass_context=True)
async def perder(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('se_agente_perder_a_gente_perde.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('se_agente_perder_a_gente_perde.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')    
        
@bot.command(pass_context=True)
async def boris(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('boris_boanoite.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('boris_boanoite.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')    

@bot.command(pass_context=True)
async def sentalhe(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('sentalhe_a_pica_nela.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('sentalhe_a_pica_nela.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')

@bot.command(pass_context=True)
async def nenem(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('jeh_nenemzin.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('jeh_nenemzin.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')

@bot.command(pass_context=True)
async def tome(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('tome_audio_meme.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('tome_audio_meme.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')

@bot.command(pass_context=True)
async def corte(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('CORTE_RAPIDO_-_TRAMONTINA.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('CORTE_RAPIDO_-_TRAMONTINA.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')

@bot.command(pass_context=True)
async def cazabe(ctx):
    if(ctx.voice_client):

        voice = ctx.voice_client
        source = FFmpegPCMAudio('Risada_do_Carlos_Alberto_de_Nobrega.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    elif(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Risada_do_Carlos_Alberto_de_Nobrega.mp3', executable=FFMPEG_PATH)
        player = voice.play(source)
    else:
        await ctx.send('')

server.server()
bot.run(TOKEN)
