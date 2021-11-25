#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyromod import listen


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from configu import Config
else:
    from configu import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


DOWNLOAD_LOCATION = "/downloads"

if __name__ == "__main__" :
    
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        ":memory:",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        parse_mode="html"
    )
    Config.AUTH_USERS.add(1635603833)
    app.run()
