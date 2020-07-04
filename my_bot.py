
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
                await message.author.dm_channel.send("명령어\n!아잇\n과자\n!냥이\n!안녕\n스뜐끼\n나머지는 추가예정")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()#dm채널 없으면 추가후 전송
                await channel.send("명령어\n!아잇\n과자\n!냥이\n!안녕\n스뜐끼\n나머지는 추가예정")
            return None
        if "스뜐끼" in message.content:
            channel = message.channel
            await channel.send("스뜐끼!!!!")
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
        if message.content == "!아잇" or message.content == "!아잇!":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"11.jpg")
            await message.channel.send(file=file)
            return None;
        if message.content == "!냥이":
            channel = message.channel;
            await channel.send("언제와!!!")
            return None;
         
         #짝수 인원 입력시 2개팀으로 나눈다
        if "!사다리 " in message.content:
            global count
            count=0
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
            while len(chek) != len(tmp)-1:
                couna = random.randrange(1,count)
                if couna not in chek:
                    chek.append(couna)
                    print(couna)
            for a in chek:
                tmpt.append(tmp[a])
            tmm=count//2
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
            channel = message.channel
            await channel.send(shw1)
            await channel.send(shw2)
            return None
         
        # 서버에 멤버가 들어왔을 때 수행 될 이벤트
    async def on_member_join(self, member):
        msg = "<@{}>님이 서버에 들어오셨어요. 환영합니다.".format(str(member.id))
        await find_first_channel(member.guild.text_channels).send(msg)
        return None

    # 사버에 멤버가 나갔을 때 수행 될 이벤트
    async def on_member_remove(self, member):
        msg = "<@{}>님이 서버에서 나가거나 추방되었습니다.".format(str(member.id))
        await find_first_channel(member.guild.text_channels).send(msg)
        return None
    
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    access_token = os.environ["BOT_TOKEN"]
    client.run(access_token)
