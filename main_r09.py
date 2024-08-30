import pandas as pd

# specify the path to the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"

# load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# extract the month from the 'date' column
df['month'] = df['date'].dt.month

# group by month and calculate the mean of 'deaths' for each month
average_deaths_per_month = df.groupby('month')['deaths'].mean()

# calculate the overall average of the monthly averages
overall_average_deaths = average_deaths_per_month.mean()

# print the results
print("Average number of deaths per month:")
print(average_deaths_per_month)
print("\nOverall average number of deaths per month across all months:", overall_average_deaths)
