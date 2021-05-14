import requests
import config
import urllib.parse


def login_util(username: str, password: str) -> str:
    url = f'https://{config.AUTH0_DOMAIN}/authorize?audience={urllib.parse.quote(config.API_AUDIENCE)}&response_type=token&client_id=k7ZEqOyBoPUs2zqw5xBHh1ytMrzpma67&redirect_uri=http%3A%2F%2Flocalhost%3A8100'
    session = requests.Session()
    a = session.get(url)
    state = a.url.split("=")[1]
    data = {'state': state,
            'username': username,
            'password': password, 'action': 'default'}
    b = session.post(a.url, data=data, allow_redirects=False)
    new_url = b.text
    new_url = new_url.replace('Found. Redirecting to ',
                              'https://happy2000.us.auth0.com')
    c = session.get(new_url, allow_redirects=False)
    token = c.text.split("=")[1].split("&")[0]
    return token
