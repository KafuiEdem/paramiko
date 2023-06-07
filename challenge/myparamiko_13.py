import paramiko
import time
from datetime import datetime
import getpass



def connect(server_ip,server_port,server_username,passwd):
    #connecting to the paramiko ssh client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {server_ip}...")
    ssh_client.connect(hostname=server_ip,username=server_username,port=server_port,password=passwd,look_for_keys=False,allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    #connecting the shell
    shell = ssh_client.invoke_shell()
    return shell

def command_send(shell,command,timeout=1):
    print(f'Sending command: {command}')
    #sending command to remote device
    shell.send(f"{command}\n")
    #allowing the process to sleep 
    time.sleep(timeout)

def show(shell,num=100000):
    #getting the output
    output = shell.recv(num).decode()
    print(output)

def close(ssh_client):
    #closing the active ssh connection
    if ssh_client.get_transport().is_active()==True:
        print("Closing connection")
        ssh_client.close()

#adding send_from_file() 
def send_from_file(shell,location,timeout):
    with open(f"{location}",'r') as f:
        file = f.read()
        command_send(shell,file,timeout)
    output = show(shell)
    print(output)

