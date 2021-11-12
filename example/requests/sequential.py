import time

import requests


def fetch(session, url):
    with session.get(url) as response:
        response.raise_for_status()
        print(f"finished {url}")
        return response.text


def main():
    urls = [
        'https://cnn.com',
        'https://google.com',
        'https://twitter.com',
        'https://facebook.com',
        'https://instagram.com',
        'https://yahoo.com',
        'https://youtube.com',
        'https://reddit.com',
        'https://wikipedia.com',
        'https://ebay.com',
        'https://pinterest.com',
    ]

    with requests.session() as session:
        for url in urls:
            fetch(session, url)


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
