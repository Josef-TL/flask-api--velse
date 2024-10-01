import requests

def get_repo_list(username):
    url = f'https://api.github.com/users/{username}/repos'
    req = requests.get(url)
    j = req.json()
    repo_list = []
    [repo_list.append(i['name']) for i in j]
    return repo_list

