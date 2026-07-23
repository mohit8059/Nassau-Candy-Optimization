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