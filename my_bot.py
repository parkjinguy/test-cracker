
# discord 라이브러리 사용 선언
import discord
import os
import random

tmp=[]
tmpt=[]
chek=[]
result1=[]
result2=[]
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
        if message.content == "!바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "너도 바보"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None;
        if message.content == "!안녕":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "연습중인 스뜐기입니다."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
            # 답변 내용 구성
        if message.content == "!창규":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "하이"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        #메시지 해당 사람 태그 호출
        if message.content == "과자":
            channel = message.channel;
            msg = "<@{}>".format("#9522")
            await channel.send(msg)
            await channel.send("호출")
            return None
        if message.content == "!도움말":
            if message.author.dm_channel:
                await message.author.dm_channel.send("명령어:!아잇,과자,!냥이,!안녕,!팀설정,!팀결과")
                await message.author.dm_channel.send("!팀설정은 !팀설정 인원1 인원2 인원3로 설정을 하며 무조건 짝수만 가능합니다(설정하면 자동으로 팀을 나눕니다) ")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()#dm채널 없으면 추가후 전송
                await channel.send("명령어:!아잇,과자,!냥이,!안녕,!팀설정,!팀결과")
                await channel.send("!팀설정은 !팀설정 인원1 인원2 인원3로 설정을 하며 무조건 짝수만 가능합니다(설정하면 자동으로 팀을 나눕니다)")
            return None
        if message.content == "!패치로그":
            if message.author.dm_channel:
                await message.author.dm_channel.send("2020-07-03 스뜐끼봇이 추가되었습니다.")
                await message.author.dm_channel.send("2020-07-04 자동 팀설정이 추가되었습니다")
                await message.author.dm_channel.send("2020-07-04 스뜐끼 답변 기능이 제거되었습니다.")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()#dm채널 없으면 추가후 전송
                await channel.send("2020-07-03 스뜐끼봇이 추가되었습니다.")
                await channel.send("2020-07-04 자동 팀설정이 추가되었습니다")
                await channel.send("2020-07-04 스뜐끼 답변 기능이 제거되었습니다.")
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
        #사진 
        if message.content == "!아잇":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"11.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!냥이":
            channel = message.channel;
            await channel.send("언제와!!!")
            return None
        global ii
        global count
        if "!사다리 " in message.content:
            count=0
            ii=0
            channel = message.channel
            arr_str = str(message.content).split(" ")
            if len(arr_str)%2 == 1:
                await channel.send("!결과를 입력하여 결과를 확인하세요")
            else:
                await channel.send("홀수 입니다 한명을 추가하세요")
                ii=1
                return None
            for i in arr_str:
                tmp.append(i)
                count=count+1
            return None
        if message.content == "!결과":
            channel = message.channel
            if ii == 0:
                while len(chek) != len(tmp)-1:
                    print(count)
                    if count == 0:
                        await channel.send("!팀설정을 해주세요")
                        return None
                    couna = random.randrange(1,count)
                    if couna not in chek:
                        chek.append(couna)
                        print(couna)
                for a in chek:
                    tmpt.append(tmp[a])
                tmm=count//2
                print(tmm)
                for c in range(0,tmm):
                    result1.append(tmpt[c])
                for s in range(tmm,tmm+tmm):
                    result2.append(tmpt[s])
                shw1=""
                shw2=""
                for a1 in result1:
                    shw1=shw1+" "+a1
                for a2 in result2:
                    shw2=shw2+" "+a2
                await channel.send(shw1)
                await channel.send(shw2)
            else:
                await channel.send("한명을 추가해서 다시 해주세요")
            tmp.clear()
            tmpt.clear()
            chek.clear()
            result1.clear()
            result2.clear()
            count=0
            return None
    
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    access_token = os.environ["BOT_TOKEN"]
    client.run(access_token)
