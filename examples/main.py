
from potee import ServiceBase

srv = ServiceBase()

@srv.ping
def comment(host):
    print(host)
    return 0

@srv.get("auth")
def get_auth(host, _id):
    return 1

@srv.put("auth")
def put_auth(host, flag):
    print(host, flag)
    return 1

@srv.get("comment")
def get_comment(host, _id):
    return 1

@srv.put("comment")
def put_comment(host, flag):
    print("put", "comment", host, flag)
    return 1

@srv.exploit("comment")
def put_comment(host):
    print("exploit", "comment", host)
    return 1

@srv.exploit("auth")
def put_comment(host):
    print("exploit", "auth", host)
    return 1

if __name__ == "__main__":
    srv.run()