import re
import requests

KEY_ICON = requests.get('https://amo.sh/I/HQ8G2K/TTW5EI')
TOKEN_ICON = re.search(r"token: '(.+)'", KEY_ICON.text).group(1)

