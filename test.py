if "!최근롤." in message.content:
            channel = message.channel
            arr_str = str(message.content).split(".")
            summonerName = arr_str[1]
            kie=RGAPI-32974447-b52e-4c46-a035-8a946a3615ed"
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
