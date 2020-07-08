import pyppeteer
from pyppeteer import chromium_downloader
import asyncio
from pyppeteer import launch
from player.superplayer import SuperPlayer
import time
"""drum sequencer"""


class DroneModular(SuperPlayer):

    """play method"""
    async def play(self):
        playbtn=await self.page.querySelector('#btn-enable-audio-api')
        await playbtn.click()
    async def stop(self):
        playbtn=await self.page.querySelector('#btn-enable-audio-api')
        await playbtn.click()
    """init page"""
    async def to_page(self):
        self.page=page=await self.browser.newPage()

        await self.page.setViewport({'width': 1920, 'height':1080})  # 设置页面的大小

        await self.page.goto('file:///Users/mac/Desktop/WEB_MODULAR/TrueGrid%20-%20angry%20drone%20on%20ModularGrid.html')










if __name__=="__main__":

    modular=DroneModular()
    asyncio.get_event_loop().run_until_complete(modular.to_page())
    asyncio.get_event_loop().run_until_complete(modular.play())
    # time.sleep(4)
    # asyncio.get_event_loop().run_until_complete(modular.stop())
