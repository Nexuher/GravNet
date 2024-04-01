import socket
import threading
import random

import time_info
import constants
import msg_formats

class Server:

    def __init__(self):
        
        self.chat_socket = self.create_socket()
        self.connected_clients = {} # dict of username : client objects

        self.initialize_server()
        self.start_listening()


    def create_socket(self):
        # AF_INET:       IPv4 adresses
        # SOCK_STREAM:   TCP packets for communication
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return new_socket


    def initialize_server(self):
        
        try:
            # Provide the server with adress in host:port format
            self.chat_socket.bind((constants.HOST, constants.PORT))
        except:
            print(f"Unable to bind to host {constants.HOST}:{constants.PORT}")
            exit(0)
        
        # Server limit
        self.chat_socket.listen(constants.CLIENT_LIMIT)

        print(f'Running the server on {constants.HOST} {constants.PORT}. Max client limit: {constants.CLIENT_LIMIT}')


    def start_listening(self):
        while True:
            # adress[0] = host, adress[1] = port
            client_object, address = self.chat_socket.accept()

            print(f"Client connected to the server: {address[0]}:{address[1]}")

            threading.Thread(target=self.handle_connected_client, args=(client_object, )).start()

    def handle_connected_client(self, client_object):
        # First incoming message is client username
        client_username = self.try_get_message(client_object) + self.generate_hashtag()

        print(client_username)

        # Setup new client
        self.connected_clients[client_username] = client_object
        user_joined_announcement_msg = msg_formats.get_server_announcement_message(time_info.return_current_time(), f"{client_username} joined the chat")
        print(user_joined_announcement_msg)
        self.send_server_announcement(user_joined_announcement_msg)

        # Keep listening for messages incoming from this client
        while True:
            try:
                message = self.try_get_message(client_object)
            except:
                del self.connected_clients[client_username]
                user_left_announcement_msg = msg_formats.get_server_announcement_message(time_info.return_current_time(), f"{client_username} left the chat")
                print(user_left_announcement_msg)
                self.send_server_announcement(user_left_announcement_msg)
                break
            
            formatted_message = msg_formats.get_standard_message(time_info.return_current_time(), client_username, message)
            print(formatted_message)
            self.send_server_announcement(formatted_message)


    def try_get_message(self, client_object):
        while True:
            message = client_object.recv(2048).decode('utf-8')

            if message != '':
                return message
            else:
                print(f"> {message}")
            

    def send_message(self, client_object, message):
        client_object.sendall(message.encode())


    def send_server_announcement(self, announcement_message):
        for client_object in self.connected_clients.values():
            self.send_message(client_object, announcement_message)
    
    def generate_hashtag(self):
        hashtag = "#"
        for number in range(constants.GUID_LENGTH):
            hashtag += str(random.randint(0,9))
        
        return hashtag
                        

if __name__ == "__main__":
    print("SERVER SERVER SERVER SERVER SERVER SERVER SERVER SERVER")
    new_server = Server()