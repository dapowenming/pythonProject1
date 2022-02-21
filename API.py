import requests
import time
import pandas as pd

cookies = {"_limsplus_session": "FN49KoW4EEyemQYzpz5LfcrCveO94MJIp9XOez9cHgAceiRvbJ2QLYfEeDPWWF22Xf1ZrXrgLpOGDbY%2B%2FNLzl0f7RmdfOOm2Ielfps5T904afDmac92b86JU0TMjH88f4sGBE%2B%2FNKd1SiiG73uEga3v9L39YT%2BPCmN6gFb6eaYjlgyGeWqcGPaTAhMeH%2FKw9YX2w--r8STBEtW4%2F6nORYl--3U%2FbmvBUHNGJtJC0xIFdkg%3D%3D"}
list = []
N =0
for i in range(4107):
    response = requests.get(f"https://han-limsplus.abcam.com/resources.json?resource_type=recombinant_pair&page={i+1}", cookies=cookies, verify=False)
    A = response.text
    null = None
    B = eval(A)
    list.extend(B)
    N=N+1
    print(N)
    time.sleep(0.5)

pf = pd.DataFrame(list)

print(list[0])

build = 'C:\\Users\\xfang\\Desktop\\2022\\LIMS\\API-recombinant_pair.xlsx'
pf.to_excel(build)