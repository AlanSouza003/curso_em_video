import urllib
from urllib import request

try:
    site = request.urlopen('https://youtube.com')
except urllib.error.URLError:
    print(f"\033[1;91mERRO: O site YOUTUBE não está acessível no momento\033[0m")
else:
    print("\033[1;92mSite acessado com sucesso!\033[0m")
    print(site)