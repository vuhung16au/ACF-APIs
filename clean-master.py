import pandas as pd
import re

target_rating_file = 'decmst24.txt'

with open(target_rating_file, 'r') as file:
    lines = file.readlines()[1:]

# Load the data into a pandas DataFrame
data = []
for line in lines:

    # if any(keyword in line for keyword in ['Unr', 'g']):
    #     continue
    
    fields = line.split()
    # fields = re.split(r'\t|\s+', line)

    id = fields[0]

    rating = fields[1]
    # rating = rating.replace('!', '').replace('?', '')

    if 'x' in rating:
        active = 'x' # inactive
    else:
        active = 'a' # active 
    
    if 'Unr' in rating:
        isRated = 'Unrated' # Unrated 
    else:
        isRated = 'Rated' # Rated (has a rating)

    if 'x' in rating:
        isNew = 'New' # New player 
    else:
        isNew = 'Existing' # Old player, has a rating 

    confidence_level = ''

    if '??' in rating:
        confidence_level = 'Very Unreliable'
    elif '?' in rating:
        confidence_level = 'Unreliable'
    elif '!!' in rating:
        confidence_level = 'Very Reliable'
    elif '!' in rating:
        confidence_level = 'Reliable'

    numericalRating = 0
    if 'Unr' in rating:
        numericalRating = 0
    if 'New' in rating:
        numericalRating = 0
    else:
        try:
            numericalRating = int(rating.replace('!', '').replace('?', '').replace('x', ''))
        except ValueError:
            numericalRating = 0

    federation = fields[2]

    name = ' '.join(fields[3:])

    data.append([id, rating, federation, name, active, isRated, isNew, confidence_level, numericalRating])

df = pd.DataFrame(data, columns=['ID', 'Rating', 'Federation', 'Name', 'Active', 'Unrated', 'New', 'ConfidenceLevel', 'NumericalRating'])

# Save to a CSV file
df.to_csv('master-ratings-unsorted.csv', index=False)
# Show the first 5 rows of the DataFrame
print(df.head())

# Sort by rating (highest on top) 
quick_ascending = 'master-ascending.csv'
df.sort_values(by='NumericalRating', ascending=False).to_csv(quick_ascending, index=False)
print("'master-ascending.csv' created")

# Show top 100 players
with open('master-ascending.csv', 'r') as file:
    for i in range(100):
        line = file.readline()
        print(line.strip())

print("Show top 100 players excluding federation = OS")
# Show top 100 players excluding federation = "OS"
df = df[df['Federation'] != 'OS']
df.sort_values(by='NumericalRating', ascending=False).to_csv('master-ascending-excluding-OS.csv', index=False)
with open('master-ascending-excluding-OS.csv', 'r') as file:
    for i in range(100):
        line = file.readline()
        print(line.strip())
