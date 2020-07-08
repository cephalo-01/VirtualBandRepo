from player.drone import DroneModular
from player.googletranslator import GoogleTranslator
from player.sequencer import DrumSequencer
from player.keyboard import KeyBoardPlayer
import pyppeteer
from pyppeteer import chromium_downloader
import asyncio
from pyppeteer import launch
from player.superplayer import SuperPlayer

#keyboard
keyboard = KeyBoardPlayer()
asyncio.get_event_loop().run_until_complete(keyboard.to_page())


#drone
modular = DroneModular()
asyncio.get_event_loop().run_until_complete(modular.to_page())
asyncio.get_event_loop().run_until_complete(modular.play())









#news_reader

translator = GoogleTranslator()
asyncio.get_event_loop().run_until_complete(translator.to_page())
translator.read_news()

#DrumSequencer

drum = DrumSequencer()
asyncio.get_event_loop().run_until_complete(drum.to_page())
asyncio.get_event_loop().run_until_complete(drum.play())