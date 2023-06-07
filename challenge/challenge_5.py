"""
Challenge #5
Create a Python script that connects to a Cisco Router using SSH and Paramiko, enters the enable mode, and then executes show running-config
The entire output should be saved to a file in the current working directory.
"""
import paramiko
import time
from getpass import getpass
from datetime import datetime

#getting the ssh clint
ssh_clinet = paramiko.SSHClient()
ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#getting the ssh password
password = getpass("Enter SSH password:")
#getting the parameter for the remote device
router = {"hostname":"192.168.123.2","username":"edem","password":password,"port":"22"}
#connting to the remote device 
print(f"Conecting to {router['hostname']}....")
ssh_clinet.connect(**router,allow_agent=False,look_for_keys=False)

#invoking an active shell
shell = ssh_clinet.invoke_shell()
#sending command to the remote devcie
shell.send("term len 0\n")
shell.send("ena \n")
shell.send(f"{password}\n")
shell.send("sh run \n")
time.sleep(2)
output = shell.recv(100000).decode()
output_list=output.splitlines()[5:-1]
file = '\n'.join(output_list)
now = datetime.now()
year = now.year
month = now.month
day = now.day
backup = f"{router['hostname']}_{year}_{month}-{day}"
print("Wrinting to file")
with open(f"data_serialization\paramiko\challenge\\{backup}.txt",'w') as f:
    f.write(file)
#closing the ssh connection
if ssh_clinet.get_transport().is_active() == True:
    print("Closing the connection")
    ssh_clinet.close()