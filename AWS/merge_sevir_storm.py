import pandas as pd
import s3fs

catalog_df = pd.read_csv('s3://sevir-demo/CATALOG.csv')
storm_df = pd.read_csv('s3://storm-data-combined/combined_results_after_scrapping.csv')
storm_df['newevent_id'] = 'S'+ str(storm_df['EVENT_ID'])

merged_df=catalog_df.merge(storm_df,how='left',left_on='id',right_on='newevent_id')

print(catalog_df.shape)
print(merged_df.info)