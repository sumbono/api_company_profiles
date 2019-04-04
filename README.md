# api_company_profiles
This app created using Python with Flask framework.

This app serve GET API to provide sgmaritime company profiles data.

## Prerequisite
Install python on your machine. You can use [python](https://www.python.org/) or [anaconda](https://www.anaconda.com/).

Install flask:
```bash
#if using pip:
pip install -U Flask

#if using anaconda
conda install -c anaconda flask
```

## Usage
Firstly download or clone this repo.

### Run the app
On your command line:
```bash
python api_sgmarine_comp_prof.py
```
and the app will serve http://localhost:5000

#### GET all company profiles:
to fetch all companies profiles use this url endpoint on the command line:
```
curl http://localhost:5000/companies
```
or you can use postman and get data with the url.

#### GET one company profile:
to fetch the company profiles you want, use company name at this url endpoint on the command line:
```
curl http://localhost:5000/companies?company_name=kurita-singapore-pte-ltd
```
and you will get KURITA (SINGAPORE) PTE LTD company profiles.
