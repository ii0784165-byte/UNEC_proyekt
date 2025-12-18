import socket
from security import encrypt_message, decrypt_message, hash_password

HOST = "127.0.0.1"
PORT = 12345

users_db = {
    "admin": hash_password("1234")
}

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("🟢 Server işə düşdü...")

    conn, addr = server.accept()
    print("🔗 Qoşulan:", addr)

    try:
        conn.send(b"Username: ")
        username = conn.recv(1024).decode()

        conn.send(b"Password: ")
        password = conn.recv(1024).decode()

        if username in users_db and users_db[username] == hash_password(password):
            conn.send(b"Login successful\n")
        else:
            conn.send(b"Login failed\n")
            conn.close()
            return

        while True:
            encrypted_msg = conn.recv(1024)
            if not encrypted_msg:
                break

            message = decrypt_message(encrypted_msg)
            print(f"{username}: {message}")

            conn.send(encrypt_message("Message received"))

    except Exception as e:
        print("❌ Xəta:", e)

    finally:
        conn.close()
