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

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import json

def onQQMessage(bot, contact, member, content):
    if contact.qq in blackList:
        print('拦截黑名单')
        return False
    if '取名' in content and not bot.isMe(contact, member):
        bot.SendTo(contact, str(chatbot.get_response(content)))
        if content[0] == '[' and content[len(content)-1] == ']':
            global chatlog
            try:
                list = content[1:len(content)-1]
                print(list)
                list = list.split('/')
                print(list)
                chatlog = chatlog + list
            except:
                pass
            if len(chatlog) > 10 :
                chatbot.train(chatlog)
                path = os.path.dirname(os.path.realpath(__file__))
                file = open(path + "\database.sqlite3",'a+')
                file.write('\n' + json.dumps(chatlog))
                chatlog = []
            print(chatlog)


chatlog = []
path = os.path.dirname(os.path.realpath(__file__))
file = path + "\database.sqlite3"
chatbot = ChatBot(
    "小取名",
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    database=file,
    trainer='chatterbot.trainers.ListTrainer'
    )
#黑名单
blackList = ['643489949']
'''
chatlog = [
    '取名你好呀',
    '你好呀(๑•̀ㅂ•́)و✧',
    '取名你多大了？',
    '本宝宝今年才出生哟(｡･∀･)ﾉﾞ',
    '取名，mua',
    '噫，脏脏我不要亲亲Σ( ° △ °|||)︴',
    '取名我要抱抱',
    '╰(*°▽°*)╯好好好抱你一下，多大人了真是',
    '取名你有男朋友了嘛？',
    '机器人怎么有男朋友哟，你484撒o(*≧▽≦)ツ┏━┓',
    '取名我当你男朋友好不好啊',
    'o(≧口≦)o我我我，你你你。。。',
    '取名今天天气真好',
    '是啊太阳那么大适合睡觉┑(￣Д ￣)┍',
    '取名你再干什么啊？',
    '我是机器人欸，你不找我我当然在发呆啦(；′⌒`)',
    '取名我们私奔吧',
    '好呀你给我买服务器~',
    ]
chatbot.train(chatlog)
'''
