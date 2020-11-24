import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://twitter.com/home')
except urllib.error.URLError:
    print('Deu erro. se vira ae')
else:
    print('Twitter tá indo bro')
    #--print(site.read())-- Pega o HTML do site