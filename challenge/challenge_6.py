"""
Challenge #6
A Network Engineer has created this Python script that executes show ip interface brief on a remote Cisco Router and displays the output.
Although the script connects and authenticates successfully, it doesn’t display the entire output of the command, but only a part of it.
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
#solution to solve the problem
shell.send("term len 0\n")
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(100000).decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()