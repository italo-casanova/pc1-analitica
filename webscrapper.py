import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level
import json

async def main():
    api = API()

    # create a json file to store the tweets
    with open('tweets.json', 'w') as f:
        q = "backus since:2023-01-01 until:2023-05-31"
        tweets = []
        async for rep in api.search_raw(q, limit=5000):
            # rep is httpx.Response object
            if rep.status_code == 200:
                tweets.extend(rep.json())
                print(rep.status_code, rep.json())
            else:
                print(rep.status_code, rep.json())

        json.dump(tweets, f, indent=4)
    # save the tweets list into a file





if __name__ == "__main__":
    asyncio.run(main())
