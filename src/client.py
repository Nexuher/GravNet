import sys
import socket
import threading
import random
import time

import constants

class Client:

    def __init__(self, username):
        self.username = username

        self.print_client_info()

        self.chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_the_server()


    def print_client_info(self):
        print(f"CLIENT {self.username} CLIENT {self.username} CLIENT {self.username} CLIENT {self.username}")


    def connect_to_the_server(self):
        # Connect to the server
        try:
            self.chat_socket.connect((constants.HOST,constants.PORT))
            print(f"connected to server")
        except:
            print(f"Unable to connect {constants.HOST}:{constants.PORT} EXITING")
            exit(0)

        t1 = threading.Thread(target=self.start_listening_to_incoming_messages)
        t2 = threading.Thread(target=self.start_waiting_for_user_input)

        t1.start()
        t2.start()

        # Send welcome message to the server
        self.send_message(self.username)
        print(self.username)


        print("Connected to the server.")


    def start_listening_to_incoming_messages(self):
        print("start_listening_to_incoming_messages")
        while True:
            message = self.chat_socket.recv(2048).decode('utf-8')

            if message != '':
                decoded_nickname = message.split("~")[0]
                decoded_message = message.split("~")[1]

                if decoded_nickname == self.username:
                    continue

                print(f"[{decoded_nickname}] {decoded_message}")


    def start_waiting_for_user_input(self):
        print("start_waiting_for_user_input")
        while True:
            # message = input()
            # if message != "":
            #     self.send_message(message)

            wait_time = random.randint(1, 4)
            time.sleep(wait_time)

            self.send_message("AHAHAHAHHAA" * random.randint(1, 3))


    def send_message(self, message):
        if message == '':
            print("Message can't be empty!")
            pass

        self.chat_socket.sendall(message.encode())


if __name__ == "__main__":
    client_name = sys.argv[1]

    new_client = Client(client_name)
