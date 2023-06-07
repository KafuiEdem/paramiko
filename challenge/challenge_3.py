"""
Challenge #3
Change the solution from Challenge #1 so that it will save the output to a file instead of printing it.
"""
import paramiko
from getpass import getpass
import time 

#getting the paramiko ssh client 
ssh_clinet = paramiko.SSHClient()
ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#getting the SSH Password of the user
password = getpass("Enter SSH password:")
#getting the parameter for the remote device
router = {"hostname":"192.168.123.2","username":"edem","password":password,"port":"22"}
#connting to the remote device 
print(f"Conecting to {router['hostname']}....")
ssh_clinet.connect(**router,look_for_keys=False,allow_agent=False)
#invoking an active shell
shell = ssh_clinet.invoke_shell()
#sending command to the remote devic
shell.send("term len 0\n")
shell.send("ena \n")
shell.send(f"{password}\n")
shell.send("sh users\n")
time.sleep(2)
output = shell.recv(10000).decode()
output_list=output.splitlines()[5:-1]
file = '\n'.join(output_list)

#writing the output to file
print("Writing output to file....")
print(file)
with open("data_serialization\paramiko\challenge\\file.txt",'w') as f:
    f.write(file)
#closing the ssh session
if ssh_clinet.get_transport().is_active()==True:
    print(f"Closng the connection to {router['hostname']}...")
    ssh_clinet.close()