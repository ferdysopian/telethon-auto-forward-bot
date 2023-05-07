# Telethon Auto Forward Bot

A simple chatbot that uses the Telethon library to automatically forward messages from a watched Telegram channel to a designated group or person. It also supports detecting certain keywords and forwarding those messages as well.

## How to Run

1. Clone the repository to your local machine.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Add your Telegram API credentials and other settings to the `.env` file.
4. Run the chatbot by executing `python main.py`.
5. The chatbot will start listening for messages in the watched channel and forwarding them to the designated account, group, or channel.

## Requirements

The following Python packages are required to run the chatbot:

- telethon==1.23.0
- python-dotenv==0.17.0

These packages are listed in the `requirements.txt` file and can be installed by running `pip install -r requirements.txt`.

## Credits

- [Telethon](https://github.com/LonamiWebs/Telethon): A Python 3 MTProto library to interact with Telegram's API as a user or through a bot account.
- [python-dotenv](https://github.com/theskumar/python-dotenv): A zero-dependency module that loads environment variables from a .env file.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
