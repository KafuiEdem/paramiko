"""
Challenge #7
A Network Engineer has created this Python script that executes show ip interface brief on a remote Cisco Router and displays the output.
However, instead of the normal output of the command (a string), it displays some sort of gibberish.
Your task is to troubleshoot the issue and solve it so that it displays the entire output.
"""

import paramiko
import time

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('Connecting to 192.168.123.2')
ssh_client.connect(hostname='192.168.123.2', port='22', username='edem', password='cisco',look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(100000).decode()#the solution is to add decode method to the recv method
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()