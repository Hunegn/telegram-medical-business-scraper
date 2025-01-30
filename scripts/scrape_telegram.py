import os
import json
import logging
import asyncio
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto

# Set up logging
logging.basicConfig(
    filename="../logs/scraping.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Telegram API credentials (Replace with actual values)
API_ID = "29979615"
API_HASH = "aad1c5a822b70173273b05fca6eda0a0"

# Telegram channels to scrape
CHANNELS = {
    "DoctorsET": "https://t.me/DoctorsET",
    "Chemed": "https://t.me/CheMed123",
    "Lobelia4Cosmetics": "https://t.me/lobelia4cosmetics",
    "YetenaWeg": "https://t.me/yetenaweg",
    "EAHCI": "https://t.me/EAHCI",
}

# Storage paths
DATA_FOLDER = "data/telegram"
TEXT_DATA_PATH = os.path.join(DATA_FOLDER, "messages.json")
IMAGE_FOLDER = os.path.join(DATA_FOLDER, "images")

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(IMAGE_FOLDER, exist_ok=True)

async def scrape_telegram():
    async with TelegramClient("telegram_scraper", API_ID, API_HASH) as client:
        scraped_data = {}

        for channel_name, channel_url in CHANNELS.items():
            print(f"🔄 Scraping messages from {channel_name}...")
            logging.info(f"Scraping messages from {channel_name}")

            messages = await client.get_messages(channel_url, limit=2000)  # Scan 2000 messages
            channel_data = []

            for msg in messages:
                msg_data = {
                    "date": str(msg.date),
                    "message": msg.message,
                    "views": msg.views if msg.views else None
                }
                channel_data.append(msg_data)

                # Download images
                if msg.media and isinstance(msg.media, MessageMediaPhoto):
                    img_folder = os.path.join(IMAGE_FOLDER, channel_name)
                    os.makedirs(img_folder, exist_ok=True)
                    img_path = os.path.join(img_folder, f"{channel_name}_{msg.id}.jpg")
                    await client.download_media(msg.media, img_path)

            scraped_data[channel_name] = channel_data

        # Save text data as JSON
        with open(TEXT_DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(scraped_data, f, indent=4)

        print("✅ Scraping completed. Data saved successfully!")

if __name__ == "__main__":
    asyncio.run(scrape_telegram())
