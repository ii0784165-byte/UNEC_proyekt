from server import start_server
from client import start_client

if __name__ == "__main__":
    choice = input("Server yoxsa Client? (s/c): ").lower()

    if choice == "s":
        start_server()
    elif choice == "c":
        start_client()
    else:
        print("Yanlış seçim")
