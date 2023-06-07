"""
Challenge #2
Change the solution from Challenge #1 so that it will prompt the user for the SSH password securely (use getpass module). 
Run the script in the terminal (you can not run it in PyCharm).
"""
import paramiko
from getpass import getpass
import time

#caling the ssh demon using paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#prompting the user for ssh password
password = getpass("Enter SSH password:")

#geting the ssh device parameters
router = {"hostname":"192.168.123.2","username":"edem","password":password,"port":"22"}
#connting to the remote device 
print(f"Conecting to {router['hostname']}....")
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)
#invoking an active shell
shell = ssh_client.invoke_shell()

#sending commend to the remote device
shell.send("term len 0\n")
shell.send("ena \n")
shell.send(f"{password}\n")
shell.send("sh users \n")
time.sleep(2)
output = shell.recv(10000).decode()
print(output)

#closing the paramiko demon if a session is active
if ssh_client.get_transport().is_active()==True:
    print(f"Colsing the connectin to {router['hostname']}...")
    ssh_client.close()