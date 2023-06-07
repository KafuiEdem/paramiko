import paramiko
import getpass
import time

#setting up the ssh client service of paramiko
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#getting the password of the using the getpass module
password = getpass.getpass("Enter password:")

#seting the parameter for the host.
linux = {"hostname":"192.168.123.200","username":"edem","password":password,"port":"22"}
#connecting to the host 
ssh_client.connect(**linux,allow_agent=False,look_for_keys=False)
stdin,stdout,stderr = ssh_client.exec_command("ifconfig\n")

output = stdout.read()
output = output.decode()
print(output)

#executing another command
stdin,stdout,stderr = ssh_client.exec_command("who\n")
time.sleep(0.5)
output = stdout.read()
output = output.decode()
print(output)


if ssh_client.get_transport().is_active()==True:
    print("Closing connection")
    ssh_client.close()