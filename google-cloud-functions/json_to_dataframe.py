import pandas as pd
import json

# Load the JSON data
json_data = '{"employees": [{"firstName": "John", "lastName": "Doe", "age": 28, "address": {"street": "123 Main St", "city": "New York", "state": "NY", "zip": "10001"}}, {"firstName": "Jane", "lastName": "Smith", "age": 32, "address": {"street": "456 Elm St", "city": "Los Angeles", "state": "CA", "zip": "90001"}}]}'
data = json.loads(json_data)

# Create an empty dataframe
df = pd.DataFrame()

# Loop through the dictionary and extract the required data
for employee in data['employees']:
    first_name = employee['firstName']
    last_name = employee['lastName']
    age = employee['age']
    street = employee['address']['street']
    city = employee['address']['city']
    state = employee['address']['state']
    zip_code = employee['address']['zip']
    
    # Add the data to the dataframe
    df = df.append({
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'street': street,
        'city': city,
        'state': state,
        'zip_code': zip_code
    }, ignore_index=True)

# Clean up the dataframe
df = df[['first_name', 'last_name', 'age', 'street', 'city', 'state', 'zip_code']]

print(df)
