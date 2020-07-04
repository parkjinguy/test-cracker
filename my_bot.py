
# discord 라이브러리 사용 선언
import discord
import os

class chatbot(discord.Client):
    up_size = 0
    low_size = 0
    upper = 0
    lower = 0
    col = 0
    row = 0
    arr = []
    arr_int = []
    flag = 0
    def drawing(up, low):
    global col
    global row
    global arr
    global arr_int
    col = len(up*2)-1
    row = 8
    arr = [["　"]*col for i in range(row)]
    arr_int = [[0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            if j%2 == 0:
                arr[i][j] = "l"
                arr_int[i][j] = 1
    for i in range(row):
        for j in range(col-2): 
            if arr_int[i][j] == 1:
                if random.randrange(1,4) == 1:
                    arr[i][j+1] = "ㅡ"
                    arr_int[i][j] = 2
                    arr_int[i][j+1] = 4
                    arr_int[i][j+2] = 3
            j = j+1
            
    def riding(n):
        global arr_int
        i = 0
        j = n*2
        while(i!=8):
            if arr_int[i][j] == 2:
                j = j+2
                i = i+1
            elif arr_int[i][j] == 3:
                j = j-2
                i = i+1
            elif arr_int[i][j] == 1:
                i = i+1
        j = j/2
        return j
    
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
        
        global up_size
        global low_size
        global upper
        global lower
        global col
        global row
        global flag
        if message.content.startswith('!사다리설정'): #윗줄과 아랫줄의 값을 설정함
            arr_str = str(message.content).split(' ')
            if arr_str[1] == '0':
                upper = arr_str[2].split('/')
                if len(upper)>8:
                    embed = discord.Embed(description = "사다리 윗줄이 너무 많아요!!\n(최대 8)")
                    await client.send_message(message.channel,embed = embed)
                    upper = []
                else:
                    embed = discord.Embed(description = "윗줄 설정 완료.")
                    await client.send_message(message.channel, embed = embed)
                up_size = len(upper)
            elif arr_str[1] == '1':
                lower = arr_str[2].split('/')
                if len(lower)>8:
                    embed = discord.Embed(description = "사다리 아랫줄이 너무 많아요!!\n(최대 8)")
                    await client.send_message(message.channel,embed = embed)
                    lower = []
                else:
                    embed = discord.Embed(description = "아랫줄 설정 완료.")
                    await client.send_message(message.channel, embed = embed)
                low_size = len(lower)

        elif message.content.startswith('!설정완료'): #사다리 그리기
            if up_size!=low_size:
                embed = discord.Embed(description = "사다리 윗줄과 아랫줄의 크기가 다릅니다.")
                await client.send_message(message.channel, embed = embed)
            elif up_size == 0 | low_size == 0:
                embed = discord.Embed(description = "사다리 윗줄 혹은 아랫줄의 설정을 확인해주세요.")
                await client.send_message(message.channel, embed = embed)
            else:
                drawing(upper,lower)
                ms = ""
                for i in range(up_size):
                    ms = ms + chr(49+i) + " : " + upper[i] + "　"*2 + chr(97+i) + " : " + lower[i] + "\n"
                for i in range(up_size):
                    ms = ms + chr(49+i)
                    if i!=up_size-1:
                        ms = ms + "..."
                ms = ms + "\n"
                for i in range(len(arr)):
                    for j in range(len(arr[i])):
                        ms = ms + arr[i][j]
                    ms = ms+"\n"
                for i in range(low_size):
                    ms = ms + chr(97+i)
                    if i!=up_size-1:
                        if i>=4:
                            ms = ms+"...."
                        else:
                            ms = ms + "..."
                embed = discord.Embed(title="사다리 탄다!!", description = ms)
                await client.send_message(message.channel,embed = embed)    
                up_result = []
                low_result = []
                for k in range(up_size):
                    up_result.append(upper[k])
                for k in range(low_size):
                    low_result.append(lower[k])
                flag = 1 
        elif message.content.startswith('!사다리진행'):
            arr_str = str(message.content).split(' ')
            if int(arr_str[1])>0 & int(arr_str[1])<up_size:
                pre_result = list(range(8))
                result = list(range(8))
                pre_result[int(arr_str[1])-1] = upper[int(arr_str[1])-1]
                result[int(arr_str[1])-1] = lower[int(riding(int(arr_str[1])-1))]
                embed = discord.Embed(description = pre_result[int(arr_str[1])-1] + " -> " + result[int(arr_str[1])-1])
                await client.send_message(message.channel,embed=embed)
        
        elif message.content.startswith('!사다리결과'):
            if flag==1:
                pre_result = list(range(8))
                result = list(range(8))
                ms_result = ""
                for i in range(up_size):
                    pre_result[i] = upper[i]
                    result[i] = lower[int(riding(i))]
                    if i != up_size-1:
                        ms_result = ms_result + pre_result[i] + " -> " + result[i] + "\n"
                    else:
                        ms_result = ms_result + pre_result[i] + " -> " + result[i]
                embed = discord.Embed(description = ms_result)
                await client.send_message(message.channel,embed=embed)
            else:
                embed = discord.Embed(description = "사다리 윗줄 혹은 아랫줄의 설정을 확인해주세요.")
                await client.send_message(message.channel, embed = embed)
            
        elif message.content.startswith('!설명'):
            embed = discord.Embed(description = "- 간단한 사다타기 기능을 가진 봇\n- 사다리를 텍스트 형식으로 출력\n- 명령어\n　- !사다리설정 (0 or 1) (ID1)/(ID2)/.../(IDn)\n　　- 0일 시 사다리타기 윗 줄 설정\n　　- 1일 시 사다리 타기 아랫 줄 설정\n　　- 윗 줄과 아랫 줄의 개수가 다를 경우 진행x\n　- !설정완료\n　　- 이 명령어를 입력할 때마다 새로운 사다리를 그림\n　- !사다리진행 (1~n)\n　　- 인덱스 값에 해당하는 ID의 사다리타기 결과 출력\n　- !사다리결과\n　　- 사다리타기의 모든 결과를 간단하게 출력")
            await client.send_message(message.channel, embed = embed)
        
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
