
from potee import ServiceBase, ServiceTesting
import requests
srv = ServiceBase()

@srv.ping
def comment(host):
    return requests.get(f"http://{host}:5000/ping").text

@srv.get("example")
def get_auth(host, _id):
    return requests.get(f"http://{host}:5000/get/{_id}").text

@srv.put("example")
def put_auth(host, flag):
    return requests.post(f"http://{host}:5000/put", data={"flag": flag}).text

@srv.exploit("example")
def exploit(host):
    answer =  requests.get(f"http://{host}:5000/exploit").text
    if answer == "yes":
        return True

if __name__ == "__main__":
    srv.run()