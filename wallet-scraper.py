import requests
from bs4 import BeautifulSoup
import re

def scrape_bitcoin_addresses(url, headers):
    """
    Scrapes Bitcoin addresses from a given URL using custom headers, focusing on addresses within <td> <a> tags.
    
    Parameters:
    - url: str. The webpage URL to scrape for Bitcoin addresses.
    - headers: dict. Custom request headers for the HTTP request.
    
    Returns:
    - list. A list of unique Bitcoin addresses found on the webpage.
    """
    addresses = []
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all <a> tags that could contain Bitcoin addresses
        a_tags = soup.find_all('a', href=True)
        
        for tag in a_tags:
            # Extract Bitcoin address from the href attribute or the text
            address_from_href = re.search(r'bitcoin/address/([13][a-km-zA-HJ-NP-Z1-9]{25,34})', tag['href'])
            address_from_text = re.search(r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b', tag.text)
            
            if address_from_href:
                addresses.append(address_from_href.group(1))
            elif address_from_text:
                addresses.append(address_from_text.group(0))
                
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Error during scraping: {e}")
    return list(set(addresses))  # Return unique addresses only

def save_addresses_to_file(addresses, filename):
    """
    Saves a list of Bitcoin addresses to a text file, with checks for uniqueness.
    
    Parameters:
    - addresses: list. A list of Bitcoin addresses to be saved.
    - filename: str. The name of the file where addresses will be saved.
    
    Returns:
    None.
    """
    try:
        with open(filename, 'w') as file:
            for address in addresses:
                file.write(address + '\n')
    except Exception as e:
        print(f"Error saving addresses to file: {e}")

if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }

    urls = ["https://bitinfocharts.com/top-100-dormant_2y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_3y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_4y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_5y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_6y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_7y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_8y-bitcoin-addresses.html","https://bitinfocharts.com/top-100-dormant_9y-bitcoin-addresses.html", ]  # Replace with actual URLs
    all_addresses = []

    for url in urls:
        print(f"Scraping {url} for Bitcoin addresses...")
        addresses = scrape_bitcoin_addresses(url, headers)
        all_addresses.extend(addresses)
    
    unique_addresses = list(set(all_addresses))  # Removing duplicates

    save_addresses_to_file(unique_addresses, "bitcoin_addresses.txt")
    print("Scraping completed. Addresses have been saved.")
