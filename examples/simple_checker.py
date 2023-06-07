from potee import ServiceBase, ServiceTesting
import requests
from aiohttp import ClientSession
import asyncio

srv = ServiceBase()


async def add_id(f, i, *args):
    result = await f(*args)
    return {i: result}


def http(f):
    async def decorator(data):
        tasks = []
        async with ClientSession() as session:
            for i, url in data.get("urls").items():
                flag = data.get("flags").get(i)
                value = data.get("values").get(i)

                task = asyncio.ensure_future(add_id(f, i, session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            return responses

    return decorator


@srv.ping
@http
async def comment(s, url):
    r = await s.get(f"http://{url}:5000/ping")
    return await r.text()


@srv.get("example")
@http
async def get_auth(s, url):
    r = await s.get(f"http://{url}:5000/get/{value}")
    return await r.text()


@srv.put("example")
@http
async def put_auth(s, url):
    r = await s.post(f"http://{url}:5000/put", data={"flag": flag})
    return await r.text()


@srv.exploit("example")
def exploit(data):
    answer = requests.get(f"http://{host}:5000/exploit").text
    if answer == "yes":
        return True


if __name__ == "__main__":
    srv.run()
