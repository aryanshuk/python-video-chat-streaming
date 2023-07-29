import socket
import cv2
import numpy as np


def receive_frames():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Use the server's IP address or 'localhost'
    port = 12345

    try:
        client_socket.connect((host, port))
    except:
        print("Connection failed.")
        return

    cv2.namedWindow("Live Video from Server : Press Esc to exit")

    while True:
        # Change the buffer size based on frame size and compression
        data = client_socket.recv(921600)
        if not data:
            break
        # Update the shape based on your camera resolution
        frame = np.frombuffer(data, dtype=np.uint8).reshape(480, 640, 3)
        cv2.imshow("Live Video from Server : Press Esc to exit", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
            break

    cv2.destroyAllWindows()
    client_socket.close()


if __name__ == "__main__":
    receive_frames()
