# api_sgmarine_comp_prof.py (using python2.7)

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.json_util import dumps
# from bson import json_util
# import json

############################
output = {}
list_of_key = ['company_url', 'company name', 'company email', 'company website', 'company phone number', 'company address', 'country', 'contacts', 'company description', 'products and services', 'category']

def checkKey(dict, key): 
      
    if key in dict.keys():
        output[key] = dict[key] 
    # else: 
    #     print("Not present")
############################

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test_db_py_01'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_db_py_01'

mongo = PyMongo(app)

# General endpoint:
"""
Example Endpoint:
[1] Fetch all data without query: /companies
[2] Fetch one data with query: /companies?company_name=asp-ship-management-group
"""

@app.route("/companies", methods=['GET'])
def fetch_companies():
    """
      Function to fetch the companies profiles.
    """
    # define the mongodb collection source
    comp = mongo.db.my_collection3

    # output = {}

    try:
        # If dictionary is not empty
        if request.args.get('company_name'):
            # get the query params
            company_name = request.args.get('company_name')
            # print(company_name)
            comp_url = "https://www.sgmaritime.com/companies/" + company_name

            # Fetch all the record(s)
            cp = comp.find_one({'company_url' : comp_url})
            print(cp)

            # Check if the records are found
            if cp:
                if cp['_id']: output['id'] = str(cp['_id'])
                
                for key in list_of_key:
                    checkKey(cp, key)

                print(output)

                return jsonify({
                'status_code': 200,
                'message': "successful",
                'data' : [output]
                })

            else:
                return jsonify({
                'data': []
                })

        # If dictionary is empty
        else:
            # Fetch all the record(s)
            cp_all = comp.find()
            print(cp_all.count)
            output_this = {}
            output_all = []

            # Return all the records as query string parameters are not available
            if cp_all.count > 0:

                for el_dict in cp_all:
                    k = el_dict.keys()
                    v = el_dict.values()
                    for kunci in k:
                        if kunci in list_of_key:
                            index_kunci_di_lok = list_of_key.index(kunci)
                            index_kunci_di_k = k.index(kunci)
                            k[index_kunci_di_k] = list_of_key[index_kunci_di_lok]
                    
                    index_id_di_k = k.index('_id')
                    k[index_id_di_k] = 'id'
                    v[index_id_di_k] = str(v[index_id_di_k])

                    output_this = dict(zip(k, v))
                    print(output_this)
                    output_all.append(dict(output_this))
                
                print(output_all)

                return jsonify({
                'status_code': 200,
                'message': "successful",
                'data' : output_all
                })
            else:
                # Return empty array if no users are found
                return jsonify({
                'data': []
                })
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500

if __name__ == '__main__':
    app.run(debug=True)