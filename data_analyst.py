import pandas as pd

# Maaş verileri
salary_data = [
    ["Europe", "Berlin", 4000, 6000, 9000],
    ["Europe", "Paris", 4000, 6000, 9000],
    ["Europe", "London", 4500, 6500, 10500],
    ["Europe", "Amsterdam", 4000, 6000, 9000],
    ["Europe", "Dublin", 4200, 6200, 9500],
    ["Europe", "Zurich", 5500, 7500, 12000],
    ["Europe", "Stockholm", 3700, 5000, 8000],
    ["Europe", "Oslo", 4000, 6000, 8500],
    ["Europe", "Vienna", 3500, 5000, 8000],
    ["Asia", "Tokyo", 3800, 5500, 8500],
    ["Asia", "Seoul", 3000, 4500, 7000],
    ["Asia", "Singapore", 4500, 7000, 10000],
    ["Asia", "Hong Kong", 4700, 7000, 10500],
    ["Asia", "Tel Aviv", 4200, 6500, 9500],
    ["N. America", "New York", 6000, 9500, 14000],
    ["N. America", "San Francisco", 6500, 10000, 15000],
    ["N. America", "Seattle", 6000, 9500, 14000],
    ["N. America", "Boston", 6000, 9500, 14000],
    ["N. America", "Austin", 5500, 9000, 13000],
    ["N. America", "Chicago", 5500, 9000, 13000],
    ["N. America", "Toronto", 4500, 7000, 11000],
    ["N. America", "Vancouver", 4300, 6700, 10000],
    ["N. America", "Montreal", 4100, 6500, 9500],
]

df_salary = pd.DataFrame(salary_data, columns=[
    "Continent", "City", "Entry-Level", "Mid-Level", "Senior-Level"
])

# Kira ve yemek giderleri verisi
rent_food_data = [
    ["Europe", "Berlin", 1220, 300],
    ["Europe", "Paris", 1610, 350],
    ["Europe", "London", 2360, 400],
    ["Europe", "Amsterdam", 1220, 320],
    ["Europe", "Dublin", 1760, 370],
    ["Europe", "Zurich", 1770, 450],
    ["Europe", "Stockholm", 880, 300],
    ["Europe", "Oslo", 1940, 400],
    ["Europe", "Vienna", 800, 280],
    ["Asia", "Tokyo", 1730, 350],
    ["Asia", "Seoul", 1140, 280],
    ["Asia", "Singapore", 2250, 400],
    ["Asia", "Hong Kong", 2590, 420],
    ["Asia", "Tel Aviv", 1160, 320],
    ["N. America", "New York", 3500, 450],
    ["N. America", "San Francisco", 3150, 430],
    ["N. America", "Seattle", 1840, 400],
    ["N. America", "Boston", 2700, 430],
    ["N. America", "Austin", 1200, 350],
    ["N. America", "Chicago", 1986, 400],
    ["N. America", "Toronto", 1120, 350],
    ["N. America", "Vancouver", 1150, 350],
    ["N. America", "Montreal", 1100, 320],
]

df_rent_food = pd.DataFrame(rent_food_data, columns=["Continent", "City", "Avg Monthly Rent (USD)", "Avg Monthly Food Cost (USD)"])

# Combining (merging) based on 'Continent' and 'City'
df_full = pd.merge(df_salary, df_rent_food, on=["Continent", "City"])

pd.set_option('display.max_rows', None)    # Tüm satırları göster
pd.set_option('display.max_columns', None) # Tüm sütunları göster
print(df_full)
#=====================================================

# 1- previosuly known that there is no missing value;but let's confirm
print(df_full.isnull().sum())
#2-.describe is showing that count,mean,std,min,...etc) ;Generate descriptive statistics
print(df_full.describe())
# 3-rent as a percentage of entry-level salary:
df_full["Rent_to_EntrySalary_percentage"] = df_full["Avg Monthly Rent (USD)"] / df_full["Entry-Level"] * 100
#Create New Metrics — Meaningful Ratios. ( rent as a percentage of entry-level salary)
print(df_full["Rent_to_EntrySalary_percentage"])  #smallest ratio has more advantage
#4-similarly,food cost as a percentage of entry-level salary:
df_full["Foodcost_to_EntrySalary_percentage"]=df_full["Avg Monthly Food Cost (USD)"]/df_full["Entry-Level"]*100
print(df_full["Foodcost_to_EntrySalary_percentage"])  #The smaller the ratio, the more affordable and sustainable it is for an entry-level worker to live in that city (or country).
# 5- Total cost of living as a percentage of entry-level salary (rent + food)
df_full["TotalCost_to_EntrySalary_percentage"] = (
    (df_full["Avg Monthly Rent (USD)"] + df_full["Avg Monthly Food Cost (USD)"])
    / df_full["Entry-Level"]
) * 100

# Find the cheapest city (lowest total cost percentage)
cheapest_city = df_full.loc[df_full["TotalCost_to_EntrySalary_percentage"].idxmin()]

print("🔻 The most affordable city in terms of cost of living:")
print(cheapest_city[["City", "Continent", "TotalCost_to_EntrySalary_percentage"]])

import matplotlib.pyplot as plt

# Sort cities by total cost as a percentage of entry-level salary
sorted_df = df_full.sort_values(by="TotalCost_to_EntrySalary_percentage")

# Set figure size and aesthetics
plt.figure(figsize=(12, 8))
bars = plt.barh(
    sorted_df["City"],
    sorted_df["TotalCost_to_EntrySalary_percentage"],
    color="skyblue"
)

# Add title and axis labels
plt.xlabel("Total Cost / Entry-Level Salary (%)")
plt.title("Affordability Ranking of Cities for Entry-Level Employees")
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Annotate bars with values
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', va='center')

plt.tight_layout()
plt.show()








