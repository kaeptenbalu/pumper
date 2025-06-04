# Binance Telegram Pump Bot

## Overview
**Please note that this bot is not intended for production use and should be used with caution.**


This is a fun project designed to automate the process of participating in cryptocurrency pump groups on Telegram. The bot will monitor messages from a specified pump group and execute trades on Binance based on the messages it receives. 

## Prerequisites

Before you start, ensure you have the following:

1. **Python 3** installed on your machine.
2. **tforwarder app** installed on your smartphone to forward messages from the pump group to the bot.
3. A **Binance API token**. You can create one by following the instructions [here](https://www.binance.com/en-NG/support/faq/360002502072).
4. A Telegram bot created. You can follow the guide [here](https://statisquo.de/2020/08/21/telegram-bot-bauen-in-10-minuten-mit-python/).

## Setup Instructions

1. **Create Binance API Token:**
   - Go to the Binance API management page and create a new API key.
   - Save your API token and secret in a text file named `binance_credentials.txt`.

2. **Create Telegram Bot:**
   - Create a new bot using BotFather on Telegram.
   - Save your bot token in a text file named `token.txt`.

3. **Install tforwarder:**
   - Download and install the tforwarder app on your smartphone.
   - Set it up to forward messages from the pump group to your Telegram bot.

4. **Configure the Pump Script:**
   - Open the `pump3000.py` script.
   - Change line 75 to adjust the percentage of BTC to pump (default is set to 10% or 0.1).

## Running the Bot

1. Start the bot a few minutes before the scheduled pump.
2. Ensure that the bot is only allowed to send messages to itself.
3. Run the `pump3000.py` script.

### Important Notes

- The bot will only act on messages that start with `#`. Ensure that the pump group follows this format.
- Use this bot at your own risk. Cryptocurrency trading involves significant risk, and you should only trade with money you can afford to lose.

## Disclaimer

This project is intended for educational and entertainment purposes only. It is not designed for production use and should be used with caution. Always do your own research before engaging in cryptocurrency trading.

## Good Luck!

Happy pumping! 🚀




 



