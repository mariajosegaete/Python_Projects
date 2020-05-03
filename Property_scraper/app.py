import requests
import asyncio
import aiohttp
import time
import async_timeout
import certifi

from pages.houses_page import HousesPage

page_content = requests.get('https://www.portalinmobiliario.com/arriendo/departamento/providencia-metropolitana').content
page = HousesPage(page_content)

# loop = asyncio.get_event_loop()

houses = page.houses

'''
async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(20):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}')
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f'https://www.portalinmobiliario.com/arriendo/departamento/providencia-metropolitana/_Desde_{50*i + 1}' for i in range(1,2)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))


for page_content in pages:
    page = HousesPage(page_content)
    houses.extend(page.houses)
'''

for i in range(1, 2):
    new_page = requests.get(f'https://www.portalinmobiliario.com/arriendo/departamento/providencia-metropolitana/_Desde_{50*i + 1}').content
    page = HousesPage(page_content)
    houses.extend(page.houses)
