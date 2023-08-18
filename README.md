## Objective
The purpose of this project was to analyze data regarding occupancy and funding/actual capacity in active overnight shelter services operating within the Toronto area.

## Tools & Architecture
![Project Arcitecture](https://i.imgur.com/g5CcxCE.png)
- Python (Ingestion & Transformation)
- Google Cloud Platform
  - Cloud Storage (Storage)
  - Cloud Composer/Airflow (Scheduling)
  - BigQuery (Warehouse)
- Looker Studio (Analytics)

## Data 
The dataset used was provided by the Shelter, Support and Housing Administration division and is available for preview and download at the [City of Toronto's open data catalogue](https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/).

### Data Model Schema:
![Data Model](https://i.imgur.com/lkccXDd.png)

## Dashboard
Queried and joined data within BigQuery, sending it to Looker Studio where it was used to build a report that highlighted insights regarding overnight shelter programs in the city. The interactive report can be found [here](https://lookerstudio.google.com/s/vIK9u398frU).

![Dashboard](https://i.imgur.com/2x3qJBc.png)
