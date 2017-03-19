import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://overwatch-a.akamaihd.net/img/pages/game/backgrounds/game_teams_center-d7d5f0437342f61298a1c2cc4ffbe81d13e70665347b3b470b430ab0dc167668217800f4cf51d2672a854d377faf5456bb25bace0ad8048e38d59c6d64e0f5d7.png")