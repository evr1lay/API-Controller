import subprocess

from requester import Requester

url = "http://localhost:8000/messages"
req = Requester(url=url)

def show_menu():
    subprocess.run("cls", shell=True, check=False)
    print(f"[X] API STATUS: {req.is_api_running()}.\n"
        "[1] Turn on API.\n"
        "[2] GET.\n"
        "[3] POST.\n"
        "[4] Exit.\n")

if __name__ == "__main__":
    while True:
        show_menu()

        try:
            user_choice = int(input("Your choice: "))
        except ValueError:
            input("Number please! Press Enter to continue")
            continue

        match user_choice:
            case 1:
                pass
            case 2:
                subprocess.run("pause", shell=True, check=False)
            case 3:
                pass
            case 4:
                break
