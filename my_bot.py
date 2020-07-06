
# discord 라이브러리 사용 선언
import discord
import os
import random
#팀나누기
tmp=[]
tmpt=[]
chek=[]
result1=[]
result2=[]
#투표
topo=[]
topo1=[]
topo2=[]
topo3=[]
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
        #메시지 해당 사람 태그 호출
        '''if message.content == "과자":
            channel = message.channel;
            msg = "<@{}>".format("#9522")
            await client.send_message(channel, "<@creake>")
            return None'''
        if message.content == "!도움말":
            aa="명령어 :  !아잇, !냥이, !안녕, !팀설정, !팀결과, !패치로그, 모름, 사딸라, !레드, !크래커, !창규, 흐뭇, !냥대노,\n"
            aa= aa+" !냥이월급날, !보리, !리브, !햄울찜, 기분좋아, !초코, !여긴 따뜻해, !도라이, !나루토는 전설이다, !투표, !투표결과, !찬성,\n"
            aa= aa+" !반대, !투표종료, !냥, !찌릿, !잠, !일해, !죄송\n"
            aa= aa+"!팀설정은 !팀설정 인원1 인원2 인원3로 설정을 하며 무조건 짝수만 가능합니다(설정하면 자동으로 팀을 나눕니다.) \n"
            aa= aa+"!투표설정은 !투표 투표내용 하면 투표가 시작되며 !찬성, !반대로 투표를 하며 !투표결과로 결과를 확인합니다 그리고 !투표종료를 하면 중지를 합니다 "
            if message.author.dm_channel:
                await message.author.dm_channel.send(aa)
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()#dm채널 없으면 추가후 전송
                await channel.send(aa)
            return None
        if message.content == "!패치로그":
            aa="2020-07-03 스뜐끼봇이 추가되었습니다.\n"
            aa="2020-07-04 자동 팀설정이 추가되었습니다.\n"
            aa="2020-07-04 스뜐끼 답변 기능이 제거되었습니다.\n"
            aa="2020-07-05 흐뭇, !냥대노, !냥이월급, 모름, 사딸라, !레드, !크래커, !창규, !보리, !리브, !햄울찜, 기분좋아 등이 추가되었습니다.\n"
            aa="2020-07-05 !초코, !여긴 따뜻해 등이 추가되었습니다.\n"
            aa="2020-07-05 !도라이, !나루토는 전설이다.\n"
            aa="2020-07-06 !투표 기능이 추가되었습니다.\n"
            aa="2020-07-06 !냥, !찌릿, !잠, !일해, ! 기능이 추가되었습니다.\n"
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
        if message.content == "!도라이":
            channel = message.channel
            await channel.send("배신자!!!")
            return None
        if message.content == "!나루토는 전설이다":
            channel = message.channel
            await channel.send("미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..")
            return None
        #사진 
        if message.content == "!아잇":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"11.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!햄프":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"2.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!냥이":
            channel = message.channel
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"3.jpg")
            await message.channel.send(file=file)
            await channel.send("언제와!!!")
            return None
        if message.content == "!찌릿":
            channel = message.channel
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"21.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!냥":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"20.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!레드":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"6.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!잠":
            channel = message.channel
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"22.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!크래커":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"5.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!보리":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"7.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!리브":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"8.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!창규":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"4.jpg")
            await message.channel.send(file=file)
            return None
        if "흐뭇" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"9.jpg")
            await message.channel.send(file=file)
            return None
        if "사딸라" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"12.jpg")
            await message.channel.send(file=file)
            return None
        if "모름" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"13.png")
            await message.channel.send(file=file)
            return None
        if "기분좋아" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"14.gif")
            await message.channel.send(file=file)
            return None                          
        if message.content == "!햄울찜":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"10.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!냥대노":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"16.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!냥이월급":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"15.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!초코":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"17.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!여긴 따뜻해":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"18.jpg")
            await message.channel.send(file=file)
            return None
        if message.content == "!일해":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a1.gif")
            await message.channel.send(file=file)
            return None
        if message.content == "!죄송":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a2.jpg")
            await message.channel.send(file=file)
            return None
        #기능 부분
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
        #투표
        
        if "!투표 " in message.content:
            channel = message.channel
            arr_str = str(message.content).split(" ")
            topo.append(arr_str[1])
            tm = "현재 "+topo[0]+"의 투표가 추가되었습니다."
            await channel.send(tm)
            await channel.send("!찬성, !반대를 해주세요")
            
        if message.content == "!찬성":
            channel = message.channel
            ac=0
            try:
                for a in topo:
                    print("ff")
                    for c in topo2:
                        print("ff")
                        for i in topo1:
                            if i == message.author.id:
                                await channel.send("중복참여입니다.")
                                return None
                    for i in topo1:
                            if i == message.author.id:
                                await channel.send("중복참여입니다.")
                                return None
                    for i in topo2:
                            if i == message.author.id:
                                await channel.send("중복참여입니다.")
                                return None
                    if ac == 0:
                        print("sa")
                        topo1.append(message.author.id)
                        return None
            except:
                await channel.send("진행중인 투표가 없습니다.")

        if message.content == "!반대":
            channel = message.channel
            ac=0
            try:
                for a in topo:
                    print("ff")
                    for c in topo1:
                        print("dd")
                        for i in topo2:
                            if i == message.author.id:
                                await channel.send("중복참여입니다.")
                                return None
                            print("ss")
                    for i in topo1:
                            if i == message.author.id:
                                await channel.send("중복참여입니다.")
                                return None
                    for i in topo2:
                            if i == message.author.id:
                                await channel.send("중복참여입니다.")
                                return None
                    if ac == 0:
                        print("fs")
                        topo2.append(message.author.id)
                        return None
                    
            except:
                await channel.send("진행중인 투표가 없습니다.")
        if message.content == "!투표 종료":
            channel = message.channel
            await channel.send("투표가 종료되었습니다.")
            topo.clear()
            topo1.clear()
            topo2.clear()
            
        if message.content == "!투표결과":
            channel = message.channel
            try:
                if len(topo1) > len(topo2):
                    print(topo[0])
                    tm1=topo[0]+"의 결과는 찬성이며 총 "+str(len(topo1))+"명이 투표했습니다."
                    await channel.send(tm1)
                elif len(topo2) > len(topo1):
                    tm1=topo[0]+"의 결과는 반대이며 총 "+str(len(topo1))+"명이 투표했습니다."
                    await channel.send(tm1)
                else:
                    tm1=topo[0]+"의 결과는 동점이며 총 "+str(len(topo1)+len(topo2))+"명이 투표했습니다."
                    await channel.send(tm1)
            except:
                await channel.send("현재 진행중인 투표가 없습니다.")
            topo.clear()
            topo1.clear()
            topo2.clear()
        
    
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    access_token = os.environ["BOT_TOKEN"]
    client.run(access_token)
