# Asyncio

## Quick Start
```py
import asyncio
import aiohttp

async def fetch_data(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      return await response.text()

async def main():
  start_time = time.time()
  async with aiohttp.ClientSession() as session:
    tasks = [
      fetch_data("https://example.com/data1"),
      fetch_data("https://example.com/data2")
    ]
    data1, data2 = await asyncio.gather(*tasks)
  end_time = time.time()

  print(f"Total time: {end_time - start_time:.2f} seconds")
  print(f"Data from https://example.com/data1: {data1}")
  print(f"Data from https://example.com/data2: {data2}")

asyncio.run(main())
```