import pandas as pd
import numpy as np

# 1. Load data
df = pd.read_csv(r'D:\Nassau Codiinator\Nassau Candy Distributor.csv')

# 2. Convert to Datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y', errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y', errors='coerce')

# 3. Clean Lead Time (Assuming a logical gap of 0-30 days max)
df['Lead Time'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Lead Time'] = df['Lead Time'].apply(lambda x: x % 30 if x > 30 else x) 

# 4. Check for errors
print(df[['Order Date', 'Ship Date', 'Lead Time']].head())

# 1. Average Lead Time per Region (Kaunsa region sabse slow hai?)
region_analysis = df.groupby('Region')['Lead Time'].mean().sort_values()
print("\n--- Efficiency by Region (Average Lead Time) ---")
print(region_analysis)

# 2. Product performance (Kaunsa product sabse zyada profit de raha hai?)
product_profit = df.groupby('Product Name')['Gross Profit'].sum().sort_values(ascending=False).head(5)
print("\n--- Top 5 Profitable Products ---")
print(product_profit)

# 3. Ship Mode Analysis (Kya shipping mode ka lead time par asar pad raha hai?)
mode_analysis = df.groupby('Ship Mode')['Lead Time'].mean()
print("\n--- Impact of Ship Mode on Lead Time ---")
print(mode_analysis)

# import math

# # Haversine formula to calculate distance between two points
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371  # Earth radius in km
#     dlat = math.radians(lat2 - lat1)
#     dlon = math.radians(lon2 - lon1)
#     a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#     return R * c

# # Factory Coordinates (jo tumne bataye the)
# factories = {
#     'Lot\'s O\' Nuts': (32.881893, -111.768036),
#     'Wicked Choccy\'s': (32.076176, -81.088371),
#     'Sugar Shack': (48.11914, -96.18115),
#     'Secret Factory': (41.446333, -90.565487),
#     'The Other Factory': (35.1175, -89.971107)
# }

# # NOTE: Yahan tumhe apne data mein City coordinates add karne honge.
# # Ek chhota example (Tumhe apna data is format mein lana hoga):
# # df['City_Lat'] = ...
# # df['City_Long'] = ...

# # Logic to find Nearest Factory
# def get_nearest_factory(row):
#     distances = {name: haversine(row['City_Lat'], row['City_Long'], lat, lon) 
#                  for name, (lat, lon) in factories.items()}
#     return min(distances, key=distances.get)

# # df['Nearest_Factory'] = df.apply(get_nearest_factory, axis=1)

import pandas as pd
import math

# File paths - MAKE SURE YE PATH SAHI HAI!
path_nassau = r'D:\Nassau Codiinator\Nassau Candy Distributor.csv'
path_cities = r'D:\Nassau Codiinator\uscities.csv'

# 1. Load Data
df = pd.read_csv(path_nassau)
cities = pd.read_csv(path_cities)

# 2. Prepare for Merge (Cleaning)
df['City_clean'] = df['City'].str.strip().str.lower()
df['State_clean'] = df['State/Province'].str.strip().str.lower()
cities['city_clean'] = cities['city'].str.strip().str.lower()
cities['state_clean'] = cities['state_name'].str.strip().str.lower()

# 3. Merge Data (Jodna)
df = df.merge(cities[['city_clean', 'state_clean', 'lat', 'lng']], 
              left_on=['City_clean', 'State_clean'], 
              right_on=['city_clean', 'state_clean'], 
              how='left')

# 4. Haversine Function
def haversine(lat1, lon1, lat2, lon2):
    if pd.isna(lat1) or pd.isna(lon1): return float('inf')
    R = 6371 # Radius of Earth
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

# Factory List
factories = {
    'Lot\'s O\' Nuts': (32.881893, -111.768036),
    'Wicked Choccy\'s': (32.076176, -81.088371),
    'Sugar Shack': (48.11914, -96.18115),
    'Secret Factory': (41.446333, -90.565487),
    'The Other Factory': (35.1175, -89.971107)
}

# 5. Calculate Nearest Factory
def get_nearest(row):
    if pd.isna(row['lat']): return "Unknown"
    distances = {name: haversine(row['lat'], row['lng'], lat, lon) for name, (lat, lon) in factories.items()}
    return min(distances, key=distances.get)

df['Nearest_Factory'] = df.apply(get_nearest, axis=1)

# 6. SAVE THE RESULT (Sabse important step)
df.to_csv(r'D:\Nassau Codiinator\Final_Optimized_Data.csv', index=False)

print("SUCCESS! 'Final_Optimized_Data.csv' file save ho gayi hai.")
print(df[['City', 'Nearest_Factory']].head(10))