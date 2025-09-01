Web Page Title Scraper
This is a simple Python command-line utility for scraping the title of a given webpage. It handles user input for the URL and the output file, and includes basic error handling for common issues like network errors or invalid URLs. The script also saves a record of the scrape, including the URL, title, and timestamp.

Features
Scrapes the title from any public webpage.

Prompts the user for a URL and a custom output filename.

Automatically handles adding https:// if a protocol is not provided.

Records the scraped title, URL, and timestamp in a text file.

Provides an option to view previous scrape results.

Requirements
This script requires the following Python libraries:

requests for making HTTP requests.

beautifulsoup4 for parsing the HTML content.

Installation
You can install the required libraries using pip:

pip install requests beautifulsoup4

How to Run
Save the script as web_scraper.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script using the Python interpreter:

python web_scraper.py

The script will present a menu with options to scrape a new page, view previous results, or exit.