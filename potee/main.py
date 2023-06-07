from collections import defaultdict
from pickle import load
from .testing import ServiceTesting
import sys
from aiohttp import ClientSession
import asyncio


class ServiceBase:
    def __init__(self):
        self.functions = defaultdict(dict)

    def get(self, _name):
        def wrapper(f):
            return self.action("get", _name)(f)

        return wrapper

    def put(self, _name):
        def wrapper(f):
            return self.action("put", _name)(f)

        return wrapper

    def exploit(self, _name):
        def wrapper(f):
            return self.action("exploit", _name)(f)

        return wrapper

    def ping(self, f):
        return self.action("ping")(f)

    def action(self, action, _name="default"):
        def decorator(f):
            self.functions[action][_name] = f

        return decorator

    @staticmethod
    def load_data():
        return {
            "urls": {i: "localhost" for i in range(10)},
            "values": {i: "123" for i in range(10)},
            "flags": {i: "qwe" for i in range(10)},
        }

    def parce_args(self):
        action = sys.argv[1]
        name = "default"
        if len(sys.argv) >= 3:
            name = sys.argv[2]

        func = self.functions[action][name]
        return asyncio.run(func(self.load_data()))

    def run(self):
        if sys.argv[1] == "test":
            ServiceTesting().run(self.functions)
            return

        print(self.parce_args())
        # result = self.parce_args()
        # if not result:
        #     print(0, end="")
        # else:
        #     print(result, end="")
