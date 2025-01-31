import os
import asyncio
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto

# Your Telegram API credentials (Replace with actual values)
API_ID = "29979615"
API_HASH = "aad1c5a822b70173273b05fca6eda0a0"

# Channels to scrape images from
CHANNELS = {
    "Chemed": "https://t.me/Chemed",
    "Lobelia4Cosmetics": "https://t.me/lobelia4cosmetics",
}

# Directory to save images
OUTPUT_FOLDER = "data/telegram/images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

async def scrape_images():
    async with TelegramClient("telegram_scraper", API_ID, API_HASH) as client:
        for channel_name, channel_url in CHANNELS.items():
            print(f"📸 Scraping images from {channel_name}...")

            # Create a folder for each channel
            channel_folder = os.path.join(OUTPUT_FOLDER, channel_name)
            os.makedirs(channel_folder, exist_ok=True)

            messages = await client.get_messages(channel_url, limit=2000)  # Scan 2000 messages
            image_count = 0

            for msg in messages:
                if msg.media and isinstance(msg.media, MessageMediaPhoto):
                    image_count += 1
                    file_path = os.path.join(channel_folder, f"{channel_name}_{image_count}.jpg")
                    await client.download_media(msg.media, file_path)

            print(f"✅ Downloaded {image_count} images from {channel_name}")

if __name__ == "__main__":
    asyncio.run(scrape_images())
