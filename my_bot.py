
# discord 라이브러리 사용 선언
import discord
import os

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("수정")

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
            channel = message.channel;
            # 답변 내용 구성
            msg = "너도 바보"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg);
            return None;
        if message.content == "!안녕":
            # 현재 채널을 받아옴
            channel = message.channel;
            # 답변 내용 구성
            msg = "연습중인 스뜐기입니다."
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg);
            return None;
        if message.content == "!과자":
            # 현재 채널을 받아옴
            channel = message.channel;
            # 답변 내용 구성
            msg = "과자";
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg);
            return None
        if message.content == "!창규":
            # 현재 채널을 받아옴
            channel = message.channel;
            # 답변 내용 구성
            msg = "하이";
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg);
            return None
        #메시지 해당 사람 태그 호출
        if message.content == "과자":
            channel = message.channel;

            msg = "<@{}>".format(message.author.id);
            await channel.send(msg);
            return None;
        if message.content == "!설명":
            if message.author.dm_channel:
                await message.author.dm_channel.send("DM 채널이 있어서 그냥 보냈어요!")
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                await channel.send("DM 채널이 없어서 만들고 보냈어요!")
            return None;
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
