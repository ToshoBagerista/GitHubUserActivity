import requests, json

def get_data(name):
	response = requests.get(f'https://api.github.com/users/{name}/events')
	if response.status_code != 200:
		return
	return response.json()

with open('data.json', 'w') as file:
	json.dump(get_data('ToshoBagerista'), file, indent=4)

print(get_data('ToshoBagerista'))