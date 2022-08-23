from re import findall, search
from random import choice
from time import sleep
from os import mkdir
import requests


print( """   
           
     \033[1;92m  ______              _                         
      \033[1;92m(_____ \            (_)                        
       \033[1;92m_____) )_____ _   _ _ ____  _____  ____  _____ 
      \033[1;92m|  __  /| ___ | | | | |    \(____ |/ _  | ___ |
      \033[1;92m| |  \ \| ____|\ V /| | | | / ___ ( (_| | ____|
      \033[1;92m|_|   |_|_____) \_/ |_|_|_|_\_____|\___ |_____)
                                        \033[1;92m(_____|                                                                   
                                                                                                         
   \033[1;93m < \033[1;92mTHE TOOL IS FREE\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mAUTHOR     : TheNooB
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mTelegram   : TheN0oB
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB     : GITHUB.COM/TheNooB\033[1;91m
 ---------------------------
""")

print("\n\033[1m\033[1;96m > Simple script that can find similar images from an image")
print(" > Reversing and scraping yandex.com APIs!")
print(" > Made for you by: [t.me/TheN0oB] [github.com/TheNooB4]\n")
print(" > You can close session with ctrl + z when you're okay\n")
photo = input("  [Input] Enter your photo name or path: ").strip()



def upload():
    try:
        response = requests.post('https://yandex.com/images-apphost/image-download', data=open(photo, "rb"),
        params={'cbird': '111', 'images_avatars_size': 'preview', 'images_avatars_namespace': 'images-cbir'}, 
        headers={'device-memory': '8', 'downlink': '10',
        'ect': '4g', 'referer': 'https://yandex.com/images/',
        'rtt': '100', 'viewport-width': '843', 'dpr': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
        try: return(str(response.json()['image_shard'])+'/'+str(response.json()['image_id']))
        except KeyError: return False
    except FileNotFoundError:
        print(" [Output] Photo not found!")
        sleep(4);exit()


def photos():
    token = upload()
    if not token: return False
    response = requests.get(f"https://yandex.com/images/search?rpt=imageview&url=https://avatars.mds.yandex.net/get-images-cbir/{token}/orig&cbir_id={token}&cbir_page=similar",
    headers={'device-memory': '8', 'downlink': '9.75','dpr': '1', 'ect': '4g',
    'rtt': '100', 'viewport-width': '1920', 'referer': 'https://yandex.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
    results = findall(r'//avatars\.mds\.yandex.net\/i\?id=[^"]+', response.text)
    if not results: return False
    return results


files = photos()
if not files: 
    print(" \033[1;93m[Output] Something went wrong!")
    sleep(4);exit()

else:
    results_file = "".join([choice("QAZWSXEDCRFVTGBYHNUJMIKLOP1234567890") for i in range(6)])
    mkdir(results_file)
    print(f'\n [Output] All Photos will saved in [ {results_file} ] Folder\n')
    for file in files:
        name = search("\?id=([^-]+)", file).group(1)
        print(f' [Output] Saving {name[:6]}.png..')
        with open(f'{results_file}/{name[:6]}.png', 'wb') as save:
            try: save.write(requests.get(f'https:{file}').content)
            except: continue
