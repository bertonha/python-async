import asyncio
import time

import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        content = await response.text()
        print(f"finished {url}")
        return content


async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)

    return await asyncio.gather(*tasks)


async def main():
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

    async with aiohttp.ClientSession() as session:
        await fetch_all(session, urls)


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
