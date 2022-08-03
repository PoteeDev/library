
from potee import ServiceBase

srv = ServiceBase()

@srv.ping
def comment(host):
    return 1

@srv.get("auth")
def get_auth(host, _id):
    return 1

@srv.put("auth")
def put_auth(host, flag):
    return 1

if __name__ == "__main__":
    srv.run()