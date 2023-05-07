from telethon import TelegramClient, events, types
from dotenv import load_dotenv
import os

load_dotenv()

# Your API credentials
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
session_name = os.getenv('SESSION_NAME')

phone_number = os.getenv('PHONE_NUMBER')
forward_to = os.getenv('FORWARD_TO')
watch_channel = os.getenv('WATCH_CHANNEL')

texts_to_detect = os.getenv('TEXTS_TO_DETECT').split(',')

async def list_groups():
    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            print(f'{dialog.id} - {dialog.name}')

async def handle_new_message(event):
    entityForward = await client.get_input_entity(int(forward_to))
    message_text = event.message.message.lower()
    if event.message.media:
        # Create a new folder named 'temp'
        if not os.path.exists('temp'):
            os.makedirs('temp')
        print('Media detected!')
        if isinstance(event.message.media, types.MessageMediaPhoto):
            print('Photo detected!')
            caption = event.message.message or ''
            photo = await event.download_media('temp/')
            await client.send_file(entityForward, photo, caption=caption)
        elif isinstance(event.message.media, types.MessageMediaDocument):
            print('Document detected!')
            document = await event.download_media('temp/')
            await client.send_file(entityForward, document, caption=event.message.message)
    elif any(text in message_text for text in texts_to_detect):
        sender = await event.get_sender()
        # sender_username = sender.username or sender.phone or sender.first_name
        await client.send_message(entityForward, f'{event.message.message}')

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Enter the code: '))
    entityWatch = await client.get_input_entity(int(watch_channel))
    client.add_event_handler(handle_new_message, events.NewMessage(entityWatch))
    await client.start()
    await list_groups()
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
