import requests
from bs4 import BeautifulSoup
from player.superplayer import SuperPlayer
import pyppeteer
from pyppeteer import chromium_downloader
import asyncio
from pyppeteer import launch
from player.superplayer import SuperPlayer
import time
import pyttsx3
import random


class GoogleTranslator(SuperPlayer):

    def get_news(self):
        url='http://www.chinadaily.com.cn/'
        res=requests.get(url=url,verify=False)
        soup=BeautifulSoup(res.text,'html.parser')
        a_list=soup.select('a')
        return a_list
    """init page"""
    async def to_page(self):
        self.page=await self.browser.newPage()

        await self.page.setViewport({'width': 1600, 'height': 900})  # 设置页面的大小

        await self.page.goto('http://www.chinadaily.com.cn/')

        # content=await self.page.content()
        #
        # soup=BeautifulSoup(content,'html.parser')
        # print(soup)


    def read_news(self):
        # news=self.get_news()
        #
        # print(news)
        news=self.get_news()
        #输入新闻

        engine = pyttsx3.init()

        for i in range(10000):
            try:
                rand=random.randint(0, len(news)-1)
                text=news[rand].text
                print('read:',text)

                if text!=None and len(text)>0:
                    engine.say(text)
                    engine.runAndWait()
                time.sleep(2)
            except Exception as e:
                print(e)


    async def test(self):
        print("test")
if __name__=="__main__":

    translator=GoogleTranslator()
    asyncio.get_event_loop().run_until_complete(translator.to_page())
    translator.read_news()

