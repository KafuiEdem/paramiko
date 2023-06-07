"""
Challenge #10
Create a Python script that connects to a Cisco Router using SSH and Paramiko and executes all the commands from a text file.
"""
import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("connectiong to 192.168.123.2...")
ssh_client.connect(hostname="192.168.123.2",username="edem",port="22",password="cisco",look_for_keys=False,allow_agent=False)

#invoking shell

shell = ssh_client.invoke_shell()

#reading commands from script.txt
with open("data_serialization\paramiko\challenge\\script.txt",'r') as f:
    file = f.read()
    shell.send("term len 0\n")
    shell.send(f"{file}\n")
    time.sleep(3)
    output = shell.recv(100000).decode()
    print(output)

if ssh_client.get_transport().is_active()==True:
    print("closing connection")
    ssh_client.close()