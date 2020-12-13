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
print("date,mot clé,rang boutique,première url boutique,nb occurences boutique,rang FB,première url FB,nb occurences FB,rang Pinterest,première url Pinterest,nb occurences Pinterest,rang Instagram,première url Instagram,nb occurences Instagram")
with open('keywords', "r") as fic:
    for kw in fic:
        keyword = kw.rstrip()
        # reinit variables
        counter = 0
        found =	{ "boutique": False, "fb": False, "pinterest": False, "instagram" : False }
        nb =	{ "boutique": 0, "fb": 0, "pinterest": 0 , "instagram" : 0}
        first_url =	{ "boutique": "", "fb": "", "pinterest": "" , "instagram" : ""}
        rank_first_url = { "boutique": 0, "fb": 0, "pinterest": 0 , "instagram" : 0}

        for url in search(keyword, tld="fr", lang="fr", num=15, stop=15, pause=5):
            counter += 1
            if "minederien.net" in url:
                if not found["boutique"] :
                    found["boutique"] = True
                    nb["boutique"] = 1
                    rank_first_url["boutique"] = counter
                    first_url["boutique"] = url
                else:
                    nb["boutique"] += 1

            elif "101489634842378" in url and "facebook" in url:
                if not found["fb"] :
                    found["fb"] = True
                    nb["fb"] = 1
                    rank_first_url["fb"] = counter
                    first_url["fb"] = url
                else:
                    nb["fb"] += 1

            elif "derien3919" in url and "pinterest" in url:
                if not found["pinterest"] :
                    found["pinterest"] = True
                    nb["pinterest"] = 1
                    rank_first_url["pinterest"] = counter
                    first_url["pinterest"] = url
                else:
                    nb["pinterest"] += 1
                    
            elif "marine_minederien" in url and "instagram" in url:
                if not found["instagram"] :
                    found["instagram"] = True
                    nb["instagram"] = 1
                    rank_first_url["instagram"] = counter
                    first_url["instagram"] = url
                else:
                    nb["instagram"] += 1

        print("{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(today,keyword,rank_first_url["boutique"],first_url["boutique"],nb["boutique"],rank_first_url["fb"],first_url["fb"],nb["fb"],rank_first_url["pinterest"],first_url["pinterest"],nb["pinterest"],rank_first_url["instagram"],first_url["instagram"],nb["instagram"]))
