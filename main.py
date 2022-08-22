import AminoXZ
from time import sleep as sl
from colored import fore
from os import system as s

error_color = fore.RED
successful_color = fore.GREEN
regular_color = fore.GREY_63
input_color = fore.DEEP_SKY_BLUE_2
start = f"""{error_color}

    ╭━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭╮╱╭╮╱╱╱╱╱╱╭╮
    ┃╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┣╯╰┳╯╰╮╱╱╱╱╱┃┃
    ┃╰╯╰┳━━┳━╮╱╱╱╭╮╭┳╮╭┫┣╮╭╋╮╭╋━━┳━━┫┃
    ┃╭━╮┃╭╮┃╭╮┳━━┫╰╯┃┃┃┃┃┃┃┣┫┃┃╭╮┃╭╮┃┃
    ┃╰━╯┃╭╮┃┃┃┣━━┫┃┃┃╰╯┃╰┫╰┫┃╰┫╰╯┃╰╯┃╰╮
    ╰━━━┻╯╰┻╯╰╯╱╱╰┻┻┻━━┻━┻━┻┻━┻━━┻━━┻━╯

    MADE BY Xsarz (Telegram -> @DXsarz)

    GitHub: https://github.com/xXxCLOTIxXx
    Telegram channel: https://t.me/DxsarzUnion
    YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q
    Discord server: https://discord.gg/GtpUnsHHT4

        !! When choosing a method, enter clear to clear the console

{regular_color}"""
client = AminoXZ.Client()

def clear():
    s("clear || cls")
    print(start)

def auth():
    try:client.login(email=input(f"{input_color}Email #~ {regular_color}"), password=input(f"{input_color}Password #~ {regular_color}"))
    except Exception as error:print(f"{error_color}\nError login:\n{error}{regular_color}\n");auth()


def getComId():
    communities=list()
    for num, my_communities in  enumerate(client.get_my_communities(size=1000), 1): print(f'\n{num})',my_communities['name']); communities.append(my_communities)
    try:
        selected_community = int(input(f'\n{input_color}Select community #~ {regular_color}'))-1
        return communities[selected_community]['ndcId']
    except ValueError:print(f"{error_color}\nPlease enter a number{regular_color}\n");getComId()
    except IndexError:print(f"{error_color}\nNumber not found{regular_color}\n");getComId()
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n");getComId()

def banLink():
    try:
        url = input(f'\n{input_color}Enter user link #~ {regular_color}')
        comId = client.get_from_link(url)["extensions"]["linkInfo"]["ndcId"]
        userId = client.get_from_link(url)["extensions"]["linkInfo"]["objectId"]
        info = client.get_user_info(userId=userId, comId=comId)
        nick = info["nickname"]
        lvl = info["level"]
        client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
        print(f"\n{successful_color}|{nick} | {userId} | {lvl} level | successfully banned.{regular_color}\n");sl(1);chooseMethod()
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n");banLink()


def banUid():
    try:
        comId = getComId()
        userId = input(f'\n{input_color}Enter user Id #~ {regular_color}')
        info = client.get_user_info(userId=userId, comId=comId)
        nick = info["nickname"]
        lvl = info["level"]
        client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
        print(f"\n{successful_color}|{nick} | {userId} | {lvl} level | successfully banned.{regular_color}\n");sl(1);chooseMethod()
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n");banUid()


def banNick():
    try:
        nicks = list()
        while True:
            input_nick = input(f'\n{input_color}Leave the field empty to start banning\nEnter a nickname to add it to the targets #~ {regular_color}')
            if input_nick == '':break
            else:nicks.append(input_nick)
        if nicks != []:
            comId=getComId()
            for i in range(3):
                users = client.get_community_members(comId=comId, size=100)["userProfileList"]
                for i in range(len(users)):
                    nick = users[i]['nickname']
                    userId = users[i]['uid']
                    lvl = users[i]['level']
                    if nick in nicks:
                        try:
                            client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
                            print(f"\n{successful_color}|{nick} | {userId} | {lvl} level | successfully banned.{regular_color}\n");sl(1)
                        except Exception as error:print(f"{error_color}\n[{nick} | {userId}] Ban error:\n{error}{regular_color}\n")
            print(f"\n{successful_color}Finish.{regular_color}\n");sl(1)
        else:print(f"{error_color}\nError: {regular_color}\n")

    except ValueError:print(f"{error_color}\nPlease enter a number{regular_color}\n");banNick()
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n")
    chooseMethod()


