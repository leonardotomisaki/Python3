import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen("https://www.pudim.com.br/")
except urllib.error.URLError:
    print("Página não acessível!")
else:
    print("Página acessível!")
