import requests
import json

print('''
  _    _           _       ______ __  __ 
 | |  | |         | |     |  ____|  \/  |
 | |__| | __ _ ___| |__   | |__  | \  / |
 |  __  |/ _` / __| '_ \  |  __| | |\/| |
 | |  | | (_| \__ \ | | | | |____| |  | |
 |_|  |_|\__,_|___/_| |_| |______|_|  |_|

      Iran Internal Link Checker
''')


with open("urls.txt","r") as urls:
    url_list = urls.readlines()


def CHECK_IP(url):
    get_url = "https://api.linkirani.ir/apiv1/shortlink"

    header = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "accept" : "application/json, text/plain, */*",
        "referer" : "https://linkirani.ir/"
    }

    paylaod = {
        "url" : url
    }

    session = requests.Session()
    res = session.post(get_url, headers=header, json=paylaod)
    
    return json.loads(res.content)["isRegistered"]


for ip in url_list:

    # check if proxy:port and print proxy only
    if ":" in ip:
        ip = ip[:ip.index(":")]
    
    check = CHECK_IP(ip)
    
    if check:
        print(f"{ip.strip()} [True]")
    else:
        print(f"{ip.strip()} [False]")
