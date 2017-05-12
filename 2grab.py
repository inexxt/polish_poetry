# Downloads poems into `data` folder

import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

NUM_OF_THREADS = 6

with open("links.txt", "r") as f:
    all_links = f.readlines()

stats = {}
broken = []

def download(l):
    url = l.split("\t")[0]
    unique_name = url.split("/")[-1]
    name = " ".join(l.split("\t")[1:])
    
    try:
        c = requests.get(url).content
        text = BeautifulSoup(c, "lxml").find("div", "content").strings
        text = "\n".join(list(text))

#         print("downloaded " + unique_name)
        try:
            counter = BeautifulSoup(c, "lxml").find("div", "view-counter").getText().split(" ")[-1]
        except:
            counter = -1

        with open("data/" + unique_name + ".txt", "w") as f:
            f.write(text)

        stats[unique_name] = int(counter)

    except:
        broken.append(l)

from multiprocessing import Pool
from time import sleep

# with Pool(NUM_OF_THREADS) as p:
#     max_ = len(all_links)

#     with tqdm(total=max_) as pbar:
#         for i, _ in tqdm(enumerate(p.imap_unordered(download, all_links))):
#             pbar.update()
#     pbar.close()

#trudno że bez równoleglości
for l in tqdm(all_links):
    download(l)