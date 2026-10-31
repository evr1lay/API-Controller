import json
import os
import subprocess

import requests

from requester import Requester

def clear() -> None:
    subprocess.run(
        ["cls"] if os.name == "nt" else ["clear"],
        shell=False,
        check=False,
    )

def show_menu(url):
    clear()
    print(f"Choice http-method for {url}\n"
        "[1] Get.\n"
        "[2] Post.\n"
        "[3] Patch.\n"
        "[4] Delete.\n"
        "[5] Exit.\n")

if __name__ == "__main__":
    clear()
    url = input("Your API URL: ")
    req = Requester(url=url)

    while True:
        if req.is_api_running() != True:
            input("API is not running...")
            break

        show_menu(req.url)

        try:
            user_choice = int(input("Your choice: "))
        except ValueError:
            input("Number please! Press Enter to continue...")
            continue

        clear()

        match user_choice:
            case 1:
                response = req.get()
                print(response.text)
                subprocess.run("pause", shell=True, check=False)
            case 2:
                print('Preview: {"endpoint": "value"}')
                raw = input('Payload: ').strip()

                if not raw.startswith("{"):
                    raw = "{" + raw + "}"

                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    print("Invalid JSON")
                    subprocess.run("pause", shell=True, check=False)
                    continue

                try:
                    response = req.post(payload=payload)
                    print("Successful!")
                except requests.exceptions.RequestException as e:
                    print(f"Request failed: {e}")

                subprocess.run("pause", shell=True, check=False)
            case 3:
                for_update_id: int | str = input("Content ID: ")

                print('Preview: {"endpoint": "value"}')
                raw = input('Payload: ').strip()

                if not raw.startswith("{"):
                    raw = "{" + raw + "}"

                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    print("Invalid JSON")
                    subprocess.run("pause", shell=True, check=False)
                    continue

                try:
                    response = req.patch(id=for_update_id, payload=payload)
                    print("Successful!")
                except requests.exceptions.RequestException as e:
                    print(f"Request failed: {e}")

                subprocess.run("pause", shell=True, check=False)
            case 4:
                for_delete_id: int | str = input("Content ID: ")

                try:
                    response = req.delete(for_delete_id)
                except requests.exceptions.RequestException as e:
                    print(f"Request failed: {e}")

                subprocess.run("pause", shell=True, check=False)
            case 5:
                input("bye...")
                break
            case _:
                input("Invalid choice...")
