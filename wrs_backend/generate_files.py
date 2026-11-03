import pandas as pd
import os

PATH = "raw_data/"
COMPOSITE_FILE = 'all_years_raw.csv'
TOP_100_FILE = '../../wrs-data/top_100.csv'
QA_OUTPUT = 'all_riders_by_race_count.csv'

def generate_top_100(source_file, destination_file,qa_output):
    df = pd.read_csv(source_file)

    result_df = df.groupby('racer_name').agg(
        race_count=('racer_name','count'),
        total_points=('points','sum')
    ).sort_values(by='race_count',ascending=False).reset_index()

    result_df.columns = ['racer_name','race_count','total_points']
    result_df['total_points'] = result_df['total_points'].astype(int)

    result_df.to_csv(qa_output, index=False)
    result_df = result_df.head(150)
    result_df.to_csv(destination_file, index=False)

def generate_master_file(path):
    base_df = pd.DataFrame()
    dir_list = os.listdir(path)
    for file in dir_list:
        df = pd.read_csv(path+file)
        base_df = pd.concat([base_df,df],ignore_index=True)
    base_df.to_csv(COMPOSITE_FILE)

if __name__ == "__main__":
    generate_master_file(PATH)
    generate_top_100(COMPOSITE_FILE, TOP_100_FILE, QA_OUTPUT)