import json
from urllib import request
from datetime import date


URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT_G4ULT92WvbXu_FlXoanMedIDspXsbWtV-i2WAA55DokJv9YttrfwTdwMtUjorHfZJsskIxHE8AIZ/pub?gid=1301422051&single=true&output=csv"  # noqa

TODAY = date.today()

webURL = request.urlopen(URL)
raw_data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
data = [x for x in
        raw_data.decode(encoding).splitlines() if x]

data_out = {
    'data': data,
    'updated': TODAY.isoformat()
}

with open('data.json', 'w') as outfile:
    outfile.write(json.dumps(data_out))
