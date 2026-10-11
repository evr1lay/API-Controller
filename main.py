import subprocess
from time import sleep

from requester import Requester

url = "http://localhost:8000/messages"
req = Requester(url=url)

def show_menu():
    subprocess.run("cls", shell=True, check=False)
    print(f"[X] API STATUS: {"✅ ON" if req.is_api_running() else "⛔ OFF"}.\n"
        "[1] Turn on API. (WIP)\n"
        "[2] GET.\n"
        "[3] POST.\n"
        "[4] Exit.\n")

if __name__ == "__main__":
    while True:
        show_menu()

        try:
            user_choice = int(input("Your choice: "))
        except ValueError:
            input("Number please! Press Enter to continue...")
            continue

        subprocess.run("cls", shell=True, check=False)

        match user_choice:
            case 1:
                pass
            case 2:
                response = req.get()
                print(response.json())

                subprocess.run("pause", shell=True, check=False)
            case 3:
                content = str(input("Your content: "))
                response = req.post(content)
                print("Successful!" if response.status_code == 200 else "Errors.")

                subprocess.run("pause", shell=True, check=False)
            case 4:
                print("bye")
                sleep(1.5)
                break
