from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Configure Selenium to use Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Path to your chromedriver
service = Service(executable_path='chromedriver.exe')

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the base URL
base_url = "https://www.dripcapital.com/hts-code/"

# Initialize an empty list to store data
data = []

# Loop over sections
for section in range(1, 100):
    section_str = str(section).rjust(2, '0')
    section_url = base_url + section_str
    print(f"Scraping Chapters of Section {section_str} from URL: {section_url}")
    driver.get(section_url)

    # Wait for the chapters to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, f"//a[contains(@href, '/hts-code/{section_str}/')]")
            )
        )
    except Exception as e:
        print(f"Error loading section page {section_url}: {e}")
        continue

    # Extract chapter numbers from links
    chapter_links = driver.find_elements(
        By.XPATH, f"//a[contains(@href, '/hts-code/{section_str}/')]"
    )
    chapter_numbers = set()
    for link in chapter_links:
        href = link.get_attribute('href')
        parts = href.strip('/').split('/')
        if len(parts) >= 5 and parts[-1].isdigit():
            chapter_numbers.add(parts[-1])

    # Loop over chapters
    for chapter in sorted(chapter_numbers):
        chapter_str = str(chapter).rjust(2, '0')
        chapter_url = f"{base_url}{section_str}/{chapter_str}"
        print(
            f"Scraping Parts and Subparts of Section: {section_str}, Chapter: {chapter_str} from URL: {chapter_url}"
        )
        driver.get(chapter_url)

        # Wait for the content to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5']")
                )
            )
        except Exception as e:
            print(f"Error loading chapter page {chapter_url}: {e}")
            continue

        # Extract HTS codes and descriptions
        h5_elements = driver.find_elements(
            By.XPATH, "//h5[@class='MuiTypography-root MuiTypography-h5']"
        )
        if not h5_elements:
            print(f"No items found on {chapter_url}")
            continue

        for h5 in h5_elements:
            try:
                parent_element = h5.find_element(By.XPATH, "..")
                text = parent_element.text.strip()
                lines = text.split('\n')

                if len(lines) >= 2:
                    #hts_code = lines[0].strip()
                    #Remove the prefix 'HTS Code' fro every row
                    hts_code = lines[0].replace('HTS Code ', '').strip()
                    description = ' '.join(lines[1:]).strip()
                    data.append({'HTS code': hts_code, 'Description': description})
                else:
                    print(f"Unexpected format at {chapter_url}: {text}")
            except Exception as e:
                print(f"Error extracting data from item on {chapter_url}: {e}")

        print("\n")  # Add a newline for better readability between chapters

# Close the browser
driver.quit()

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('hts_codes_WebScrapped.csv', index=False)

print("Data has been saved to hts_codes_WebScrapped.csv")