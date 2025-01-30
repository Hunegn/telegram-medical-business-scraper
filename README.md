# Ethiopian Medical Business Data Scraper

## Project Overview

This project focuses on scraping and analyzing data from Ethiopian medical business-related Telegram channels. The extracted data will be used to build a data warehouse, conduct object detection on images, and expose the data through a FastAPI service.

## Features

- **Telegram Scraping:** Extract data from various Ethiopian medical business Telegram channels.
- **Image Scraping & Processing:** Collect and preprocess images for object detection.
- **Data Cleaning & Transformation:** Process extracted data into structured formats.
- **Data Warehouse:** Store and manage the cleaned data efficiently.
- **API Integration:** Serve the data through a FastAPI-based REST API.

## Data Sources

We will scrape data from the following Telegram channels:

- [DoctorsET](https://t.me/DoctorsET)
- [Chemed Telegram Channel](https://t.me/lobelia4cosmetics)
- [Yetenaweg](https://t.me/yetenaweg)
- [EAHCI](https://t.me/EAHCI)
- Additional sources from [et.tgstat.com](https://et.tgstat.com/medicine)

## Folder Structure

```plaintext
Ethiopian-Medical-Data-Scraper/
│-- data/                        # Raw and processed data storage
│   ├── raw/                     # Unprocessed scraped data
│   ├── processed/               # Cleaned and transformed data
│   ├── images/                  # Downloaded images
│   ├── database/                # Data warehouse (SQLite/PostgreSQL)
│
│-- scripts/                     # Python scripts for various tasks
│   ├── telegram_scraper.py       # Extracts data from Telegram channels
│   ├── image_scraper.py          # Scrapes images from Telegram
│   ├── data_cleaning.py          # Cleans and structures the scraped data
│   ├── object_detection.py       # Applies object detection models on images
│   ├── data_warehouse.py         # Manages the structured data warehouse
│   ├── api_service.py            # FastAPI service to expose the data
│
│-- models/                       # Object detection models
│-- notebooks/                    # Jupyter notebooks for data exploration & analysis
│-- logs/                         # Logging for tracking execution & errors
│-- requirements.txt              # Dependencies list
│-- README.md                     # Project documentation
```

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Hunegn/telegram-medical-business-scraper.git
   cd telegram-medical-business-scraper
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Telegram API credentials**

   - Obtain API credentials from [my.telegram.org](https://my.telegram.org/)
   - Store API credentials in a `.env` file:
     ```plaintext
     TELEGRAM_API_ID=your_api_id
     TELEGRAM_API_HASH=your_api_hash
     TELEGRAM_BOT_TOKEN=your_bot_token
     ```

5. **Run the Telegram scraper**

   ```bash
   python scripts/telegram_scraper.py
   ```

6. **Process and clean the data**

   ```bash
   python scripts/data_cleaning.py
   ```

7. **Run object detection on images**

   ```bash
   python scripts/object_detection.py
   ```

8. **Launch the API service**

   ```bash
   uvicorn scripts.api_service:app --reload
   ```

## Future Enhancements

- Implement NLP techniques to analyze medical discussions.
- Improve object detection models for more accurate image analysis.
- Develop a web-based dashboard for interactive data visualization.

## Contributors

- **[Your Name]** – Developer & Data Engineer

## License

This project is licensed under the MIT License.

