import pyppeteer
from pyppeteer import chromium_downloader
import asyncio
from pyppeteer import launch
from player.superplayer import SuperPlayer
import time
"""drum sequencer"""


class DrumSequencer(SuperPlayer):

    """play method"""
    async def play(self):
        #click play btn
        playButton = await self.page.querySelector('#playButton')
        await playButton.click()
    """stop method"""
    async def stop(self):
        #click play btn
        stopButton = await self.page.querySelector('#stopButton')
        await stopButton.click()
    """speed adjust"""
    async def speed(self):
        #click play btn
        speed = await self.page.querySelector('#playbackSpeed')
        await speed.type(75)



    kick_list=[0,6,12]
    snare_list = [5, 9]
    hat_list = [0, 6, 9,12,14]

    """init page"""
    async def to_page(self):
        self.page=page=await self.browser.newPage()
        await self.page.setViewport({'width': 1600, 'height':900})  # 设置页面的大小

        await self.page.goto('http://www.disco-computer.com/synthesizer/synth.html?saveAs=asdaeaed')

        #开始编写sequence
        for k in self.kick_list:
            kickbtn=await page.querySelector('#kick'+str(k))
            await kickbtn.click()

        for s in self.snare_list:
            snarebtn=await page.querySelector('#clap'+str(s))
            await snarebtn.click()

        for h in self.hat_list:
            hatbtn=await page.querySelector('#hat'+str(h))
            await hatbtn.click()

    """clear drum"""
    async def clear_drum(self):
        #clear pattern
        for k in self.kick_list:
            kickbtn=await self.page.querySelector('#kick'+str(k))
            await kickbtn.click()
    """clear snare"""
    async def clear_snare(self):
        for s in self.snare_list:
            snarebtn=await self.page.querySelector('#clap'+str(s))
            await snarebtn.click()
    """clear hihat"""
    async def clear_hihat(self):
        for h in self.hat_list:
            hatbtn=await self.page.querySelector('#hat'+str(h))
            await hatbtn.click()
    """clear all pattern"""
    async def clear(self):
        self.clear_drum()
        self.clear_snare()
        self.clear_hihat()





if __name__=="__main__":

    drum=DrumSequencer()
    asyncio.get_event_loop().run_until_complete(drum.to_page())
    asyncio.get_event_loop().run_until_complete(drum.play())
    asyncio.get_event_loop().run_until_complete(drum.speed())

    # time.sleep(10)
    # asyncio.get_event_loop().run_until_complete(drum.stop())

    # asyncio.get_event_loop().run_until_complete(drum.clear_drum())

