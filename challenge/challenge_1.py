"""
    Create a Python script that connects to a Cisco Router using SSH and Paramiko. 
    The script should execute the show users command in order to display the logged-in users.
    Print out the output of the command.
"""
import paramiko
from getpass import getpass
import time

#creating the ssh client
ssh_clinet = paramiko.SSHClient()
ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#connect to the paramiko ssh demon
router = {"hostname":"192.168.123.2","username":"edem","password":"cisco","port":"22"}
ssh_clinet.connect(**router,allow_agent=False,look_for_keys=False)
print(f"Connecting to {router['hostname']}")
#invoking the shell
shell = ssh_clinet.invoke_shell()
shell.send('terminal length 0\n')
shell.send("en\n")
shell.send("cisco\n")
shell.send("show users\n")
time.sleep(2)
output = shell.recv(100000).decode()

print(output)

#close the ssh connection if the ssh session is active
if ssh_clinet.get_transport().is_active()==True:
    print("closing the SSH connection")
    ssh_clinet.close()