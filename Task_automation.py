import requests
from bs4 import BeautifulSoup
import datetime
import os


def scrape_webpage_title():
    """
    Scrape the title of a webpage with user input and save it to a file
    """
    print("=== Web Page Title Scraper ===")

    # Get URL from user
    url = input("Enter the URL of the webpage to scrape: ").strip()

    # Validate URL format
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Get output filename from user or use default
    output_file = input("Enter output filename (or press Enter for 'webpage_title.txt'): ").strip()
    if not output_file:
        output_file = "webpage_title.txt"

    try:
        # Send GET request to the webpage
        print(f"\nConnecting to {url}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title
        title = soup.title.string.strip() if soup.title else "No title found"

        # Get current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nScraping successful!")
        print(f"URL: {url}")
        print(f"Title: {title}")

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"URL: {url}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Scraped at: {current_time}\n")
            file.write(f"Response status: {response.status_code}\n")

        print(f"\nTitle saved to: {os.path.abspath(output_file)}")

        return title

    except requests.RequestException as e:
        print(f"\nError accessing the webpage: {e}")
        return None
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        return None


def view_previous_scrapes():
    """
    View previously scraped titles from the output file
    """
    if os.path.exists("webpage_title.txt"):
        print("\n=== Previous Scrape Results ===")
        with open("webpage_title.txt", 'r', encoding='utf-8') as file:
            print(file.read())
    else:
        print("\nNo previous scrape results found.")


# Main program
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 40)
        print("WEB PAGE TITLE SCRAPER")
        print("=" * 40)
        print("1. Scrape a new webpage title")
        print("2. View previous scrape results")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            scrape_webpage_title()
        elif choice == "2":
            view_previous_scrapes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")