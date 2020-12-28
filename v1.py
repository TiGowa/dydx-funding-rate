from datetime import date
import requests, json, csv, inquirer
import pandas as pd

# Allow user to select the relevant market.
select = [
	inquirer.List('markets',
                message="Please select relevant market.",
                choices=['PBTC-USDC', 'WETH-PUSD', 'PLINK-USDC'],
            ),
		]

answer = inquirer.prompt(select)

user_choice = answer["markets"]

PARAMS = {"markets": user_choice, "limit": "100"}

response = requests.get('https://api.dydx.exchange/v1/historical-funding-rates', params=PARAMS)

data = response.json()

today = date.today()

with open('{}.txt'.format(today), 'w') as out_file:
	json.dump(data, out_file)

with open('{}.txt'.format(today), 'r') as my_file:
	my_data=my_file.read()

dic = json.loads(my_data)

my_list = (dic[user_choice]['history'])

with open('data.csv', 'w', newline='') as f:
	fieldnames = ['market', 'effectiveAt', 'fundingRate', 'fundingRate8Hr', 'averagePremiumComponent', 'averagePremiumComponent8Hr']
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(0, 100):
		writer.writerow(my_list[i])

# Get the last date of the dump. 
def get_last_date(my_list):
	max_range = len(my_list)
	n = max_range - 1
	parse = my_list[n]
	last_date = parse['effectiveAt']
	return last_date

# Get new query as limit equals 100.
def new_query(new_date):
	new_PARAMS = {"markets": user_choice, "limit": "100", "startingBefore": new_date}
	new_response = requests.get('https://api.dydx.exchange/v1/historical-funding-rates', params=new_PARAMS)
	new_data = new_response.json()
	file_name = str(new_date)
	with open('{}.txt'.format(file_name), 'w') as out_file:
		json.dump(new_data, out_file)
	with open('{}.txt'.format(file_name), 'r') as my_file:
		my_new_data=my_file.read()
	new_dic = json.loads(my_new_data)
	my_new_list = (new_dic[user_choice]['history'])
	with open('data.csv', 'a', newline='') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		for i in range(0, 100):
			writer.writerow(my_new_list[i])
    
	get_last_date(my_new_list)
	new_date = get_last_date(my_new_list)
	new_query(new_date)


new_date = get_last_date(my_list)

new_query(new_date)