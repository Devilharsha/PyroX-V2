import asyncio
import requests
import wget
import yt_dlp
import config
import os

from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from pyrogram import filters
from pyrogram.types import *

from Barath import barath, MODULE
from config import HANDLER, OWNER_ID, BARATH

@barath.on_message(filters.command("video",prefixes=HANDLER) & filters.me)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
