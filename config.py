"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", None) or "4324828"
        self.API_HASH: str = os.environ.get("API_HASH", None) or "ff4db0d67b7788634bde213e3ce96e72"
        self.SESSION: str = os.environ.get("PYROGRAM_SESSION", None) or "BQBQ4wEq3naWuiRQU41HMbam47RMTr078H636csUUf8DaFTNBAat_WpxkIC10J2QTSkkmjvJLUGEnybmg-g3y62-2YKB7PutbvGinT6eJ4QQcUyoQbO2udsakafa6bu8c5mZ4Be53G1oyDZpiYIT5wxuBW4-ESyr9mBwAV-PhHuW5GSacUiu6p9emfo71EvFTkDxCTfSDXxLc0D6NLkKE7GrXmCO048nd0R97oeXYXwa9qqktNFlg0ZRoTVvB8uoTwCNlGpA_CWxqmOPTj402pS0k6PJvTrk0TCd2-0I0XwcTT6qvj2wF1W57VXctU980tcRAZsK5J2n9LYe1SlLR9qTfOktWAA"
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "2082798662").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
