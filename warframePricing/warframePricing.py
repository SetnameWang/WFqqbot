# -*- coding: utf-8 -*-

'''
版权所有（C） 2017 <SetnameWang>
这一程序是自由软件，你可以遵照自由软件基金会出版的GNU通用公共许可证条款来修改和重新发布这一程序。或者用许可证的第二版，或者（根据你的选择）用任何更新的版本。
发布这一程序的目的是希望它有用，但没有任何担保。甚至没有适合特定目的的隐含的担保。更详细的情况请参阅GNU通用公共许可证。
你应该已经和程序一起收到一份GNU通用公共许可证的副本。如果还没有，
写信给：
The Free Software Foundation, Inc., 675 Mass Ave, Cambridge,
MA02139, USA
还应加上如何和你保持联系的信息。
如果程序以交互方式进行工作，当它开始进入交互方式工作时，使它输出类似下面的简短声明：
Gnomovision 第69版， 版权所有（C） 19XX， 作者姓名，
Gnomovision绝对没有担保。 要知道详细情况，请输入‘show w’。
这是自由软件，欢迎你遵守一定的条件重新发布它，要知道详细情况，
请输入‘show c’。
假设的命令‘show w’和‘show c’应显示通用公共许可证的相应条款。当然，你使用的命令名称可以不同于‘show w’和‘show c’。根据你的程序的具体情况，也可以用菜单或鼠标选项来显示这些条款。
如果需要，你应该取得你的上司（如果你是程序员）或你的学校签署放弃程序版权的声明。下面只是一个例子，你应该改变相应的名称：
Yoyodyne公司以此方式放弃James Harker
所写的 Gnomovision程序的全部版权利益。
，1989.4.1
Ty coon副总裁
这一许可证不允许你将程序并入专用程序。如果你的程序是一个子程序库。
你可能会认为用库的方式和专用应用程序连接更有用。如果这是你想做的事，使用GNU库通用公共许可证代替本许可证。
'''

from blitz_js_query import Blitz
import json
import os

#调用 API
def getInfo(name, detial):
    try: 
        name = itemDirectionary[0][name]
    except:
        empty = True
    url = '/warframe/v1/items/'+name+'/statistics'
    print(url)
    global tempory
    #从API获取数据并且传参给output函数
    blitz_api.get(url).then(lambda res : output(res, detial))
    print(tempory)
    return tempory

def output(info, detial):
#    转化JSON格式数据
#    json_string=json.dumps(info['body'])
#    info = json.loads(json_string)
    global tempory
    infos = json.loads(info['body'])
    '''
    print('----------------')
    print('名称: ' + infos['name'])
    print('----------------')
    print('需求/供给：' + str(infos['demand']['count']) + '(' + str(int(infos['demand']['percentage']*100)) + '%)/' + str(infos['supply']['count']) + '(' + str(int(infos['supply']['percentage']*100)) + '%)')
    print('-------------------------求购-------------------------')
    '''
    desup =  str(infos['demand']['count']) + '(' + str(int(infos['demand']['percentage']*100)) + '%)/' + str(infos['supply']['count']) + '(' + str(int(infos['supply']['percentage']*100)) + '%)'
    tempory = '小取名为您查询到以下信息(。・∀・)ノ\n名称: ' + infos['name'] + '\n需求/供给: ' + desup
    avg = ''
    median = ''
    min = ''
    max = ''
    name = ''
    setPlace = 1
    #翻译名称
    for i in range(0, len(infos['components'])):
        if infos['components'][i]['name'] == 'Set': setPlace = i
        infos['components'][i]['name'] = itemDirectionary[1][infos['components'][i]['name']]
    infos['components'][setPlace] , infos['components'][0] = infos['components'][0] , infos['components'][setPlace]
    #写入求购内容
    numInfo = len(infos['components'])
    if detial :
        for i in range(0,numInfo):
            avg = avg + str(round(infos['components'][i]['buying']['avg'], 1)) + '\t'
            median =  median + str(round(infos['components'][i]['buying']['median'], 1)) + '\t'
            max = max + str(round(infos['components'][i]['buying']['max'], 1)) + '\t'
            min = min + str(round(infos['components'][i]['buying']['min'], 1)) + '\t'
            name = name + str(infos['components'][i]['name']) + '\t'
    #        median[i] = str(int(infos['components'][i]['buying']['median']*100)/10)
    #        max[i] = str(int(infos['components'][i]['buying']['min']*100)/10)
    #        min[i] = str(int(infos['components'][i]['buying']['max']*100)/10)
    #        name[i] = str(infos['components'][i]['name'])
        tempory = tempory + '\n-' + numInfo*5*'-' + '求购' + numInfo*5*'-'  + '-' + '\n部件名称: ' + name + '\n最多出价: ' + median + '\n最大出价: ' + max + '\n最小出价: ' + min + '\n平均出价: ' + avg + '\n'
        #清空数据集
        avg = ''
        median = ''
        min = ''
        max = ''
        name = ''
        #写入出售内容
        for i in range(0,numInfo):
            avg = avg + str(round(infos['components'][i]['selling']['avg'], 1)) + '\t'
            median =  median + str(round(infos['components'][i]['selling']['median'], 1)) + '\t'
            max = max + str(round(infos['components'][i]['selling']['max'], 1)) + '\t'
            min = min + str(round(infos['components'][i]['selling']['min'], 1)) + '\t'
            name = name + str(infos['components'][i]['name']) + '\t'
        tempory = tempory + '-' + numInfo*5*'-' + '出售' + numInfo*5*'-' +  '\n部件名称: ' + name + '\n最多出价: ' + median + '\n最大出价: ' + max + '\n最小出价: ' + min + '\n平均出价: ' + avg + '\n------' + numInfo*10*'-'
    else:
        #写入出售内容
        for i in range(0,numInfo):
            tempory = tempory + '\n' + str(infos['components'][i]['name']) + '\t' + str(round(infos['components'][i]['selling']['median'], 1)) + '\t'



