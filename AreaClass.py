import requests
import json
import os
from datetime import date


class AreaClass(object):

    def __init__(self, id, user, country):
        self.link = "http://api.geonames.org/childrenJSON?geonameId=" + id + "&username=" + user
        self.country = country

    def parse(self):
        results = []
        page = requests.get(self.link)
        contents = page.content
        data = json.loads(contents)
        if data.get('totalResultsCount') > 0:
            city = data.get('geonames')[0].get("adminName1")

            for area in data.get('geonames'):
                results.append({"name": area.get("name"), "id": area.get("geonameId")})

            data = {"city": city, "areas": results}

            json_string = json.dumps(data)

            directory = './data/' + date.today().__str__() + "/country/" + self.country + '/cities/'
            if not os.path.exists(directory):
                os.makedirs(directory)

            file = directory + "/" + city + ".json"
            f = open(file, "w")
            f.write(json_string)
            f.close()

            print("Store data in: " + os.path.abspath(file))

