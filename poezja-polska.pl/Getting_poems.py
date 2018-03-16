
# coding: utf-8

# In[27]:

page = lambda x: 'http://www.poezja-polska.pl/fusion/articles.php?cat_id=3&rowstart={}'.format(x * 15)
MAX_PAGE = 3027
BASE_ADDR = 'http://www.poezja-polska.pl/fusion/'


# In[37]:

from bs4 import BeautifulSoup 
import requests
from tqdm import tqdm
from time import sleep

def get_links_from_page(link, with_titles=False):
    soup = BeautifulSoup(requests.get(page(k)).text, "html.parser")
    soup = soup.findAll("td", "main-body")[1].findAll("a")
    links = [x.attrs["href"] for x in soup]
    if with_titles:
        titles = [x.string for x in soup]
        return list(zip(links, titles))
    else:
        return [BASE_ADDR + l for l in links]

def flatten(ll):
    return [x for l in ll for x in l]    


# In[40]:

links = []
for k in tqdm(range(2)):
    links.append(get_links_from_page(k))
    sleep(1)
    
import json

with open("links_from_poezja_polska.pl", "w") as f:
    json.dump(flatten(links), f)


# In[43]:




# In[ ]:



