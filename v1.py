'''
Created on 5 окт. 2021 г.

@author: burun
'''
import telepot
import schedule
import time
token = '2077637098:AAEsdjpcXJ-Bcin4qebi7UjLFhl-yKwf39g'
bot = telepot.Bot(token)
img = 'https://vk.com/zhuravsk?z=photo179191197_456239446%2Fphotos179191197' 
text= 'darova'
def qq():
        bot.sendMessage(503971041, 'qq')
        bot.sendPhoto(503971041, f'{img}')
schedule.every(10).seconds.do(qq)
while True:
    schedule.run_pending()
    time.sleep(1)
    

