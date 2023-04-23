import sqlite3
import pandas as pd


#create connection
conn = sqlite3.connect('restaurant_recommender.db')
cursor = conn.cursor()

#read from db table
df = pd.read_sql("SELECT * FROM restaurants", conn)
df['restaurant'] = df['name']

def default_recommendations(df):
    random_samples = df.sample(n = 10, replace = True)
    return random_samples

v = default_recommendations(df)

list = list(v.index)
i = list[0]
for index, row in v.iterrows():
    if index == i:
        name = v.at[index, 'restaurant']
        print(name)

print('*' *2)