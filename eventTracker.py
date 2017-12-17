# -*- coding: utf-8 -*-

from urllib import request
import json
from threading import Timer
import time
import os
from qqbot import qqbotsched


'''

                             _ooOoo_
                            o8888888o
                            88" . "88
                            (| -_- |)
                            O\  =  /O
                         ____/`---'\____
                       .'  \\|     |//  `.
                      /  \\|||  :  |||//  \
                     /  _||||| -:- |||||-  \
                     |   | \\\  -  /// |   |
                     | \_|  ''\---/''  |   |
                     \  .-\__  `-`  ___/-. /
                   ___`. .'  /--.--\  `. . __
                ."" '<  `.___\_<|>_/___.'  >'"".
               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
               \  \ `-.   \_ __\ /__ _/   .-` /  /
          ======`-.____`-.___\_____/___.-`____.-'======
                             `=---='
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                     佛祖保佑        永无BUG
'''


@qqbotsched(hour = '23,1')
def clock(bot):
    gl = bot.List('group')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '护肝小天使取名提醒您，现在已经23点了\n注意身体请及时睡觉喔')



'''
#定时发送高价警报消息
@qqbotsched(second='0')
def warning(bot):
    try:
        for i in warList:
            try: 
                output = '取...取名发现了高价值警报(ฅ´ω`ฅ)\n\n' + worldDict[0][i['MissionInfo']['location']] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
            except:
                output = '取...取名发现了高价值警报(ฅ´ω`ฅ)\n\n' + i['MissionInfo']['location'] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
            output = output + '\n任务: ' + worldDict[0][i['MissionInfo']['missionType']] + ' - ' + worldDict[0][i['MissionInfo']['faction']]
            if 'countedItems' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['countedItems'][0]['ItemType'].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
                item = item + str(i['MissionInfo']['missionReward']['countedItems'][0]['ItemCount']) + ' + 现金 ' + str(i['MissionInfo']['missionReward']['credits'])
            elif 'items' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['items'][0].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
                item = item + ' + 现金 ' + str(i['MissionInfo']['missionReward']['credits'])
            else:
                item = '现金 ' + str(i['MissionInfo']['missionReward']['credits'])
            output = output + '\n奖励: ' + item
            timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
            minitue = int(timeLeft/60)
            sec = int(timeLeft - minitue*60)
            output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 '
            gl = bot.List('group', '643489949')
            if gl is not None:
                for group in gl: bot.SendTo(group, output)
            warList.remove(i)
    except:
        pass

'''
'''
@qqbotsched(hour='11,17', minute='55')
def mytask(bot):
    gl = bot.List('group', '456班')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同志们：开饭啦啦啦啦啦啦！！！')

'''

#循环
def timerLoop(inc, updateJson):
    t = Timer(inc, updateJson)
    t.start()

def loadDict():
    #载入词库
    path = os.path.dirname(os.path.realpath(__file__))
    file = open(path + "\worldDATA.txt", "r")
    itemDirc = [{},{}]
    for lines in file.readlines():
        lines = lines.rstrip("\n")
        linebar = lines.split('=')
        itemDirc[0][linebar[0]] = linebar[1]
        itemDirc[1][linebar[1]] = linebar[0]
    file.close()
    return itemDirc

#获取JSON文件
def updateJson():
    print('updating world data...')
    url = 'http://content.warframe.com/dynamic/worldState.php'
    req = request.Request(url)
    data = request.urlopen(req).read()
#    json_string=json.dumps(info['body'])
    data = json.loads(data)
    del(data['Date'])
    del(data['WorldSeed'])
    del(data['Version'])
    del(data['MobileVersion'])
    del(data['BuildLabel'])
    del(data['Events'])
    del(data['Goals'])
    del(data['GlobalUpgrades'])
    del(data['FlashSales'])
    del(data['HubEvents'])
    del(data['NodeOverrides'])
    del(data['BadlandNodes'])
    del(data['PrimeAccessAvailability'])
    del(data['PrimeVaultAvailabilities'])
    del(data['LibraryInfo'])
    del(data['PVPChallengeInstances'])
    del(data['PersistentEnemies'])
    del(data['PVPAlternativeModes'])
    del(data['PVPActiveTournaments'])
    del(data['ProjectPct'])
    del(data['ConstructionProjects'])
    del(data['TwitchPromos'])
    '''
    剩余八个参数：
    Time              > 时间
    Alerts            > 警报
    Sorties           > 突击
    SyndicateMissions > 集团任务
    ActiveMissions    > 裂隙
    Invasions         > 入侵
    VoidTraders       > 虚空商人
    DailyDeals        > 每日折扣
    '''
    global worldData
    global warList
    global lastAlerts
    global thisAlerts
    #存储上一次警报
    try:
        lastAlerts = worldData['Alerts']
    except:
        lastAlerts = []
    #存储worldstate数据
    worldData = data
    print('update complate...')
    #存储本次警报
    thisAlerts = data['Alerts']
    '''
    try:
        for i in lastAlerts:
            thisAlerts.remove(i)
    except:
        pass
    try:
        for i in thisAlerts:
            if 'countedItems' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['countedItems'][0]['ItemType'].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
            elif 'items' in i['MissionInfo']['missionReward']:
                item = i['MissionInfo']['missionReward']['items'][0].split('/')
                try: 
                    item = worldDict[0][item[len(item)-1]]
                except:
                    item = item[len(item)-1]
            for element in ('泥炭萃取物','蓝图','狗蛋','库娃遗传密码','枪托','枪机','破坏者','亡魂','希芙','光环','反应堆','催化剂','裂罅') :
                if (element in item): warList.append(i)
    except:
        pass
    '''
    timerLoop(30, updateJson)

