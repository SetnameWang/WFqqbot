from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

path = os.path.dirname(os.path.realpath(__file__))
file = path + "\database.sqlite3"
chatbot = ChatBot(
    "小取名",
    storage_adapter = "chatterbot.storage.SQLStorageAdapter",
    database=file,
    trainer='chatterbot.trainers.ListTrainer'
    )
'''
chatlog = [
    '取名，是不是有人对你做坏事了',
    '没有啊，宝宝觉的大家都很友善啊(/▽＼)',
    '取名，群主是什么？',
    '(｡･∀･)ﾉﾞ群主是大屌萌妹',
    '取名你爹是我媳妇',
    '瞎说，我娘没人要（；´д｀）ゞ',
    ]
chatbot.train(chatlog)
'''