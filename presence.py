from pypresence import Presence 
import time
import requests 

client_id = ""
rpc = Presence(client_id)
rpc.connect()

url = "https://r-a-d.io/api"
rpc.clear()

while True:
    r = requests.get(url=url)
    data=r.json()
    np = data['main']['np']
    dj = data['main']['dj']['djname']
    dj_image = data['main']['dj']['djimage']
    thread = data['main']['thread']
    if dj_image = "Hanyuu":
        large_image = "hanyuu"
    elif dj_image = "Claud":
        large_image = "claud"
    elif dj_image = "apt-get":
        large_image = "apt-get"
    elif dj_image = "kipukun":
        large_image = "kipukun"
    elif dj_image = "Suzubrah":
        large_image = "suzubrah"
    elif dj_image = "exci":
        large_image = "exci"
    elif dj_image = "Wessie":
        large_image = "wessie"
    elif dj_image = "Vin":
        large_image = "vin"
    elif dj_image = "ed":
        large_image = "ed"
    rpc.update(state=np, details=dj + " playing at r-a-d.io",large_image=large_image,large_text="Tune in!")
    time.sleep(15)