from tsup.youtube.youtube_upload import YoutubeUpload
from datetime import datetime, date, timedelta
import asyncio
from tsup.utils.webdriver.setupPL import checkRequirments
import os


channel_cookie_path = r"/home/lz/Documents/tiktoka-studio-uploader/HowToPronounce-cookie.json"

videopath = r"/home/lz/Documents/tiktoka-studio-uploader/offline.mp4"
tags = ["pronounce","pronunciation","english","stephanie"]
playlist = "Pronunciation of Top 10000 Google Words"
# if you use some kinda of proxy to access youtube,
proxy_option = ""

# for cookie issue,
title = "How to Pronounce offline in American English and British English"
username = "linzhoulxyz@gmail.com"
password = "U437P8Is9prmNquVerHJ9%R00bn"
description = """Learn how to say commented with HowToPronounce Free Pronunciation Tutorials.
Definition and meaning can be found here: 

https://www.google.com/search?q=define+commented


This video shows you how to pronounce commented correctly in American English and British English.
SUBSCRIBE for how to pronounce more https://bit.ly/3FAgWoK
WATCH MORE videos here: https://bit.ly/3FAgWoK"""


wait = 0
# 0-wait uploading done
# 1-wait Processing done
# 2-wait Checking done


# auto install requirments for user
# checkRequirments()
upload = YoutubeUpload(
    # use r"" for paths, this will not give formatting errors e.g. "\n"
    root_profile_directory="",
    proxy_option=proxy_option,
    is_open_browser=True,
    debug=True,
    use_stealth_js=False,
    # if you want to silent background running, set watcheveryuploadstep false
    channel_cookie_path=channel_cookie_path,
    username=username,
    browser_type="firefox",
    wait_policy="go next after uploading success",
    password=password,
    is_record_video=True
    # for test purpose we need to check the video step by step ,
)
today = date.today()
def checkfilebroken(path):
    print(f"check whether file exist{path}")
    if (os.path.exists(path)
        and os.path.getsize(path) > 0
    ):
        print(f'{path} is exist')
        return True
    else:
        print(f'{path} is not  exist')
        
        return False

def instantpublish():
    asyncio.run(
        upload.upload(
            video_path=videopath,
            title=title,
            description=description,
            tags=tags,
            playlist=playlist,
            publish_policy=1,
        )
    )


checkfilebroken(channel_cookie_path)
checkfilebroken(videopath)
instantpublish()