def loadDict():
    #载入词库
    path = os.path.dirname(os.path.realpath(__file__))
    file = open(path + "\data.txt", "r")
    itemDirc = [{},{}]
    for lines in file.readlines():
        lines = lines.rstrip("\n")
        linebar = lines.split('=')
        itemDirc[0][linebar[0]] = linebar[1]
        itemDirc[1][linebar[1]] = linebar[0]
    file.close()
    return itemDirc

#翻译函数
def translate(common):
    print(common)
    info = common.split(' ',1)
    global itemDirectionary
    numTry = 0
    empty = True
    while numTry < 2:
        try: 
            name = itemDirectionary[numTry][info[0]]
            empty = False
            numTry = numTry +1
        except:
            numTry = numTry+1
    print(info)
    if empty == True:
        #载入词库
        path = os.path.dirname(os.path.realpath(__file__))
        file = open(path + "\data.txt", "a+")
        #写入词库
        file.write('\n' + info[0] + '=' + info[1])
        #加入字典文件
        itemDirectionary[0][info[0]] = info[1]
        itemDirectionary[1][info[1]] = info[0]
        return '翻译成功(*/ω＼*)小取名更聪明啦'
    else:
        return '写入字典失败(。﹏。*)\n哪里出了问题呢......'
    

#qqbot消息响应函数
def onQQMessage(bot, contact, member, content):
    if contact.qq in blackList:
        print('拦截黑名单')
        return False
    if content in ('help','Help','帮助') and content != '': # and contact.qq == 643489949:
        bot.SendTo(contact, '目前小取名听得懂的话ヽ(✿ﾟ▽ﾟ)ノ：\nhelp, 帮助, c, cd, 翻译, 奸商, 突击, 警报.  \n输入c/cd + 物品名称，小取名会告诉你市场价格的哟(๑•̀ㅂ•́)و✧。\n示例“c 冰队”\n用“翻译 中文 英文”的格式告诉取名，可以帮助取名增加词库丰度哟~。\n示例“翻译 小丑 Mirage Prime”')
    else:
        content = content.split(' ',1 )
    if content[0] == 'cd' or content[0] == 'c' and content != '':
        sendInfo = ''
        if content[0] in ('CD','cd'): 
            detial = True
        if content[0] in ('c','C'): 
            detial = False
        sendInfo = getInfo(content[1], detial)
        if sendInfo == '':  bot.SendTo(contact, 'Σ( ° △ °|||)︴小取名的字典里没有这个物品呢.\n可以使用“翻译 中文 英文”帮助小取名完善词库么(´ｰ∀ｰ`)')
        bot.SendTo(contact, sendInfo)
        global tempory
        tempory ,sendInfo = '' , ''
    if content[0] == '翻译' and content != '':
        bot.SendTo(contact, translate(content[1]))



#载入字典文件
print('loading directionary...')
#itemDirectionary[0]是中>英
#itemDirectionary[1]是英>中
itemDirectionary = loadDict()
print('Verson v.0.0.2\n--Povered by Setname')
#链接API服务器
print('connecting...')
blitz_api = Blitz({
    "api_url": "https://api.nexus-stats.com:443"
})
print('connected...')
tempory = ''
#黑名单
blackList = ['643489949']
#查询
#getInfo('Chilling Globe')
#翻译
#print(translate('小丑p Mirage Prime'))