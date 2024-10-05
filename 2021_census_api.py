## This api queries the ONS 2021 Census dataset: specifically, passport (and multi-passport) holders within Bristol's five constituencies.

## Api guidance including relevant endpoints available at https://developer.ons.gov.uk/createyourowndataset/
## EG. to view area-type ids, call url = ('https://api.beta.ons.gov.uk/v1/population-types/UR/dimensions/rgn/categorisations')
## Note: I have chosen to use area-type=p19wpc which refers to parliamentary constituencies as redrawn in 2019 (first used in 2024 General Election)
## If you wish to use parliamentary constituencies pre-2019, area-type=wpc

import json, requests, pprint

## Querying census results: passport (and multi-passport) holders within Bristol's five constituencies.
url = ('https://api.beta.ons.gov.uk/v1/population-types/UR/census-observations?area-type=p19wpc,E14001131,E14001132,E14001133,E14001134,E14001135&dimensions=multi_passports')
response = requests.get(url)
response.raise_for_status()
#pprint.pprint(response.text) ## Downloaded data stored in response.text
json_as_python = json.loads(response.text)
#pprint.pprint(json_as_python) ## View data
#print(json_as_python.keys()) ## View keys: I am interested in the 'observations' key.

bris_obs = json_as_python['observations']

## Creating dictionary of the data I want: constituency name and how many people hold each type of (multi)passport.
constituency_data = {}

for data_point in bris_obs:
    constituency = data_point['dimensions'][0]['option'] #Get the name of the constituency
    passport = data_point['dimensions'][1]['option'] #Get the passport type
    # observation = data_point['observation']
    # print(constituency)
    # print(passport)
    # print(observation)

    if constituency in constituency_data.keys():
        constituency_data[constituency][passport] = data_point['observation']
    else:
        constituency_data[constituency] = {passport: data_point['observation']}

# pprint.pprint(constituency_data)

## Writing results to a json file
with open("constituency_data.json", "w", encoding='utf-8') as f:
    json.dump(constituency_data, f, ensure_ascii=False, indent=4)
