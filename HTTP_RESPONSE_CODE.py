import requests

myFile = open("Your list of URLs here, one per line", "r")
weblist = myFile.readlines()
weblist = list(map(lambda s: s.strip(), weblist))

i = 0
while i < len(weblist):
    try:
        request = requests.head(weblist[i])
        print(request.status_code)
    except requests.ConnectionError:
        print("failed to connect")
    i = i + 1