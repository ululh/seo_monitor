from googlesearch import search

from datetime import datetime
import pandas as pd

keywords_file = "keywords"
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/

# pinterest derien3919
# facebook 101489634842378
# instagram https://www.instagram.com/marine_minederien/

data = {}
df = pd.DataFrame()

# gets a dict of dict and updates it 
def populate(website, url, data, counter):
    if not data['found'][website] :
        data['found'][website] = True
        data['nb'][website] = 1
        data['rank_first_url'][website] = counter
        data['first_url'][website] = url
    else:
        if data['nb'][website] == None:
            data['nb'][website] = 1
        else:
            data['nb'][website] += 1

    return(data)

today =  datetime.now().strftime('%Y%m%d')

with open(keywords_file, "r") as fd:
    for kw in fd:
        keyword = kw.rstrip()
        # reinit variables, None is used instead of 0 so unfound does not create confusion in the graph
        counter = 0
        data['found'] =	{ "store": False, "fb": False, "pinterest": False, "instagram" : False }
        data['nb'] =	{ "store": None, "fb": None, "pinterest": None, "instagram" : None}
        data['first_url'] =	{ "store": "", "fb": "", "pinterest": "" , "instagram" : ""}
        data['rank_first_url'] = { "store": None, "fb": None, "pinterest": None , "instagram" : None}

        for url in search(keyword, tld="fr", lang="fr", stop=15, pause=5):
            counter += 1
            if "minederien.net" in url:
                data = populate("store", url, data, counter)

            elif "101489634842378" in url and "facebook" in url:
                data = populate("fb", url, data, counter)

            elif "derien3919" in url and "pinterest" in url:
                data = populate("pinterest", url, data, counter)
                    
            elif "marine_minederien" in url and "instagram" in url:
                data = populate("instagram", url, data, counter)

        row = {'date' : today, 'keyword' : keyword, 'store_rank_first_url' : data['rank_first_url']['store'],
            'store_first_url' : data['first_url']["store"], 'store_nb' : data['nb']["store"], 'fb_rank_first_url' : data['rank_first_url']['fb'],
            'fb_first_url' : data['first_url']["fb"], 'fb_nb' : data['nb']["fb"], 'pinterest_rank_first_url' : data['rank_first_url']['pinterest'],
            'pinterest_first_url' : data['first_url']["pinterest"], 'pinterest_nb' : data['nb']['pinterest'],
            'instagram_rank_first_url' : data['rank_first_url']['instagram'], 'instagram_first_url' : data['first_url']["instagram"],
            'instagram_nb' : data['nb']['instagram']
        }
        df = df.append(row, ignore_index=True)

# format dataframe for csv
column_order = ['date', 'keyword', 'store_rank_first_url', 'store_first_url', 'store_nb', 'fb_rank_first_url', 'fb_first_url', 'fb_nb',
    'pinterest_rank_first_url', 'pinterest_first_url', 'pinterest_nb', 'instagram_rank_first_url', 'instagram_first_url', 'instagram_nb']

df[column_order].to_csv(f'ref_mdr_{today}.csv', index=False)
