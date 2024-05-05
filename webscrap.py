from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape Google Places
def scrape_google_places(query):
    service = Service("./chromedriver")  # Path to your chromedriver
    service.start()
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com/maps")

    search_box = driver.find_element_by_css_selector("input[aria-label='Search Google Maps']")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    # Wait for results to load
    driver.implicitly_wait(5)

    # Extract information
    results = []
    for item in driver.find_elements_by_class_name("section-result"):
        name = item.find_element_by_class_name("section-result-title").text
        address = item.find_element_by_class_name("section-result-location").text
        rating = item.find_element_by_css_selector("span[aria-label^='Rated']").get_attribute('aria-label')
        results.append({'Name': name, 'Address': address, 'Rating': rating})

    driver.quit()
    return results

# Function to scrape TripAdvisor
def scrape_tripadvisor(query):
    url = f"https://www.tripadvisor.com/Search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for item in soup.find_all('div', class_='result-title'):
        name = item.text.strip()
        try:
            print(item)
            rating = item.find_next('span', class_='ui_bubble_rating')['alt']
            print(rating)
        except:
            rating = "N/A"
        results.append({'Name': name, 'Rating': rating})

    return results

# Main function
def main():
    query = input("Enter location query: ")

    # Scrape Google Places
    # google_results = scrape_google_places(query)
    # google_df = pd.DataFrame(google_results)

    # Scrape TripAdvisor
    tripadvisor_results = scrape_tripadvisor(query)
    tripadvisor_df = pd.DataFrame(tripadvisor_results)

    # Combine both datasets
    # combined_df = pd.merge(google_df, tripadvisor_df, on='Name', how='outer')

    # Save dataset to CSV
    combined_df.to_csv('scraped_data.csv', index=False)
    print("Dataset saved as 'scraped_data.csv'")

if __name__ == "__main__":
    main()
