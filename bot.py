import discord
import asyncio
import random
import openpyxl
import datetime
import os


client = discord.Client()





@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('헵자야 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):



    if message.content.startswith('헵자야 도움말'):
      embed = discord.Embed(title="명령어", description="", color=0xAAFFFF)
      embed.add_field(name="헵자야 안녕", value="헵자가 인사를 해줘요", inline=False)
      embed.add_field(name="헵자야 유튜브", value="헵자가 유튜브 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 트위치", value="헵자가 트위치 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 트위터", value="헵자가 트위터 링크를 알려줘요", inline=False)
      embed.add_field(name="헵자야 인스타", value="헵자가 인스타 링크를 알려줘요", inline=False)
      embed.set_footer(text="!SOBI#1919")
      embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/543747267794829331/b5a1e2cd0bb4a1ce24417e4049782ebc.png?size=128")
      await message.channel.send(embed=embed)


    if message.content.startswith('헵자야 생년월일'):
      embed = discord.Embed(title="HEAVYgiant", description="HEAVYgiant#0217", color=0xAAFFFF)
      embed.add_field(name="2005년", value="2월 17일", inline=False)
      embed.set_footer(text="!SOBI#1919")
      embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/543747267794829331/b5a1e2cd0bb4a1ce24417e4049782ebc.png?size=128")
      await message.channel.send(embed=embed)


    if message.content == "헵자야 내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}님의 정보 : {user} / 디스코드 가입일: {date.year}/{date.month}/{date.day} / 프로필 사진: {user.avatar_url}")


    if message.content.startswith('헵자야 시계'):
      await message.channel.send(embed=discord.Embed(title="헵자 시계", timestamp=datetime.datetime.utcnow()))



    if message.content.startswith('헵자야 파이썬'):
      await message.channel.send("""
```py
print("헵자봇 제작자 멍청이임")
```
""")









    if message.content.startswith('헵자야 유튜브'):
      await message.channel.send('https://www.youtube.com/channel/UCFcFcyR8VmVg43RdGTiN3kQ')

    if message.content.startswith('헵자야 트위치'):
      await message.channel.send('https://www.twitch.tv/heavygiant217')

    if message.content.startswith('헵자야 트위터'):
      await message.channel.send('https://twitter.com/heavygiant217')

    if message.content.startswith('헵자야 디코'):
      await message.channel.send('https://discord.gg/gUTAY9Cqbc')

    if message.content.startswith('헵자야 인스타'):
      await message.channel.send('https://instagram.com/heavygiant?igshid=1ewywjzmyfdwy')


    if message.content.startswith('헵자야 안녕'):
      await message.channel.send('ㅎㅇㅎㅇ')

    if message.content.startswith('헵자야 바보'):
      await message.channel.send('힝')

    if message.content.startswith('헵자야 송강욱 고인물'):
      await message.channel.send('?')

    if message.content.startswith('헵자야 마인크래프트'):
      await message.channel.send('갓똥겜')

    if message.content.startswith('헵자야 멍청이'):
      await message.channel.send('힝 나빠써 ㅠㅜ')

    if message.content.startswith('헵자야 힝'):
      await message.channel.send('히ㅇ이이이이이이이이이이이이잉ㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠㅜㅠ')

    if message.content.startswith('헵자야 귀여워'):
      await message.channel.send('뀨?')

    if message.content.startswith('헵자야 애교'):
      await message.channel.send('아잉아잉아잉아잉 이이이잉 잉 이 잉!!!!!!!!!')

    if message.content.startswith('헵자야 뀨'):
      await message.channel.send('뀨!! 뀨!!')

    if message.content.startswith('헵자야 헵자'):
      await message.channel.send('머요')

    if message.content.startswith('헵자야 멍뭉'):
      await message.channel.send('멍뭉!💕 멍뭉!💕')

    if message.content.startswith('헵자야 사랑해'):
      await message.channel.send('나듀 사량해 💕💕')

    if message.content.startswith('헵자야 나이'):
      await message.channel.send('17')

    if message.content.startswith('헵자야 생일'):
      await message.channel.send('2월 17일')

    if message.content.startswith('헵자야 냥'):
      await message.channel.send('냥!')

    if message.content.startswith('헵자야 멍멍'):
      await message.channel.send('멍❤')

    if message.content.startswith('헵자야 솝이'):
      await message.channel.send('멍청한 개발자')

    if message.content.startswith('헵자야 소비'):
      await message.channel.send('멍청한 개발자')

    if message.content.startswith('헵자야 소비를 어떻게 생각해'):
      await message.channel.send('소비바부')

    if message.content.startswith('헵자야 ㅡㅡ'):
      await message.channel.send('ㅡㅡ')

    if message.content.startswith('헵자야 ㄷㄷ'):
      await message.channel.send('ㅎㄷㄷ')






acces_token = os.environ["BOT_TOKEN"]
client.run(access_token)
