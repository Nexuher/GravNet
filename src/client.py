import sys
import socket
import threading
import random
import time

import msg_formats
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
            print(f"Connected to server")
        except:
            print(f"Unable to connect {constants.HOST}:{constants.PORT} EXITING")
            exit(0)

        t1 = threading.Thread(target=self.start_listening_to_incoming_messages)
        t2 = threading.Thread(target=self.start_waiting_for_user_input)

        t1.start()
        t2.start()

        # Send welcome message to the server
        self.send_message(self.username)

        print("Connected to the server.")


    def start_listening_to_incoming_messages(self):
        while True:
            decoded_message = self.chat_socket.recv(2048).decode('utf-8')

            if decoded_message != '':
                message_timestamp, username, message = msg_formats.split_standard_message(decoded_message)

                if username == self.username:
                    continue

                print(f"[{message_timestamp}] <{username}>: \n{message}")


    def start_waiting_for_user_input(self):
        if constants.ENABLE_SPAM_TESTING:
            self.run_spam_testing()
        else:
            while True:
                message = input()
                if message != "":
                    self.send_message(message)

    def send_message(self, message):
        if message == '':
            print("Message can't be empty!")
            pass

        self.chat_socket.sendall(message.encode())

    def run_spam_testing(self):
        while True:
            message = "AHAHAHAHHAA" * random.randint(1, 3)
            wait_time = random.randint(1, 4)
            time.sleep(wait_time)
            #print(">>" + message)
            self.send_message(message)

if __name__ == "__main__":
    client_name = sys.argv[1]

    new_client = Client(client_name)
