import subprocess
import time

def Serveo_Link():
    max_attempts = 3
    attempts = 0
    url = None

    while attempts < max_attempts:
        subprocess.Popen("bash serveo_link.sh", shell=True)
        time.sleep(4)

        with open("serveo_output.txt", "r") as file:
            output = file.read()

        if "https://" in output:
            url = output.strip().split("https://")[1]
            break
        else:
            attempts += 1
            print(f"Serveo failed on attempt {attempts}. Retrying...")

    if url is not None:
        return url
    else:
        print("Serveo link retrieval failed after multiple attempts.")
        return None
