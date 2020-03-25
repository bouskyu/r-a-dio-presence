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
    if dj == "Hanyuu-sama":
        large_image = "hanyuu"
    elif dj == "Claud":
        large_image = "claud"
    elif dj == "apt-get":
        large_image = "apt-get"
    elif dj == "kipukun":
        large_image = "kipukun"
    elif dj == "Suzubrah":
        large_image = "suzubrah"
    elif dj == "exci":
        large_image = "exci"
    elif dj == "Wessie":
        large_image = "wessie"
    elif dj == "Vin":
        large_image = "vin"
    elif dj == "ed":
        large_image = "ed"
    rpc.update(state=np, details=dj + " playing at r-a-d.io",large_image=large_image,large_text="Tune in!")
    time.sleep(15)
