from wxpy import *

#扫码登录
bot = Bot()

#初始化图灵机器人（api_key 申请：http://www.turingapi.com/）
tuling = Tuling(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxx')

#自动回复所有文字消息
@bot.register()

def auto_reply_all(msg):
    #tuling.do_reply(msg) #自动回复所有文字信息
    print("接收："+str(msg))
    s=input("请输入内容：")
    msg.reply("在忙！稍等")
    msg.reply_image('jerry.png')

#开始运行
bot.join()
