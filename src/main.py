import json
import subprocess
from time import sleep

from requester import Requester


def show_menu(url):
    subprocess.run("cls", shell=True, check=False)
    print(f"Choice http-method for {url}\n"
        "[1] Get.\n"
        "[2] Post.\n"
        "[3] Patch.\n"
        "[4] Delete.\n"
        "[5] Exit.\n")

if __name__ == "__main__":
    subprocess.run("cls", shell=True, check=False)
    url = input("Your API URL: ")
    req = Requester(url=url)

    while True:
        show_menu(req.url)

        try:
            user_choice = int(input("Your choice: "))
        except ValueError:
            input("Number please! Press Enter to continue...")
            continue

        subprocess.run("cls", shell=True, check=False)

        match user_choice:
            case 1:
                response = req.get()
                print(response.text)
                subprocess.run("pause", shell=True, check=False)
            case 2:
                print('Preview: "content": "Hello, World!"')
                raw = input("Payload (""): ")
                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    print("Invalid JSON")
                    continue

                response = req.post(payload=payload)
                if response != None and response.status_code == 200:
                    print("Successful!")
                else:
                    print("Response is None or something")

                subprocess.run("pause", shell=True, check=False)
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("bye")
                sleep(1.5)
                break
