import requests

resp = requests.get('https://api.github.com')
print(resp)
#200->success
#404->not found