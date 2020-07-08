import pyppeteer
from pyppeteer import chromium_downloader
import asyncio
from pyppeteer import launch
from player.superplayer import SuperPlayer
import time
"""drum sequencer"""


class KeyBoardPlayer(SuperPlayer):

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



    kick_list=[0,6,12]

    """init page"""
    async def to_page(self):
        self.page=page=await self.browser.newPage()
        await self.page.setViewport({'width': 1920, 'height':1000})  # 设置页面的大小

        await self.page.goto('https://www.musicca.com/piano')

        #开始演奏
        white_keys=await self.page.xpath("//span[@class='white-key']")
        black_keys=await self.page.xpath("//span[@class='black-key']")


        # chords=[[2,4],[7,9]]
        # for i in range(10000000):
        #     chord=chords[i%2]
        #     for c in chord:
        #         await white_keys[c].click()
        #         await black_keys[c].click()

        for i in range(10000000):
             await white_keys[-1:][0].click()
             time.sleep(0.2)
             await white_keys[-1:][0].click()
             time.sleep(0.2)
             # await white_keys[-1:][0].click()
             time.sleep(0.1)
             await black_keys[-1:][0].click()
             time.sleep(4)
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

    keyboard=KeyBoardPlayer()
    asyncio.get_event_loop().run_until_complete(keyboard.to_page())
    # asyncio.get_event_loop().run_until_complete(drum.play())

    # time.sleep(10)
    # asyncio.get_event_loop().run_until_complete(drum.stop())

    # asyncio.get_event_loop().run_until_complete(drum.clear_drum())

