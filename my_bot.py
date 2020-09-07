import discord
import os
import random
#from urllib import parse
import requests
import json
import pymysql
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
participation1=[]
participation2=[]
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
            aa= "명령어 : !팀설정, !팀결과, !투표, !투표결과, !찬성, !반대, !투표종료, !롤., !참여설정., !참여목록, !참여.\n"
            aa= aa+"!참여인원., !참가입력., !참여종료., !탄종류(9x19) \n"
            aa= aa+"!팀설정은 !팀설정 인원1 인원2 인원3로 설정을 하며 무조건 짝수만 가능합니다(설정하면 자동으로 팀을 나눕니다.) \n"
            aa= aa+"!투표설정은 !투표 투표내용 하면 투표가 시작되며 !찬성, !반대로 투표를 하며 !투표결과로 결과를 확인합니다 그리고 !투표종료를 하면 중지를 합니다.\n "
            aa= aa+"!롤.은 .뒤에 롤닉네임을 그대로 적어주시면 잠시뒤에 자동으로 출력이됩니다.\n"
            aa= aa+"!참가입력. 은 !참가입력.뒤에 제목 그리고 뒤에.을 붙이고 참여자 닉네임을 \n"
            aa= aa+"참여순서는 참여설정, 참여, 참여인원, 참여종료 이며 현재 테스트 중인 기능입니다.\n"
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
        
        if "!오픈" in message.content:
            channel = message.channel
            #dirctory = os.path.dirname(__file__)
            #file=discord.File(dirctory+"a21.jpg")
            #await message.channel.send(file=file)
            await message.channel.send("활성화 ")
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
            kie="RGAPI-d9f23dae-0359-467d-a030-a83bce3204fd"
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
            kie="RGAPI-d9f23dae-0359-467d-a030-a83bce3204fd"
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
        #
        if "!참여설정." in message.content:
            channel = message.channel
            conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
            arr = str(message.content).split(".")
            curs = conn.cursor()
            sql = "select name from cat1 where name='"+arr[1]+"'"
            curs.execute(sql)
            row = curs.fetchone()
            try:
                str(row[0])
                await channel.send("이미 존재 합니다.")
                conn.close()
                return
            except:
                conn.close()
                conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
                curs = conn.cursor()
                sql = "insert into cat1(name) values('"+arr[1]+"')"
                curs.execute(sql)
                conn.commit()
                conn.close()
                await channel.send(message.author.name+"님이 "+arr[1]+" 참여 여부 생성 하였습니다.")
                return
            return
        if "!참여목록" in message.content:
            channel = message.channel
            conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
            curs = conn.cursor()
            sql = "select name from cat1"
            curs.execute(sql)
            row = curs.fetchone()
            tmp=""
            while row:
                tmp=tmp+str(row[0])+"\n"
                row=curs.fetchone()
            await channel.send(tmp)
            return
        if "!참여." in message.content:
            channel = message.channel
            conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
            curs = conn.cursor()
            arr = str(message.content).split(".")
            sql = "select * from cat1 where name='"+arr[1]+"'"
            curs.execute(sql)
            try:
                row = curs.fetchone()
                str(row[0])
                conn.close()
                conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
                curs = conn.cursor()
                sql = "insert into cat2 values("+str(row[0])+",'"+str(message.author.name)+"')"
                curs.execute(sql)
                conn.commit()
                conn.close()
                await channel.send(message.author.name+"님이 "+str(row[1])+"에 참여 하였습니다.")
                return
            except:
                await channel.send("이미 참가자 입니다.")
                return
        if "!참여인원." in message.content:
            channel = message.channel
            conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
            curs = conn.cursor()
            
            count=0
            tmp="인원은 : "
            arr = str(message.content).split(".")
            sql = "select cat2.name from cat2 inner join cat1 on cat1.num=cat2.num where cat1.name = '"+arr[1]+"'"
            curs.execute(sql)
            row = curs.fetchone()
            #try:
            while row:
                tmp = tmp + str(row[0])+". "
                count=count+1
                row=curs.fetchone()
            conn.close()
            await channel.send("현재 인원 : "+tmp+" 이며")
            await channel.send("인원은 : "+str(count)+"입니다.")
            return
            #except:
                #await channel.send("현재 목록에 없습니다.")
                #return
        if "!참여종료." in message.content:
            channel = message.channel
            arr = str(message.content).split(".")
            try:
                conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
                curs = conn.cursor()
                sql = "select num from cat1 where name  = '"+str(arr[1])+"'"
                curs.execute(sql)
                row = curs.fetchone()
                conn.close()
                conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
                curs = conn.cursor()
                sql = "delete from cat2 where num  = "+str(row[0])
                curs.execute(sql)
                conn.commit()
                conn.close()
                conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
                curs = conn.cursor()
                sql = "delete from cat1 where name  = '"+arr[1]+"'"
                curs.execute(sql)
                conn.commit()
                conn.close()
                await channel.send(i+" 참여가 종료 되었습니다.")
                return
            except:
                await channel.send("참여 목록에 없습니다.")
                return
            return
        if "!참가입력." in message.content:
            channel = message.channel
            conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
            curs = conn.cursor()
            arr = str(message.content).split(".")
            if "Cracker" == message.author.name or "냥이" == message.author.name:
                sql = "select * from cat1 where name='"+arr[1]+"'"
                curs.execute(sql)
                try:
                    row = curs.fetchone()
                    str(row[0])
                    conn.close()
                    conn = pymysql.connect(host='axxb6a0z2kydkco3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='jji99uozpvwxyq5v', password='wvombycad95zjtqp',db='ar5orud2kuyhu3gv', charset='utf8')
                    curs = conn.cursor()
                    sql = "insert into cat2 values("+str(row[0])+",'"+str(arr[2])+"')"
                    curs.execute(sql)
                    conn.commit()
                    conn.close()
                    await channel.send(arr[2]+"님이 "+str(row[1])+"에 참여 하였습니다.")
                    return
                except:
                    await channel.send("참여 목록에 없습니다.")
                    return
            return
        
        if "!12/70" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"12/70 5.25mm Buckshot 몸 8x27 갑바 15 6운\n"
            tm = tm+ "12/70 8.5mm Magnum Buckshot 몸 8x50 갑바 26 6운\n"
            tm = tm+"12/70 6.5mm Express Buckshot 몸 9x35 갑바 26 6운\n"
            tm = tm+"12/70 7mm Buckshot 몸 8x39 갑 26 6운\n"
            tm = tm+"12/70 Flechette 몸 8x25 갑바 31 3확6높\n"
            await channel.send(tm)
            return
        
        if "!12x70" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"12x70 RIP 265 갑바 11 1무\n"
            tm = tm+"12/70 HP Slug SuperFormance 몸 220 갑 12 1무\n"
            tm = tm+"12/70 Grizzly 40 Slug 몸 190 갑 12 1확2희\n"
            tm = tm+"12/70 HP Slug Copper Sabot Premier 몸 206 갑 46 1확2운3의\n"
            tm = tm+"12x70 Led Slug 몸 167 갑 55 1확2낮3의\n"
            tm = tm+"12/70 Poleva-3 Slug 몸 140 갑 40 1확2높3의\n"
            tm = tm+"12/70 Dual Sabot Slug 몸 2x85 갑 65 1확2높3희\n"
            tm = tm+"12/70 FTX Custom Lite Slug 몸 183 갑 65 2확3희\n"
            tm = tm+"12/70 Poleva-6u Slug 몸 150 갑 50 2확3희\n"
            tm = tm+"12/70 shell with .50 BMG bullet 몸 197 갑 57 2확3높4희\n"
            tm = tm+"12/70 AP-20 Slug 몸 164 갑 65 3확4높5운6의\n"
            await channel.send(tm)
            return
        
        if "!20/70" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"20/70 5.6mm Buckshot 몸8x26 갑바12 6운\n"
            tm = tm+"20/70 6.2mm Buckshot 몸8x22 갑바13 6운\n"
            tm = tm+"20x70 7.5mm Buckshot 몸8x25 갑바14 6운\n"
            tm = tm+"20/70 7.3mm Buckshot 몸9x23 갑바13 6운\n"
            tm = tm+"12x70 Led Slug 몸 167 갑 55 1확2낮3의\n"
            await channel.send(tm)
            return
        
        if "!20x70" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"20/70 Devastator Slug 몸198 갑바13 6무\n"
            tm = tm+"20/70 Slug 'Poleva-3' 몸120 갑바35 1확2희\n"
            tm = tm+"20x70 7.5mm Buckshot 몸8x25 갑바14 6운\n"
            tm = tm+"20/70 Star Slug 몸154 갑바42 1확2높3무\n"
            tm = tm+"20/70 Slug Poleva-6u 몸135 갑바40 1확2높3무\n"
            await channel.send(tm)
            return
        
        if "!9x18" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"9x18 mm PM SP8 gzh 몸67 갑바2 6무\n"
            tm = tm+"9x18 mm PM SP7 gzh 몸77 갑바5 6무\n"
            tm = tm+"9x18 mm PM PSV 몸69 갑바5 6무\n"
            tm = tm+"9x18 mm PM 9 P gzh 몸50 갑바16 1희\n"
            tm = tm+"9x18 mm PM PSO gzh 몸54 갑바13 1희\n"
            tm = tm+"9x18 mm PM PS gs PPO 몸55 갑바16 1낮\n"
            tm = tm+"9x18 mm PM PRS gs 몸58 갑바16 1운\n"
            tm = tm+"9x18 mm PM PPe gzh 몸61 갑바15 1낮\n"
            tm = tm+"9x18 mm PM PPT gzh 몸59 갑바22 1높2의\n"
            tm = tm+"9x18 mm PM Pst gzh 몸50 갑바26 1확2의\n"
            tm = tm+"9x18 mm PM RG028 gzh 몸65 갑바26 1확2희\n"
            tm = tm+"9x18 mm PM 9 BZT gzh 몸53 갑바28 1확2높3의\n"
            tm = tm+"9x18 mm PM PMM	58 몸24 갑바33 2확3낮\n"
            tm = tm+"9x18 mm PM PBM	40 몸28 갑바30 2확3높4의\n"
            await channel.send(tm)
            return
        
        if "!9x18" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"7.62x25mm TT LRNPC 몸66 갑바27 1운\n"
            tm = tm+"7.62x25mm TT LRN 몸64 갑바28 1운\n"
            tm = tm+"7.62x25mm TT FMJ43 몸60 갑바29 1높\n"
            tm = tm+"7.62x25mm TT AKBS 몸58 갑바32 1높2의\n"
            tm = tm+"7.62x25mm TT P gl 몸58 갑바32 1확2의\n"
            tm = tm+"7.62x25mm TT PT gzh T 몸60 갑바34 1확2의\n"
            tm = tm+"7.62x25mm TT Pst gzh 몸50 갑바36 2확3운4의\n"
            await channel.send(tm)
            return
        
        if "!9x19" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"9x19 mm RIP 몸102 갑바11 6무\n"
            tm = tm+"9x19 mm QuakeMaker 몸85 갑바22 1확2의\n"
            tm = tm+"9x19 mm PSO gzh 몸59 갑바32 1확2희\n"
            tm = tm+"9x19 mm Luger CCI 몸70 갑바38 1확2희\n"
            tm = tm+"9x19 mm Green Tracer 몸58 갑바33 1확2운3의\n"
            tm = tm+"9x19 mm Pst gzh 몸54 갑바33 2확3희\n"
            tm = tm+"9x19 mm AP 6.3 몸52 갑바48 3확4낮5높6의\n"
            tm = tm+"9x19 mm 7N31 몸52 갑바53	3확4높5낮6운\n"
            await channel.send(tm)
            return
        
        if "!45" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+".45 RIP 몸127 갑바12 1의\n"
            tm = tm+".45 ACP Hydra-Shok 몸95 갑바30 1확2운\n"
            tm = tm+".45 ACP Lasermatch FMJ 몸74 갑바37 1확2높3의\n"
            tm = tm+".45 ACP FMJ 몸72 갑바36 1확2높3의\n"
            tm = tm+".45 ACP AP 몸70 갑바43 3확4높5운6희\n"
            await channel.send(tm)
            return
        
        if "!9x21" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"9x21 mm SP12 몸80 갑바63 1확2희\n"
            tm = tm+"9x21 mm SP11 몸65 갑바44 1확2운\n"
            tm = tm+"9x21 mm SP10 몸49 갑바46 3확4낮5운6희\n"
            tm = tm+"9x21 mm SP13 몸63 갑바47 3확4높5낮6운\n"
            await channel.send(tm)
            return
        
        if "!5.7x28" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"5.7x28 mm R37.F 몸98 갑바7 1낮\n"
            tm = tm+"5.7x28 mm SS198LF 몸74 갑바15 1확2의\n"
            tm = tm+"5.7x28 mm R37.X 몸81 갑바14 1높2의\n"
            tm = tm+"5.7x28 mm SS197SR 몸62 갑바22 2높3희\n"
            tm = tm+"5.7x28 mm L191 몸58 갑바41 3확4운6희\n"
            tm = tm+"5.7x28 mm SB193 몸54 갑바37 3확4낮5운6희\n"
            tm = tm+"5.7x28 mm SS190 몸49 갑바43 3확4높5낮6운\n"
            await channel.send(tm)
            return
        
        if "!4.6x30" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"4.6x30mm Action SX 몸65 갑바39 1확2희3의\n"
            tm = tm+"4.6x30mm Subsonic SX 몸45 갑바46 3확4높5운6희\n"
            tm = tm+"4.6x30mm FMJ SX 몸43 갑바41 4확5낮6운\n"
            tm = tm+"4.6x30mm AP SX 몸35 갑바46 5확6높\n"
            await channel.send(tm)
            return
        
        if "!9x39" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"9x39 mm SP-5 몸68 갑바52 3확4높5운6희\n"
            tm = tm+"9x39 mm SP-6 몸58 갑바60 4확5높6낮\n"
            tm = tm+"9x39 mm 7N9 SPP 몸64 갑바56 4확5높6낮\n"
            tm = tm+"9x39 mm 7N12 BP 몸60 갑바68 4확6높\n"
            await channel.send(tm)
            return
        
        if "!366" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+".366 TKM Geksa 몸110 갑바38 1확2운\n"
            tm = tm+".366 TKM FMJ 몸98 갑바48 2확3낮5의\n"
            tm = tm+".366 TKM EKO 몸73 갑바40 3확4운5의\n"
            tm = tm+".366 AP 몸90 갑바60 4확5높6낮\n"
            await channel.send(tm)
            return
        
        if "!5.45x39" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"5.45x39 mm SP 몸68 갑바34 1확2의\n"
            tm = tm+"5.45x39 mm HP 몸74 갑바20 1확2의\n"
            tm = tm+"5.45x39 mm PRS 몸60 갑바281확2희\n"
            tm = tm+"5.45x39 mm US 몸65 갑바34 1확2운\n"
            tm = tm+"5.45x39 mm FMJ 몸54 갑바30 1확2높3의\n"
            tm = tm+"5.45x39 mm T 몸57 갑바38 2확3의\n"
            tm = tm+"5.45x39 mm PS 몸50 갑바35 2확3낮3의\n"
            tm = tm+"5.45x39 mm PP 몸46 갑바32 3확4운5의\n"
            tm = tm+"5.45x39 mm BP 몸48 갑바41 3확4낮5희\n"
            tm = tm+"5.45x39 mm BT 몸44 갑바49 3확4높5낮6운\n"
            tm = tm+"5.45x39 mm BS 몸40 갑바57 5확6높\n"
            tm = tm+"5.45x39 mm FMJ 몸54 갑바30 1확2높3의\n"
            tm = tm+"5.45x39 mm 7N39 'Igolnik' 몸37 갑바60 6확\n"
            await channel.send(tm)
            return
        
        if "!5.56x45" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"5.56x45 mm Warmage 몸85 갑바14 1의\n"
            tm = tm+"5.56x45 mm 55 HP 몸75 갑바22 1높\n"
            tm = tm+"5.56x45 mm Mk 255 Mod 몸60 갑바32 1확2낮3의\n"
            tm = tm+"5.56x45 mm M856 T 몸55 갑바34 2확3운4의\n"
            tm = tm+"5.56x45 mm 55 FMJ 몸52 갑바33 2확3낮4의\n"
            tm = tm+"5.56x45 mm M855 몸50 갑바37 3확4운5희\n"
            tm = tm+"5.56x45 mm M856A1 몸51 갑바52 3확4높5낮6운\n"
            tm = tm+"5.56x45 mm M855A1 몸45 갑바52 4확5높5낮\n"
            tm = tm+"5.56x45 mm M995 몸40 갑바58 5확6높\n"
            await channel.send(tm)
            return
        
        if "!7.62x51" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"7.62x39 mm HP 몸87 갑바35 1확2낮3의\n"
            tm = tm+"7.62x39 mm US 몸56 갑바42 2확3높4운5의\n"
            tm = tm+"7.62x39 mm T45M 몸62 갑바46 3확4운5의\n"
            tm = tm+"7.62x39 mm PS 몸57 갑바52 3확4낮5운6희\n"
            tm = tm+"7.62x39 mm BP 몸58 갑바63 4확5높6낮\n"
            await channel.send(tm)
            return
        
        if "!7.62x51" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"7.62x39 mm HP 몸87 갑바35 1확2낮3의\n"
            tm = tm+"7.62x39 mm US 몸56 갑바42 2확3높4운5의\n"
            tm = tm+"7.62x39 mm T45M 몸62 갑바46 3확4운5의\n"
            tm = tm+"7.62x39 mm PS 몸57 갑바52 3확4낮5운6희\n"
            tm = tm+"7.62x39 mm BP 몸58 갑바63 4확5높6낮\n"
            await channel.send(tm)
            return
        
        if "!7.62x54" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"7.62x54R T-46M 몸82 갑바83 4확5낮6운\n"
            tm = tm+"7.62x54R LPS Gzh 몸81 갑바78 4확5낮6운\n"
            tm = tm+"7.62x54R 7N1 Sniper cartridge 몸86 갑바84 4확5높6낮\n"
            tm = tm+"7.62x54R 7BT1 몸78 갑바87 6확\n"
            tm = tm+"7.62x54R SNB 몸75 갑바87 6확\n"
            tm = tm+"7.62x54R 7N37 몸72 갑바88 6확\n"
            await channel.send(tm)
            return
        
        if "!12.7x55" in message.content:
            channel = message.channel
            tm = "무:의미없음, 희:아주 희박, 운:운좋으면, 낮:관통률낮음, 높:높은확률, 확:확정\n"
            tm = tm+"12.7x55 mm PS12A 몸165 갑바22 1확\n"
            tm = tm+"12.7x55 mm PS12 몸115 갑바60 2확3높4희5의\n"
            tm = tm+"12.7x55 mm PS12B 몸102 갑바57 4확5높6낮\n"
            await channel.send(tm)
            return
    
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    access_token = os.environ["BOT_TOKEN"]
    client.run(access_token)
