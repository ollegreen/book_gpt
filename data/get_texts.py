# generated by ChatGPT
# another source for scraping: https://www.youtube.com/watch?v=vjVOUxlU0Qs

import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the bookshelf page
url = "https://www.gutenberg.org/ebooks/bookshelf/22"
response = requests.get(url)

# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links to individual book pages
book_links = soup.select("ol > li > a")

# Loop through each book page and download the plain text version
for link in book_links:
    book_url = link["href"]
    book_title = link.text.strip()

    # Visit the book page and find the link to the plain text version
    book_page = requests.get(book_url)
    book_soup = BeautifulSoup(book_page.content, "html.parser")
    plain_text_link = book_soup.select_one('a[href*="/files/"]')

    # Download the plain text version and save it to a file
    if plain_text_link:
        plain_text_url = "https://www.gutenberg.org" + plain_text_link["href"]
        plain_text_content = requests.get(plain_text_url).text
        with open(f"{book_title}.txt", "w", encoding="utf-8") as f:
            f.write(plain_text_content)