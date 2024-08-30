import socket
from threading import Thread
# Provides us with methods for interacting with the operating system.
import os

class Client:
  
  # When creating a client, connect to the server, ask for
  # a username, and begin server communication.
  def __init__(self, HOST, PORT):
    self.socket = socket.socket()
    self.socket.connect((HOST, PORT))
    self.name = input("Enter your name: ")
    
    self.talk_to_server()
    
  # First send over the name of the client. Then start listening
  # for messages on a separate thread. Message sending will be on
  # the main thread.
  def talk_to_server(self):
    self.socket.send(self.name.encode())
    Thread(target = self.receive_message).start()
    self.send_message()
    
  # Get user input and send the message to the server
  # with the client's name prepended.
  def send_message(self):
    while True:
      client_input = input("")
      client_message = self.name + ": " + client_input
      self.socket.send(client_message.encode())
      
  # Constantly listen out for messages. If the message is response
  # from the server is empty, close the program.
  def receive_message(self):
    while True:
      server_message = self.socket.recv(1024).decode()
      if not server_message.strip():
        os._exit(0)
      # Add some color to the console.
      print("\033[1;31;40m" + server_message + "\033[0m")
      
if __name__ == '__main__':
  Client('127.0.0.1', 7632)