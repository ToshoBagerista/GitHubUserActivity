import json, requests, sys


def get_data(name, repo=""):
	response = requests.get(f'https://api.github.com/users/{name}/events')
	if response.status_code != 200:
		return
	return response.json()

def main():
	if len(sys.argv) != 2:
		print(f"Usage: github_activity <username>")
		return
	
	apiData	= get_data(sys.argv[1])

	for i in apiData:
		if i['type'] == 'PushEvent':
			print(f"Pushed {len(i["payload"]["commits"])} to {i["repo"]["name"]}")
		elif i['type'] == 'PullRequestEvent': print(f"Pull Request in {i["repo"]["name"]}")
		elif i['type'] == 'CreateEvent': print(f"Created {i['payload']['ref_type']} in {i['repo']['name']}")
		elif i['type'] == 'DeleteEvent': print(f"Deleted {i['payload']['ref']} in {i['repo']['name']}")
		elif i['type'] == 'ForkEvent': print(f"Forked {i['repo']['name']}")
		elif i['type'] == 'WatchEvent': print(f"Starred {i['repo']["name"]}")
		elif i['type'] == 'PublicEvent': print(f"Public event in {i['repo']['name']}")
		else: print(f"Unknown event type: {i['type']}")

if __name__ == "__main__":
	main()