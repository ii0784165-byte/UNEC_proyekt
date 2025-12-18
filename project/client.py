import socket
from security import encrypt_message, decrypt_message

HOST = "127.0.0.1"
PORT = 12345

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    try:
        print(client.recv(1024).decode(), end="")
        client.send(input().encode())

        print(client.recv(1024).decode(), end="")
        client.send(input().encode())

        print(client.recv(1024).decode())

        while True:
            msg = input("You: ")

            if not msg.strip():
                print("⚠️ Boş mesaj olmaz")
                continue

            client.send(encrypt_message(msg))
            print("Server:", decrypt_message(client.recv(1024)))

    except Exception as e:
        print("❌ Xəta:", e)

    finally:
        client.close()
