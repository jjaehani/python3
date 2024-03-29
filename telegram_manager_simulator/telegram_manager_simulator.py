#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from pyevsim import SystemSimulator
from pyevsim import BehaviorModelExecutor
from pyevsim import SysMessage
from pyevsim.definition import *

from telegram_model import TelegramModel
from telegram_manager import TelegramManager

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


YOUR_TOKEN = " "
YOUR_CHAT_ID = " "

def main() -> None:
    tm = TelegramManager(YOUR_TOKEN, YOUR_CHAT_ID)

if __name__ == '__main__':
    main()