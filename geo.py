import argparse
from CountryClass import CountryClass
from AreaClass import AreaClass

parser = argparse.ArgumentParser(description='Parse http://www.geonames.org data based on country or city in country')

parser.add_argument('country',
                    help='Country name for which parse cities. This is mandatory argument.')

parser.add_argument('username',
                    help='Api username. This is mandatory argument.')

parser.add_argument('--id',
                     help='Link to geotree for city')


args = parser.parse_args()
country = args.country.lower()
username = args.username.lower()

if args.id is not None:
    id = args.id.lower()
else:
    id = ''

if id is not '':
    print("Parse "+country + "' city by id: " + id)
    area = AreaClass(id, username, country)
    area.parse()
else:
    print("Parse country: " + country)
    parser = CountryClass()
    parser.parse(country)
