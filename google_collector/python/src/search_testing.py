try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

from datetime import datetime

# https://www.geeksforgeeks.org/performing-google-search-using-python-code/

# pinterest derien3919
# facebook 101489634842378
# instagram https://www.instagram.com/marine_minederien/

today =  datetime.now().strftime('%Y%m%d')
with open('k', "r") as fic:
    for kw in fic:
        keyword = kw.rstrip()
        for url in search(keyword, tld="fr", lang="fr", stop=15, pause=5):
            print(f'{keyword} {url}')
        print()
