from potee import ServiceBase, ServiceTesting
import requests
from aiohttp import ClientSession
import asyncio

srv = ServiceBase()


@srv.ping
@srv.http
async def comment(s, url):
    r = await s.get(f"http://{url}:5000/ping")
    return await r.text()


@srv.get("example")
async def get_auth(s, url, value):
    r = await s.get(f"http://{url}:5000/get/{value}")
    return await r.text()


@srv.put("example")
async def put_auth(s, url, flag):
    r = await s.post(f"http://{url}:5000/put", data={"flag": flag})
    return await r.text()


@srv.exploit("example")
def exploit(data):
    answer = requests.get(f"http://{host}:5000/exploit").text
    if answer == "yes":
        return True




if __name__ == "__main__":
    srv.run()
