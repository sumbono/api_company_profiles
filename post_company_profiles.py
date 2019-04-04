# sgmarine_company_profiles.py (using python2.7)

from pymongo import MongoClient
import json
# import datetime

client = MongoClient('mongodb://localhost:27017/')
mydb = client['test_db_py_01']
my_collection2 = mydb['test_db_py_01']

company_profiles_data = []

with open("./company_profiles.json", 'r') as infile:
    list_contents = json.load(infile)

    for item in list_contents:
      company_profiles_data.append(item)

# unique data
# company_profiles_data = list(set(company_profiles_data))
print(company_profiles_data)

mydb.my_collection3.insert(company_profiles_data)

print(mydb.collection_names())