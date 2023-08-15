import pandas as pd

class Transform:
    #initialize dataframe object
    def __init__(self, dataframe):
        self.dataframe = dataframe

    #transformation function for dataset
    def transform_df_data(self):
        #returns df copy
        df = self.dataframe.copy()
        #converts column headers to lowercase
        df.columns = df.columns.str.lower()

        #convert date column to datetime object
        df['occupancy_date'] = pd.to_datetime(df['occupancy_date'], format='%Y-%m-%d')
        #convert location id to integer
        df['location_id'] = df['location_id'].fillna(0).astype('int64')

        #create date dimension table
        date_dim = df[['occupancy_date']].reset_index(drop=True)
        date_dim = date_dim.drop_duplicates().reset_index(drop=True)
        date_dim['date_id'] = date_dim.index
        date_dim['occupancy_day'] = date_dim['occupancy_date'].dt.day
        date_dim['occupancy_month'] = date_dim['occupancy_date'].dt.month
        date_dim['occupancy_year'] = date_dim['occupancy_date'].dt.year
        date_dim = date_dim[['date_id', 'occupancy_date', 'occupancy_day', 'occupancy_month', 'occupancy_year']]

        #convert date_dim table to dictionary
        date_dict = date_dim['occupancy_date'].to_dict()

        # create sector dimension table
        sector_dim = df[['sector']].reset_index(drop=True)
        sector_dim = sector_dim.drop_duplicates().reset_index(drop=True)
        sector_dim['sector_id'] = sector_dim.index
        sector_dim = sector_dim[['sector_id', 'sector']]

        # create overnight service type dimension table
        os_type_dim = df[['overnight_service_type']].reset_index(drop=True)
        os_type_dim = os_type_dim.drop_duplicates().reset_index(drop=True)
        os_type_dim['os_type_id'] = os_type_dim.index
        os_type_dim = os_type_dim[['os_type_id', 'overnight_service_type']]

        # create capacity type dimension table
        capacity_type_dim = df[['capacity_type']].reset_index(drop=True)
        capacity_type_dim = capacity_type_dim.drop_duplicates().reset_index(drop=True)
        capacity_type_dim['capacity_type_id'] = capacity_type_dim.index
        capacity_type_dim = capacity_type_dim[['capacity_type_id', 'capacity_type']]

        # create organization dimension table
        organization_dim = df[['organization_id', 'organization_name']]
        organization_dim = organization_dim.drop_duplicates()
        organization_dim = organization_dim.sort_values(by=['organization_id']).reset_index(drop=True)

        # create shelter group dimension table
        shelter_dim = df[['shelter_id', 'shelter_group']]
        shelter_dim = shelter_dim.drop_duplicates()
        shelter_dim = shelter_dim.sort_values(by=['shelter_id']).reset_index(drop=True)

        # create location dimension table
        location_dim = df[['location_id', 'location_name', 'location_address', 'location_postal_code', 'location_city',
                           'location_province']]
        location_dim = location_dim.drop_duplicates()
        location_dim = location_dim.sort_values(by=['location_id']).reset_index(drop=True)

        # create program dimension table
        program_dim = df[['program_id', 'program_name', 'program_model', 'program_area']]
        program_dim = program_dim.drop_duplicates()
        program_dim = program_dim.sort_values(by=['program_id']).reset_index(drop=True)

        #begin construction of fact table
        # rename df column headers
        df.rename(columns={'occupancy_date': 'date_id', 'sector': 'sector_id', 'overnight_service_type': 'os_type_id',
                           'capacity_type': 'capacity_type_id'}, inplace=True)
        #replace dates with integers for date_id column
        df['date_id'].replace(date_dict.values(), date_dict.keys(), inplace=True)
        #replace values with enumerated lists
        df['sector_id'].replace(['Men', 'Mixed Adult', 'Women', 'Families', 'Youth'], [*range(0, 5)], inplace=True)
        df['capacity_type_id'].replace(['Room Based Capacity', 'Bed Based Capacity'], [*range(0, 2)], inplace=True)
        df['os_type_id'].replace(['Motel/Hotel Shelter', 'Shelter', 'Isolation/Recovery Site',
                                  '24-Hour Women\'s Drop-in', '24-Hour Respite Site', 'Warming Centre'],
                                 [*range(0, 6)], inplace=True)
        # create fact table
        fact_table = df[['_id', 'date_id', 'organization_id', 'shelter_id', 'location_id', 'program_id', 'sector_id',
                         'os_type_id', 'capacity_type_id', 'service_user_count', 'capacity_actual_bed',
                         'capacity_actual_room', 'capacity_funding_bed', 'capacity_funding_room', 'occupied_beds',
                         'occupied_rooms', 'unoccupied_beds', 'unoccupied_rooms', 'unavailable_beds',
                         'unavailable_rooms', 'occupancy_rate_beds', 'occupancy_rate_rooms']]

        #return fact and dim tables as nested dictionary
        return {'date_dim': date_dim.to_dict(),
                'sector_dim': sector_dim.to_dict(),
                'os_type_dim': os_type_dim.to_dict(),
                'capacity_type_dim': capacity_type_dim.to_dict(),
                'organization_dim': organization_dim.to_dict(),
                'shelter_dim': shelter_dim.to_dict(),
                'location_dim': location_dim.to_dict(),
                'program_dim': program_dim.to_dict(),
                'fact_table': fact_table.to_dict()}