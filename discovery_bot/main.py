import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"

if __name__ == "__main__":
    tag = 'lasvegasfoodies'
    print('https://www.instagram.com/explore/tags/' + tag + '/?__a=1')
    x = requests.get(
        'https://www.instagram.com/explore/tags/' + tag + '/?__a=1', headers={"user-agent": USER_AGENT})
    print(x.json)
