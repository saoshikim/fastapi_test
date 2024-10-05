import requests
import asyncio
import time

#conoHa用
BASE_URL = "http://123.45.67.89:8000"

#ローカル用
#BASE_URL = "http://127.0.0.1:8000"

async def sleep_time(sec):
    loop = asyncio.get_running_loop()
    try:
        res = await loop.run_in_executor(
            None,
            lambda: requests.get(f"{BASE_URL}/sleep_time/?sec={sec}", timeout=10)
        )
        return res.text
    except requests.RequestException as e:
        return f"Error: {e}"

async def main():
    print(f"main開始{time.strftime('%X')}")
    results = await asyncio.gather(sleep_time(1), sleep_time(2))
    print(results)
    print(f"main終了{time.strftime('%X')}")
    
if __name__ == "__main__":
    asyncio.run(main())