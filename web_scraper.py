import requests
from bs4 import BeautifulSoup

# Target URL - You can replace this with any other news website
URL = "https://www.bbc.com/news"

# Send HTTP request
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all headline elements - adjust tag/class based on the site
    headlines = soup.find_all("h2")  # You can refine with class_="some-class" if needed

    # Extract and clean headline text
    top_headlines = []
    for h in headlines:
        text = h.get_text(strip=True)
        if text:
            top_headlines.append(text)

    # Save to text file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for headline in top_headlines:
            f.write(headline + "\n")

    print(f"{len(top_headlines)} headlines saved to 'headlines.txt'.")

else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
