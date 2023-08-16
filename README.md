## Objective
The purpose of this project was to analyze data regarding occupancy and funding/actual capacity in active overnight shelter services operating within the Toronto area.

## Tools & Architecture
![Project Arcitecture](https://i.imgur.com/g5CcxCE.png)
- Python (Integration)
- Google Cloud Platform
  - Cloud Storage (Storage)
  - Cloud Composer/Airflow (Scheduling)
  - BigQuery (Warehouse)
- Looker Studio (Analytics)

## Data 
The dataset used was provided by the Shelter, Support and Housing Administration division and is available for preview and download at the [City of Toronto's open data catalogue](https://open.toronto.ca/dataset/daily-shelter-overnight-service-occupancy-capacity/).

### Data Model Schema:
![Data Model](https://i.imgur.com/k2k2r1v.png)
