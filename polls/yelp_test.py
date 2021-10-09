from dotenv import load_dotenv, find_dotenv
import requests, json, os


load_dotenv(find_dotenv())
print(os.getenv("connstring"))


YELP_API = os.getenv('YELP_API')
headers = {'Authorization': 'Bearer %s' % YELP_API}
business_id = 'FEVQpbOPOwAPNIgO7D3xxw'
url = 'https://api.yelp.com/v3/businesses/FEVQpbOPOwAPNIgO7D3xxw'.format(business_id)


response = requests.get(url, headers = headers)
business_date = response.json()
print(json.dumps(business_date, indent = 3))