#突击函数
def Sorties():
    output = str(worldDict[0][worldData['Sorties'][0]['Boss']]) + ''
    for i in worldData['Sorties'][0]['Variants']:
        try:
            output = output + '\n\n地点: ' + worldDict[0][i['node']]
        except:
            output = output + '\n\n地点: ' + i['node']
        output = output + '\n任务: ' + worldDict[0][i['missionType']]
        output = output + '\n状态: ' + worldDict[0][i['modifierType']]
    return output

#警报
def Alerts():
    output = '小取名发现现在有警报[' + str(len(worldData['Alerts'])) + ']个：'
    for i in worldData['Alerts']:
        try: 
            output = output + '\n\n' + worldDict[0][i['MissionInfo']['location']] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
        except:
            output = output + '\n\n' + i['MissionInfo']['location'] + ' 等级 ' + str(i['MissionInfo']['minEnemyLevel']) + '-' + str(i['MissionInfo']['maxEnemyLevel'])
        output = output + '\n任务: ' + worldDict[0][i['MissionInfo']['missionType']] + ' - ' + worldDict[0][i['MissionInfo']['faction']]
        if 'countedItems' in i['MissionInfo']['missionReward']:
            item = i['MissionInfo']['missionReward']['countedItems'][0]['ItemType'].split('/')
            try: 
                item = worldDict[0][item[len(item)-1]]
            except:
                item = item[len(item)-1]
            item = item + str(i['MissionInfo']['missionReward']['countedItems'][0]['ItemCount']) + ' + 现金 ' + str(i['MissionInfo']['missionReward']['credits'])
        elif 'items' in i['MissionInfo']['missionReward']:
            item = i['MissionInfo']['missionReward']['items'][0].split('/')
            try: 
                item = worldDict[0][item[len(item)-1]]
            except:
                item = item[len(item)-1]
            item = item + ' + 现金 ' + str(i['MissionInfo']['missionReward']['credits'])
        else:
            item = '现金 ' + str(i['MissionInfo']['missionReward']['credits'])
        output = output + '\n奖励: ' + item
        timeLeft = int(int(i['Expiry']['$date']['$numberLong'])/1000) - time.time()
        minitue = int(timeLeft/60)
        sec = int(timeLeft - minitue*60)
        output = output + '\n剩余时间: ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 '
    return output

def onQQMessage(bot, contact, member, content):
    if content in ('js','奸商','虚空商人') and content != '':
        timeLeft = int(worldData['VoidTraders'][0]['Activation']['$date']['$numberLong'])/1000 - int(worldData['Time'])
        if timeLeft > 0:
            day = int(timeLeft/86400)
            hour = int(timeLeft/3600 - day*24)
            minitue = int(timeLeft/60 - hour*60 - day*1440)
            bot.SendTo(contact, '小取名翻了翻日历ʅ（´◔౪◔）ʃ\n奸商还剩：\n' + str(day) + ' 天 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 就来坑你钱啦！')
        else:
            timeLeft = int(worldData['VoidTraders'][0]['Expiry']['$date']['$numberLong'])/1000 - int(worldData['Time'])
            day = int(timeLeft/86400)
            hour = int(timeLeft/3600 - day*24)
            minitue = int(timeLeft/60 - hour*60 - day*1440)
            bot.SendTo(contact, '奸商还剩：\n' + str(day) + ' 天 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 就要跑啦！\n刺杀奸商 = 3')
    if content in ('平原','希图斯','稀图斯','平原时间') and content != '':
        timeNow = int(time.time() - 1513450500)
        timeNow = timeNow - int(timeNow/9000)*9000
        if timeNow - 6000 < 0 : 
            timeLeft = int(6000 - timeNow)
            hour = int(timeLeft/3600)
            minitue = int(timeLeft/60 - hour * 60)
            sec = int(timeLeft - minitue*60 - hour * 3600)
            output = '小取名偷偷告诉你，白天的平原风景正好，赶紧去捕鱼吧~\n\n还剩 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 Boss就要来吓人了喔'
            bot.SendTo(contact,output)
        elif timeNow - 3000 >= 0 : 
            timeLeft = int(9000 - timeNow)
            hour = int(timeLeft/3600)
            minitue = int(timeLeft/60 - hour*60)
            sec = int(timeLeft - minitue*60 - hour * 3600)
            output = '晚上啦，平原闹鬼啦\n\n还剩 ' + str(hour) + ' 小时 ' + str(minitue) + ' 分钟 ' + str(sec) + ' 秒 Boss就要休息不吓人了哟。'
            bot.SendTo(contact,output)
    if content in ('突击','每日') and content != '':
        bot.SendTo(contact,Sorties())
    if content in ('警报') and content != '':
        bot.SendTo(contact, Alerts())
    if content in ('集团任务') and content != '':
        bot.SendTo(contact, '功能未上线！')
    if content in ('裂隙') and content != '':
        bot.SendTo(contact, '功能未上线！')
    if content in ('入侵') and content != '':
        bot.SendTo(contact, '功能未上线！')
    if content in ('每日折扣','折扣') and content != '':
        bot.SendTo(contact, '功能未上线！')

#开始循环
print('loading directionary...')
#wroldData[0]是中>英
#wroldData[1]是英>中
worldDict = loadDict()
worldData = {}
warList = []
lastAlerts = []
thisAlerts = []
updateJson()