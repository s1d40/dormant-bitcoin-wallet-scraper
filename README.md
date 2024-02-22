# Dormant Bitcoin Wallet Scraper

## Project Overview
This Python script scrapes dormant Bitcoin wallet addresses from various pages on https://bitinfocharts.com/. It is designed to collect data on Bitcoin addresses that have not had any transactions over specific periods, ranging from 2 to 9 years. This information can be crucial for analysts, investors, and researchers interested in the cryptocurrency market's dormant assets.

## Features
- Scrapes multiple pages for dormant Bitcoin wallet addresses.
- Uses BeautifulSoup and requests libraries for web scraping.
- Filters and collects unique Bitcoin addresses.
- Saves the scraped addresses to a text file for easy access and analysis.

## Installation

### Prerequisites
- Python 3.x
- BeautifulSoup4
- Requests

You can install the required packages using pip:

pip install beautifulsoup4 requests

Clone the Repository

First, clone this repository to your local machine using the following command:

git clone https://github.com/s1d40/dormant-bitcoin-wallet-scraper.git

cd dormant-bitcoin-wallet-scraper

python wallet-scraper.py

This will start the scraping process, and the script will print out the URLs it is scraping. Once completed, it will save the unique Bitcoin addresses to bitcoin_addresses.txt in the project directory.


*Note: This is a very simple script that works only on tables from https://bitinfocharts.com/top-100-dormant_9y-bitcoin-addresses.html, it will scrape from 2y to 9y. You might need to edit the script for it to work on other websites.

Contributing

Feel free to fork the project and submit pull requests. If you find any issues or have suggestions for improvement, please open an issue in the repository.

License

This project is open source and available under the MIT License.
