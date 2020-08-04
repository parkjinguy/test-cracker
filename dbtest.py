import discord
import os
import random
#from urllib import parse
import requests
import json
import time
import pymysql
class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("!도움말")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")
    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):    
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        # message.content = message의 내용
        if message.content == "!도움말":
            aa="명령어 :  !아잇, !냥이, !안녕, !팀설정, !팀결과, !찌릿, !잠, !일해, !레드, !크래커, !냥, !창규, !냥대노, !죄송\n"
            aa= aa+" !냥이월급날, !보리, !리브, !햄울찜, 기분좋아, !초코, !여긴 따뜻해, !도라이, !나루토는 전설이다, !투표, !투표결과, !찬성,\n"
            aa= aa+" !반대, !투표종료, !요염, !뭘 꼬라봐, !사륜안, !경이, !롤., !하 인생, !돌맹, !잘한다, !냥청, !글적, !짱깨, !글적\n"
            aa= aa+" !참가, !참가결과, !참가취소, !인성, 흐뭇, 모름, 사딸라, 다이어트, 할짝  시무룩\n"
            aa= aa+"!팀설정은 !팀설정 인원1 인원2 인원3로 설정을 하며 무조건 짝수만 가능합니다(설정하면 자동으로 팀을 나눕니다.) \n"
            aa= aa+"!투표설정은 !투표 투표내용 하면 투표가 시작되며 !찬성, !반대로 투표를 하며 !투표결과로 결과를 확인합니다 그리고 !투표종료를 하면 중지를 합니다.\n "
            aa= aa+"!롤.은 .뒤에 롤닉네임을 그대로 적어주시면 잠시뒤에 자동으로 출력이됩니다.\n"
            aa= aa+"참가 여부는 !참가만 입력하면 자동 참가되고 최소는 !참가취소 결과보기는 !참가결과 이며 결과는 한번만 출력됩니다.\n"
            if message.author.dm_channel:
                await message.author.dm_channel.send(aa)
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()#dm채널 없으면 추가후 전송
                await channel.send(aa)
            return None
        #욕 필터
        #mess = message.content
        #tmp = ["씨발","ㅅㅂ","시발","병신","좆까","니얼굴","니 얼굴"]
        #for i in tmp:
            #bad = mess.find(i)
            #print(bad)
            #if bad == 0:
                #await message.channel.send("욕하지 마세요")
                #await message.delete() 현재 관리자로 인해 비활성화
        if "!인성" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a21.jpg")
            await message.channel.send(file=file)
            return None
        if "on" in message.content:
            conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
 
                # Connection 으로부터 Cursor 생성
            curs = conn.cursor()
            #sql = "create table cat1(num int(2), name varchar(30))"
            #sql = "insert into cat1 values(1,'test')"
            #sql = "select * from cat1"
            sql = "delete from cat1"
            curs.execute(sql)
            conn.commit() #insert
            #rows = curs.fetchall()
            #print(rows)
            conn.close()
            return
        if "!마피아 시작" in message.content:
            server = message.server
            voice_client = client.voice_client_in(server)
            return
            
    
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    access_token="NzM3MjYyNDIyOTI2Mjk1MTcx.Xx6zIw.I8Ihn3DqNx5uVI00aqHqO3qDAA4"
    client.run(access_token)
