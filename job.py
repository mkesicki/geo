import subprocess
import argparse
from datetime import date
import json

parser = argparse.ArgumentParser(description='Call script to parse data from http://www.geonames.org data based on country or city in country')

parser.add_argument('username',
                    help='Api username. This is mandatory argument.')

args = parser.parse_args()
username = args.username.lower()
directory = './data/'

countries = ['ae', 'om', 'bh', 'qa', 'sa', 'kw']

for country in countries:
    subprocess.call(['python3.6', 'geo.py', country, username])
    file = directory = './data/' + date.today().__str__() + "/country/"+country + '/cities/data.json'
    json_data = json.load(open(file))

    for city in json_data.get('cities'):
        subprocess.call(['python3.6', 'geo.py', country, username, '--id=' + city.get('id')])