def banSelectedUser(type):
    try:
        comId = getComId()
        if type == '2':users = client.get_community_members(comId=comId, size=100)["userProfileList"]
        elif type == '1':users = client.get_community_members(comId=comId, size=100, type='online')["userProfileList"]
        if users == []:print(f"{error_color}\nNobody online{regular_color}\n")
        else:
            for i in range(len(users)):
            	nick = users[i]['nickname']
            	userId = users[i]['uid']
            	print(f'{i+1}){nick} | {userId}')
            while True:
                try:
                    num = int(input(f'\n{input_color}Select user #~ {regular_color}'))-1
                    nickname = users[num]['nickname']
                    userId = users[num]['uid']
                    client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
                    print(f"\n{successful_color}|{nickname} | {userId} | successfully banned.{regular_color}\n");sl(1);break
                except ValueError:print(f"{error_color}\nPlease enter a number{regular_color}\n")
                except IndexError:print(f"{error_color}\nNumber not found{regular_color}\n")
                except Exception as error:print(f"{error_color}\n[{nick} | {userId}] Ban error:\n{error}{regular_color}\n");break
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n")
    chooseMethod()

def banLvl():
    try:
        max_lvl = int(input(f'\n{input_color}Enter the level up to which everyone will be banned inclusive #~ {regular_color}'))
        if max_lvl < 1 or max_lvl > 19:print(f"{error_color}\nError: Valid numbers are from 1 to 19.{regular_color}\n");banLvl()
        else:
            comId=getComId()
            for i in range(3):
                users = client.get_community_members(comId=comId, size=100)["userProfileList"]
                for i in range(len(users)):
                    nick = users[i]['nickname']
                    userId = users[i]['uid']
                    lvl = users[i]['level']
                    if max_lvl >= lvl:
                        try:
                            client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
                            print(f"\n{successful_color}|{nick} | {userId} | {lvl} level | successfully banned.{regular_color}\n");sl(1)
                        except Exception as error:print(f"{error_color}\n[{nick} | {userId}] Ban error:\n{error}{regular_color}\n")
            print(f"\n{successful_color}Finish.{regular_color}\n");sl(1)
    except ValueError:print(f"{error_color}\nPlease enter a number{regular_color}\n");banLvl()
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n")
    chooseMethod()

def banManySymbols():
    try:
        comId=getComId()
        for i in range(3):
            users = client.get_community_members(comId=comId, size=100)["userProfileList"]
            for i in range(len(users)):
                nick = users[i]['nickname']
                userId = users[i]['uid']
                lvl = users[i]['level']
                bio = users[i]['content']
                if bio != None:
                    if len(bio) > 5000:
                        try:
                            client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
                            print(f"\n{successful_color}|{nick} | {userId} | {lvl} level | successfully banned.{regular_color}\n");sl(1)
                        except Exception as error:print(f"{error_color}\n[{nick} | {userId}] Ban error:\n{error}{regular_color}\n")
        print(f"\n{successful_color}Finish.{regular_color}\n");sl(1)
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n")
    chooseMethod()

def avaBan():
    try:
        comId=getComId()
        for i in range(3):
            users = client.get_community_members(comId=comId, size=100)["userProfileList"]
            for i in range(len(users)):
                nick = users[i]['nickname']
                userId = users[i]['uid']
                lvl = users[i]['level']
                if users[i]['icon'] is None:
                    try:
                        client.ban(userId=userId, reason="Ban script @DXsarz", comId=comId)
                        print(f"\n{successful_color}|{nick} | {userId} | {lvl} level | successfully banned.{regular_color}\n");sl(1)
                    except Exception as error:print(f"{error_color}\n[{nick} | {userId}] Ban error:\n{error}{regular_color}\n")
        print(f"\n{successful_color}Finish.{regular_color}\n");sl(1)
    except Exception as error:print(f"{error_color}\nError:\n{error}{regular_color}\n")
    chooseMethod()


def chooseMethod():
    method = input(f"\n1)Ban by link\n2)Ban by uid\n3)Ban everyone with matching nickname\n4)Ban by last / online users\n5)Ban by level\n6)Ban anyone with a lot of characters in their description\n7)Ban everyone who doesn't have an avatar\n{input_color}Choose a ban method #~ {regular_color}")
    if method == '1':banLink()
    elif method == '2':banUid()
    elif method == '3':banNick()
    elif method == '4':
        while True:
            type = input(f"\n1)Select online users\n2)Select last joined users\n{input_color}Select type #~ {regular_color}")
            if type == '1':banSelectedUser(type='1');break
            elif type == '2': banSelectedUser(type='2');break
            else:print(f"\n{error_color}Choose one of the proposed types{regular_color}\n");sl(1)
    elif method == '5':banLvl()
    elif method == '6':banManySymbols()
    elif method == '7':avaBan()
    elif method.lower() == 'clear':clear();chooseMethod()
    else:print(f"\n{error_color}Invalid method, please select one of the suggested methods{regular_color}\n");sl(1);chooseMethod()

def main():
    print(start)
    auth()
    chooseMethod()


if __name__ == '__main__':
    main()
