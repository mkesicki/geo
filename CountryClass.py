import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import date
import re


class CountryClass(object):

    def __init__(self):
        self.domain = 'http://www.geonames.org/'
        self.geo_domain = 'http://geotree.geonames.org/'

    def parse(self, country):

        results = []
        page = requests.get(self.domain + 'search.html?country='+country)
        contents = page.content
        soup = BeautifulSoup(contents, "html.parser")
        tds = soup.findAll("td")
        for td in tds:
            links = td.findAll('a')
            if links is not None:
                for link in links:
                    if link is not None:
                        img = link.find('img')
                        if img is not None:
                            if 'P' == img['alt']:
                                next = tds[tds.index(td) + 1]
                                p = re.compile("[\d]+")
                                id = re.search(p, link['href']).group(0)
                                href = next.find('a')
                                results.append({"name": href.text, "link": self.domain + href['href'][1:], "tree": self.geo_domain + id + "/", "id": id})

        data = {"cities": results}
        json_string = json.dumps(data)
        directory = './data/' + date.today().__str__() + "/country/"+country + '/cities'
        if not os.path.exists(directory):
            os.makedirs(directory)

        file = directory+"/data.json"
        f = open(file, "w")
        f.write(json_string)
        f.close()

        print("Store data in: " + os.path.abspath(file))

