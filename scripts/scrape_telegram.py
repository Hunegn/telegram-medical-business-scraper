from telethon.sync import TelegramClient
import pandas as pd
import os

# Your Telegram API credentials (replace with your own)
API_ID = "29979615"
API_HASH = "aad1c5a822b70173273b05fca6eda0a0"
SESSION_NAME = "telegram_scraper"

# List of Telegram channels to scrape
CHANNELS = [
    "https://t.me/DoctorsET",
    "https://t.me/lobelia4cosmetics",
    "https://t.me/yetenaweg",
    "https://t.me/EAHCI"
]

# Output directory
OUTPUT_DIR = "../data/telegram"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to scrape messages from a Telegram channel
def scrape_channel(client, channel, limit=500):
    messages = []
    print(f"Scraping messages from {channel}...")
    
    for message in client.iter_messages(channel, limit=limit):
        messages.append({
            "channel": channel,
            "message_id": message.id,
            "date": message.date,
            "text": message.text,
            "views": message.views,
            "forwards": message.forwards,
        })
    
    return messages

# Main function to run the scraper
def main():
    with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        all_messages = []
        
        for channel in CHANNELS:
            try:
                messages = scrape_channel(client, channel)
                all_messages.extend(messages)
            except Exception as e:
                print(f"Error scraping {channel}: {e}")
        
        # Save messages to CSV
        df = pd.DataFrame(all_messages)
        output_file = os.path.join(OUTPUT_DIR, "telegram_messages.csv")
        df.to_csv(output_file, index=False)
        print(f"Scraping completed! Data saved to {output_file}")

if __name__ == "__main__":
    main()
