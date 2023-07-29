import socket
import cv2
import numpy as np
import threading


def send_frames(client_socket, addr):
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        data = frame.tobytes()
        try:
            client_socket.sendall(data)
        except:
            print(f"Client {addr} disconnected.")
            break
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 12345

    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server is listening for incoming connections...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")
            client_thread = threading.Thread(
                target=send_frames, args=(client_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server shutting down...")
        server_socket.close()


if __name__ == "__main__":
    main()
