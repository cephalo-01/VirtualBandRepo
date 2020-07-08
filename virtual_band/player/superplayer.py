import pyppeteer
from pyppeteer import chromium_downloader
import asyncio
from pyppeteer import launch
import pyttsx3



class SuperPlayer():
    """basic player class"""

    def __init__(self,**para):
        asyncio.get_event_loop().run_until_complete(self.init_browser())

    async def init_browser(self):
        """init chrome browser"""
        self.browser = await launch(
            {'headless': False,'autoClose':False,'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})
        # self.browser = await launch(
        #     {'headless': False,'autoClose':False,'dumpio':True,'executablePath':'/Users/mac/Library/Application Support/pyppeteer/chrome-mac/Chromium.app','args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox']})

if __name__=="__main__":
    player=SuperPlayer()
