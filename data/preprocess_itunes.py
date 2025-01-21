import pandas as pd

# Load the CSV file
input_file = 'df_popular_podcasts.csv' 
output_file = 'itunes_podcast_dataset.tsv' 

# Read the CSV file
df = pd.read_csv(input_file)

# Keep only the "title" and "description" columns
filtered_df = df[['Name', 'Description']]

# Rename the header row
filtered_df.columns = ['title', 'description']

# Save the file as a TSV (Tab-Separated Values)
filtered_df.to_csv(output_file, sep='\t', index=False)

print(f"Converted file saved as {output_file}")