# Description

This simple repository contains script to parse data from http://www.geonames.org/.
It is using their API, so you will need user account to use it.
Script parse data from API and stores in json files.
The idea is to get cities per country or get areas assigned to specific id.

# Requirements

1. Python 3.6
2. BeautifulSoup module
3. requests module

# Examples

## geo.py:

This script do real parsing. It takes arguments and parse data:
```bash
python3.6 geo.py -h
usage: geo.py [-h] [--id ID] country username

Parse http://www.geonames.org data based on country or city in country

positional arguments:
  country     Country name for which parse cities. This is mandatory argument.
  username    Api username. This is mandatory argument.

optional arguments:
  -h, --help  show this help message and exit
  --id ID     Place id from geonames
``` 

```bash
python3.6 geo.py pl username
Parse country: pl
Store data in: /Users/username/geo/data/2018-03-02/country/pl/cities/data.json
```

This will get cities for Poland and store it in json file. Part of file output:

```json
"cities": 
[
    {
        "name": "Warsaw", 
        "link": "http://www.geonames.org/maps/google_52.23_21.012.html", 
        "tree": "http://geotree.geonames.org/756135/", 
        "id": "756135"}, 
    {
        "name": "Łódź",
        "link": "http://www.geonames.org/maps/google_51.75_19.467.html",
        "tree": "http://geotree.geonames.org/3093133/", 
        "id": "3093133"
    },
]
```

```bash
python3.6 geo.py pl --id=3094802 username
Parse pl area by id: 3094802
Store data in: /Users/username/geo/data/2018-03-02/country/pl/cities/Lesser Poland Voivodeship.json
```

This will parse are #3094892 from Poland and store it in file. Part of file output:

```json
{
  "city": "Lesser Poland Voivodeship"
, 
"areas": 
  [
      {
        "name": "Bielany", 
        "id": 3103478
      }, 
      {
        "name": "Bronowice Wielkie", 
        "id": 3102544
       },
  ]
}

```

## job.py:

Second script just call geo.py script for array of countries. The idea is that it can be used for array of countries.
It will first parse cities per country and for each city in country it will get its areas.
Think about cron job to update data. At this moment, job use array of GCC countries:
```python 
countries = ['ae', 'om', 'bh', 'qa', 'sa', 'kw']
```
This is hardcoded but can be changed to get data as argument.

```bash
python3.6 job.py -h
usage: job.py [-h] username

Call script to parse data from http://www.geonames.org data based on country
or city in country

positional arguments:
  username    Api username. This is mandatory argument.

optional arguments:
  -h, --help  show this help message and exit
```

```bash
$ python3.6 job.py username
Parse country: ae
Store data in: /Users/username/geo/data/2018-03-02/country/ae/cities/data.json
Parse ae area by id: 292223
...
Parse country: om
Store data in: /Users/username/geo/data/2018-03-02/country/om/cities/data.json
Store data in: /Users/username/geo/data/2018-03-02/country/ae/cities/Dubai.json
Parse om area by id: 287286
Store data in: /Users/username/geo/data/2018-03-02/country/om/cities/Muscat.json
...
```


# Final words

This script was created in my free time. I needed some data related with 
geographical content and geonames is good source of it. Script is free, you can do whatever you want with it but there is no warranty,
also no animals were hurt during working on it.   
If you want to improve it, please feel fee and create issues, pull requests.
