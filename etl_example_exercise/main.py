### Start solution here
import pandas as pd
import os

data_source_1 = './Input/data_source_1/'
data_source_2 = './Input/data_source_2/'
output_file = './Output/consolidated_output.1.csv'


def read_all_data_files_from(input_source) -> pd.DataFrame:
    all_df = pd.DataFrame()
    for filename in os.listdir(input_source):
        if filename.endswith('.csv') or filename.endswith('.dat'):
            df = pd.read_csv(input_source + filename)
            df['source'] = filename[:-4]
            all_df = pd.concat([all_df, df], ignore_index=True)
    return all_df


df1 = read_all_data_files_from(data_source_1)
df2 = read_all_data_files_from(data_source_2)

# combine both data sources into 1 DataFrame
full_df = pd.concat([df1, df2], ignore_index=True)

# remove products that are not worth more than 1.00
full_df = full_df[full_df.worth > 1.00]

# Save DataFrame to output file
full_df.to_csv(output_file)
