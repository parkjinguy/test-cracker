import discord
import os
import random
#from urllib import parse
import requests
import json
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
#참여
participation=[]
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
            aa="명령어 :  !아잇, !냥이, !안녕, !팀설정, !팀결과, !패치로그 !찌릿, !잠, !일해, !레드, !크래커, !냥, !창규, !냥대노, !죄송\n"
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
        if message.content == "!패치로그":
            aa="2020-07-03 스뜐끼봇이 추가되었습니다.\n"
            aa="2020-07-04 자동 팀설정이 추가되었습니다.\n"
            aa="2020-07-04 스뜐끼 답변 기능이 제거되었습니다.\n"
            aa="2020-07-05 흐뭇, !냥대노, !냥이월급, 모름, 사딸라, !레드, !크래커, !창규, !보리, !리브, !햄울찜, 기분좋아 등이 추가되었습니다.\n"
            aa="2020-07-05 !초코, !여긴 따뜻해 등이 추가되었습니다.\n"
            aa="2020-07-05 !도라이, !나루토는 전설이다.\n"
            aa="2020-07-06 !투표 기능이 추가되었습니다.\n"
            aa="2020-07-06 !냥, !찌릿, !잠, !일해, 다이어트 기능이 추가되었습니다.\n"
            aa="2020-07-06 !요염, !뭘, !사륜안 기능이 추가되었습니다.\n"
            aa="2020-07-08 햄울찜님의 요청으로 !크래커(수정), !경이(추가) 되었습니다.\n"
            aa="2020-07-10 cracker님의 요청으로 !롤.(추가) 되었습니다.\n"
            aa="2020-07-11 !롤.(수정) 되었습니다.\n"
            aa="2020-07-11 대부분 명령어가 다른 채팅과 같이 사용하게(수정) 되었습니다.\n"
            aa="2020-07-11 햄울찜님의 요청으로 !하 인생(추가) 되었습니다.\n"
            aa="2020-07-17 크래커님의 요청으로 할짝(추가) 되었습니다.\n"
            aa="2020-07-18 냥이님의 요청으로 !냥이(수정) 되었습니다.\n"
            aa="2020-07-18 햄찌님의 요청으로 !경청(추가) 되었습니다.\n"
            aa="2020-07-18 크래커님의 요청으로 !글적(추가) 되었습니다.\n"
            aa="2020-07-18 크래커님의 요청으로 생축(추가) 되었습니다.\n"
            aa="2020-07-21 햄찌님의 요청으로 !(추가) 되었습니다.\n"
            aa="2020-07-21 햄찌님의 요청으로 !피식(추가) 되었습니다.\n"
            aa="2020-07-23 핥짝님의 요청으로 !피식(추가) 되었습니다.\n"
            aa="2020-07-27 크래커님의 요청으로 !참여,!참여결과, !참여취소(추가) 되었습니다.\n"
            aa="2020-07-27 크래커님의 요청으로 !참가,!참가결과, !참가취소(수정) 되었습니다.\n"
            aa="2020-07-27 블루스크린님의 요청으로 !인성(수정) 되었습니다.\n"
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
        if "!도라이" in message.content:
            channel = message.channel
            await channel.send("배신자!!!")
            return None
        if "!나루토는 전설이다" in message.content:
            channel = message.channel
            await channel.send("미안하다 이거 보여주려고 어그로끌었다.. 나루토 사스케 싸움수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 싸움이다.. 그찐따같던 나루토가 맞나? 진짜 나루토는 전설이다..진짜옛날에 맨날나루토봘는데 왕같은존재인 호카게 되서 세계최강 전설적인 영웅이된나루토보면 진짜내가다 감격스럽고 나루토 노래부터 명장면까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 카카시앞에 운석날라오는 거대한 걸 사스케가 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 나루토가 없다면 마을을 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 나루토처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 보루토를 최근에 알았는데 미안하다.. 지금20화보는데 진짜 나루토세대나와서 너무 감격스럽고 모두어엿하게 큰거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 시노는 말이많아진거같다 좋은선생이고..그리고 보루토왜욕하냐 귀여운데 나루토를보는것같다 성격도 닮았어 그리고버루토에 나루토사스케 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 보루토에 나오는 신급괴물임?ㅡ 나루토사스케 합체한거봐라 진짜 ㅆㅂ 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 나루토사스케가 저렇게 되다니 진짜 눈물나려고했다.. 버루토그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. ㅆㅂ 사스케 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 나루토는 진짜 애니중최거명작임..")
            return None
        #사진 
        if "!아잇" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"11.jpg")
            await message.channel.send(file=file)
            return None
        if "생축" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"happy.jpg")
            await message.channel.send(file=file)
            return None
        if "!햄프" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"2.jpg")
            await message.channel.send(file=file)
            return None
        if  message.content=="!냥이":
            channel = message.channel
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"3.jpg")
            await message.channel.send(file=file)
            return None
        if "!찌릿" in message.content:
            channel = message.channel
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"21.jpg")
            await message.channel.send(file=file)
            return None
        if  message.content=="!냥":
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"20.jpg")
            await message.channel.send(file=file)
            return None
        if "!레드" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"6.jpg")
            await message.channel.send(file=file)
            return None
        if "!잠" in message.content:
            channel = message.channel
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"22.jpg")
            await message.channel.send(file=file)
            return None
        if "!크래커" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"5.jpg")
            await message.channel.send(file=file)
            return None
        if "!보리" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"7.jpg")
            await message.channel.send(file=file)
            return None
        if "!리브" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"8.jpg")
            await message.channel.send(file=file)
            return None
        if "!창규" in message.content:
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
        if "!햄울찜" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"10.jpg")
            await message.channel.send(file=file)
            return None
        if "!냥대노" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"16.jpg")
            await message.channel.send(file=file)
            return None
        if "!냥이월급" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"15.jpg")
            await message.channel.send(file=file)
            return None
        if "!초코" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"17.jpg")
            await message.channel.send(file=file)
            return None
        if "!여긴 따뜻해" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"18.jpg")
            await message.channel.send(file=file)
            return None
        if "!일해" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a1.gif")
            await message.channel.send(file=file)
            return None
        if "!죄송" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a2.jpg")
            await message.channel.send(file=file)
            return None
        if "!다이어트" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a3.png")
            await message.channel.send(file=file)
            return None
        if "!요염" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a4.jpg")
            await message.channel.send(file=file)
            return None
        if "!뭘 꼬라봐" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a5.jpg")
            await message.channel.send(file=file)
            return None
        if "!사륜안" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a6.jpg")
            await message.channel.send(file=file)
            return None
        if "!경이" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a7.jpg")
            await message.channel.send(file=file)
            return None
        if "!하 인생" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a8.jpg")
            await message.channel.send(file=file)
            return None
        if "!돌맹" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a9.jpg")
            await message.channel.send(file=file)
            return None
        if "할짝" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a10.jpg")
            await message.channel.send(file=file)
            return None
        if "!잘한다" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a11.png")
            await message.channel.send(file=file)
            return None
        if "!냥청" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a13.jpg")
            await message.channel.send(file=file)
            return None
        if "!글적" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a14.gif")
            await message.channel.send(file=file)
            return None
        if "!짱깨" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a15.jpg")
            await message.channel.send(file=file)
            return None
        if "!피식" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a16.jpg")
            await message.channel.send(file=file)
            return None
        if "시무룩" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a17.jpg")
            await message.channel.send(file=file)
            return None
        if "!핥짝핥짝" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a18.jpg")
            await message.channel.send(file=file)
            return None
        if "!멍 때리는중" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a19.jpg")
            await message.channel.send(file=file)
            return None
        if "!인성" in message.content:
            dirctory = os.path.dirname(__file__)
            file=discord.File(dirctory+"a21.jpg")
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
            
        if "!롤." in message.content:
            channel = message.channel
            arr_str = str(message.content).split(".")
            summonerName = arr_str[1]
            kie="RGAPI-3791d24d-fc42-4c2d-bf78-f7a821a6c207"
            APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + arr_str[1]
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://developer.riotgames.com",
                "X-Riot-Token": kie
                }
            res = requests.get(APIURL, headers=headers)
            tmm=res.json()
            id=tmm['id']
            summonerName=id
            APIURL = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://developer.riotgames.com",
                "X-Riot-Token": kie
                }
            res = requests.get(APIURL, headers=headers)
            tmm=res.json()
            ac=""
            try:
                if tmm[0]['queueType']=="RANKED_FLEX_SR":
                    ac=ac+"자랭"
                else:
                    ac=ac+"솔랭"
                ac=ac+"\n티어 : "+repr(tmm[0]['tier'])+" "+repr(tmm[0]['rank'])+"\n 승리수 : "+repr(tmm[0]['wins']) +"\n 패배수 : "+repr(tmm[0]['losses'])+"\n점수"+repr(tmm[0]['leaguePoints'])+"\n"
                if tmm[1]['queueType']=="RANKED_FLEX_SR":
                    ac=ac+"자랭"
                else:
                    ac=ac+"솔랭"
                ac=ac+"\n티어 : "+repr(tmm[1]['tier'])+" "+repr(tmm[1]['rank'])+"\n 승리수 : "+repr(tmm[1]['wins']) +"\n 패배수 : "+repr(tmm[1]['losses'])+"\n점수"+repr(tmm[1]['leaguePoints'])+"\n"
            except:
                ac=ac+'랭크없음'
            await channel.send(ac)
        if "!최근롤." in message.content:
            channel = message.channel
            arr_str = str(message.content).split(".")
            summonerName = arr_str[1]
            kie="RGAPI-3791d24d-fc42-4c2d-bf78-f7a821a6c207"
            APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + arr_str[1]
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://developer.riotgames.com",
                "X-Riot-Token": kie
                }
            res = requests.get(APIURL, headers=headers)
            tmm=res.json()
            id=tmm['id']
            print(id)
            summonerName=id
            APIURL = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + id
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://developer.riotgames.com",
                "X-Riot-Token": kie
                }
            res = requests.get(APIURL, headers=headers)
            tmm=res.json()
            num = {0,1,2,3,4,5,6,7,8,9}
            ac=""
            try:
                #print(tmm)
                for i in num:
                    ac =ac+ tmm["participants"][i]["summonerName"]+"\n"
                await channel.send("현재 같이 하고있는 유저는 \n"+ac)
                return
            except:
                await channel.send("현재 검색 유저의 경기가 없습니다. \n")
                return
            return
        #참여 여부
        if message.content == "!참가":
            channel = message.channel
            try:
                for i in participation:
                    if i == message.author.name:
                        await channel.send("중복참가입니다.")
                        return
                participation.append(message.author.name)
                await channel.send(message.author.name+"님 참가하였습니다.")
            except:
                await channel.send("에러")
            return
        if message.content == "!참가취소":
            channel = message.channel
            for i in participation:
                if i == message.author.name:
                    participation.remove(message.author.name)
                    await channel.send("취소되었습니다.")
                    return
            await channel.send("참가가자 아닙니다.")
            return
        if message.content == "!참가인원":
            channel = message.channel
            try:
                tm="현재 : "
                count=0
                res=len(participation)
                for i in participation:
                    count=count+1
                    if count >= 1 and count != res:
                        tm=tm+i+", "
                    else:
                        tm=tm+i
                await channel.send(tm)
                await channel.send("인원수는 : "+str(count)+"명")
            except:
                await channel.send("에러")
            return
        if "!참여 " in message.content:
            channel = message.channel
            try:
                if "Cracker" == message.author.name or "냥이" == message.author.name:
                    arr_str = str(message.content).split(" ")
                    name = arr_str[1]
                    for i in participation:
                        if i == name:
                            await channel.send("중복참가입니다.")
                            return
                    participation.append(name)
                    await channel.send(name + "님을 추가했습니다.")
            except:
                await channel.send("다시입력해주세요")
            return
        if message.content == "!참가결과":
            channel = message.channel
            try:
                aa=""
                tm="참가인원은 : "
                count=0
                res=len(participation)
                for aa in participation:
                    count=count+1
                    if count >= 1 and count != res:
                        tm=tm+aa+", "
                    else:
                        tm=tm+aa+" "
                if count == 0:
                    await channel.send("참가자가 없습니다.")
                else:
                    await channel.send(tm)
                    await channel.send("참가인원은 : "+str(count)+"명")
            except:
                await channel.send("참가자가 없습니다.")
            participation.clear()
            return
    
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    access_token = os.environ["BOT_TOKEN"]
    client.run(access_token)
