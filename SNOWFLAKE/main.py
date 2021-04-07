from s3_helper import S3Helper
from data_scraper import DataScraper
from snowflake_helper import SnowflakeHelper
import config
import pandas as pd
import os
import glob

if __name__ == "__main__":

    # 1. Download required data

    #   a. Download metadata
    S3Helper.instance().download_file(config.S3_SEVIR_BUCKET_NAME, config.SEVIR_DIR + 'CATALOG.csv', 'CATALOG.csv')
    print('Downloaded catalog.csv!')
    #   b. Download images
    # S3Helper.download_file(config.S3_SEVIR_BUCKET_NAME, '', '.h5')
    #   c. Download storm events
    DataScraper.instance().scrape("https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/", config.STORM_EVENT_DIR)
    print('Downloaded storm events files!')

    # 2. Process downloaded data

    #   a. Process metadata
    # Read Catalog csv into pandas dataframe, rename dataframe columns header and drop NaN rows
    event_catalog_df = pd.read_csv(config.SEVIR_DIR + 'CATALOG.csv', low_memory=False)
    event_catalog_df.columns = [x.upper() for x in event_catalog_df.columns]
    event_catalog_df = event_catalog_df.dropna()
    event_catalog_df['EVENT_ID'] = event_catalog_df['EVENT_ID'].astype(int)
    print("Metadata processed and changed into a dataframe")

    #   b. Process images
    #   c. Process storm events
    column_set = set()
    df_list = []
    for f in glob.glob(config.STORM_EVENT_DIR + '*.csv.gz'):
        df = pd.read_csv(f, compression='gzip', error_bad_lines=False, low_memory=False)
        if len(column_set) == 0:
            column_set.update(set(df.columns))
            df_list.append(df)
        elif column_set == set(df.columns):
            df_list.append(df)

    storm_events_df = pd.concat(df_list)
    storm_events_df.drop(storm_events_df.columns[0], axis=1, inplace=True)
    storm_events_df.columns = [x.upper() for x in storm_events_df.columns]

    storm_events_df.reset_index(drop=True, inplace=True)
    print("Storm events dataset processed and changed into one dataframe")

    # 3. Push data to snowflake
    #   a. Push catalog dataframe to snowflake
    SnowflakeHelper.instance().write_dataframe(event_catalog_df, 'CATALOG')
    print('Sevir metadata uploaded into snowflake table "CATALOG"')

    #   b. Push storm events dataframe to snowflake
    total_rows = len(storm_events_df)
    start = 0
    end = 0
    batch_size = 1000
    while start < total_rows:
        if start + batch_size > total_rows:
            end = total_rows - 1
        else:
            end = start + batch_size - 1

        try:
            SnowflakeHelper.instance().write_dataframe(storm_events_df.loc[start:end], 'STORM_EVENTS')
            print('Uploaded batch {0} to {1}'.format(start, end))
        except:
            print('Failed to upload batch {0} to {1}'.format(start, end))
            pass
        start = start + batch_size

    print('Storm events data uploaded into snowflake table STORM_EVENTS')

    # 4. Close connections
    SnowflakeHelper.instance().close()

    print('Bye Bye!')
