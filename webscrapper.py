import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()

    q = "interbank since:2023-01-01 until:2023-05-31"
    tweets = []
    async for rep in api.search_raw(q, limit=5000):
        # rep is httpx.Response object
        if rep.status_code == 200:
            tweets.extend(rep.json())
        else:
            print(rep.status_code, rep.json())



if __name__ == "__main__":
    asyncio.run(main())
