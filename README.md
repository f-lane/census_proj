## How many people in Bristol have a UK and other passport?
### Using the Office of National Statistics' 2021 Census dataset to investigate dual passport ownership in Bristol.

#### I used this mini-project to familiarise myself with shapefiles and geopandas. 
For a basic guide to shapefiles, see: https://chrishavlin.wordpress.com/2016/11/16/shapefiles-tutorial/ <br />
The ONS API documentation is available at: https://developer.ons.gov.uk/

#### How to run: 

This project runs on Python. It requires the following non-native libraries: requests, pandas, matplotlib, geopandas.

- The 2021_census_api.py file gets data about passport ownership in Bristol's five constituencies from the ONS API. The results are written to constituency_data.json. <br />
- The shapefile of UK parliamentary constituencies (post-2019) was sourced from the ONS' Open Geography Portal: https://geoportal.statistics.gov.uk/datasets/ons::westminster-parliamentary-constituencies-july-2024-boundaries-uk-buc-2/about <br />
- The Final.ipynb provides some very basic visualisations of the data, using matplotlib and geopandas (examples below):

![image](https://github.com/user-attachments/assets/067831db-7562-4bea-911f-871111a1fb74) <br />
<br />
<br />
![image](https://github.com/user-attachments/assets/f4e687a9-5c50-4b69-9170-7bf0d48cfc13)



