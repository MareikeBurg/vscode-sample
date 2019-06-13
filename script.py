import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who):
    greeting = "hello, {}".format(who)
    return greeting


r = requests.get("https://google.com")
print(r.status_code)
