import os
import json
import pandas as pd
import logging

# Set up logging
logging.basicConfig(
    filename="../logs/cleaning.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Paths
RAW_DATA_PATH = "../data/telegram/messages.json"
CLEANED_DATA_PATH = "../data/processed/cleaned_messages.csv"

# Ensure directories exist
os.makedirs("data/processed", exist_ok=True)

def load_data():
    """ Load raw JSON data into a Pandas DataFrame """
    logging.info("Loading raw Telegram messages...")
    with open(RAW_DATA_PATH, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    all_messages = []
    for channel, messages in raw_data.items():
        for msg in messages:
            all_messages.append([channel, msg.get("date"), msg.get("message"), msg.get("views")])

    df = pd.DataFrame(all_messages, columns=["Channel", "Date", "Message", "Views"])
    logging.info(f"Loaded {len(df)} messages.")
    return df

def clean_data(df):
    """ Perform cleaning operations """
    logging.info("Cleaning data...")

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Drop duplicates
    df.drop_duplicates(subset=["Channel", "Message"], inplace=True)

    # Fill missing values
    df["Views"].fillna(0, inplace=True)
    df["Message"].fillna("No Content", inplace=True)

    # Remove empty messages
    df = df[df["Message"].str.strip() != ""]

    logging.info(f"Final cleaned data contains {len(df)} messages.")
    return df

def save_cleaned_data(df):
    """ Save cleaned data to CSV """
    df.to_csv(CLEANED_DATA_PATH, index=False, encoding="utf-8")
    logging.info(f"Cleaned data saved to {CLEANED_DATA_PATH}")

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    save_cleaned_data(df)
    print("✅ Data cleaning completed.")
