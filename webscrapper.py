import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()

    q = "interbank since:2023-01-01 until:2023-05-31"
    async for rep in api.search_raw(q, limit=5000):
        # rep is httpx.Response object
        print(rep.status_code, rep.json())
        break

if __name__ == "__main__":
    asyncio.run(main())
