import subprocess
import time

def Serveo_Link():
    subprocess.Popen("bash serveo_link.sh", shell=True)
    time.sleep(3)
    with open("serveo_output.txt", "r") as file:
        output = file.read()
    url = output.strip().split("https://")[1]
    print(f"    👉 Public URL: https://{url}")
