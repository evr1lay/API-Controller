import subprocess

from api import api_on
from requester import Requester

url = "http://localhost:8000/messages"
req = Requester(url=url)

def show_menu():
    print(f"[-] API STATUS: {req.is_api_running()}.\n"
        f"[1] GET - {url}.\n"
        f"[2] POST - {url}.\n"
        "[3] Exit.\n")

if __name__ == "__main__":
    show_menu()
    user_choice = int(input("Your choice: "))

    match user_choice:
        case 1:
            subprocess.run("")
