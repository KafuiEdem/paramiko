"""
Challenge #9
Create a Python script that connects to a Cisco Router using SSH and Paramiko and executes a list of commands. The commands are saved in a Python list.
An example of a list with commands to execute:
# the second element (cisco) is the enable command
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user']
"""
import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("connectiong to 192.168.123.2...")
ssh_client.connect(hostname="192.168.123.2",username="edem",port="22",password="cisco",look_for_keys=False,allow_agent=False)
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal length 0', 'sh run | i user','wr']

#invoking the active shell
shell = ssh_client.invoke_shell()

for command in commands:
    shell.send(f"{command}\n")
    time.sleep(1)
output = shell.recv(100000).decode()

print(output)

#closing the active ssh session
if ssh_client.get_transport().is_active()==True:
    print("Closing the ssh connection")
    ssh_client.close()