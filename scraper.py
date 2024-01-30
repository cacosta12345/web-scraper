import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

import requests
from page_parser import parse_citations_needed_count, parse_citations_needed_report

def get_citations_needed_count(url):
    response = requests.get(url)
    return parse_citations_needed_count(response.text)

def get_citations_needed_report(url):
    response = requests.get(url)
    return parse_citations_needed_report(response.text)


if __name__ == "__main__":
    
    url = input("Enter the URL of the Wikipedia page to scrape (or press enter to use the default): ")
    if not url.strip():
        url = "https://en.wikipedia.org/wiki/History_of_slavery"

    count = get_citations_needed_count(url)
    print(f"Number of citations needed: {count}\n")

    report = get_citations_needed_report(url)
    print("Citations needed report:\n", report)
