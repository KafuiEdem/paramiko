import paramiko
import getpass
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass("Enter password:")

linux = {"hostname":"192.168.123.200","username":"edem","password":password,"port":"22"}
print(f"Connting to {linux['hostname']}")
ssh_client.connect(**linux,allow_agent=False,look_for_keys=False)
shell = ssh_client.invoke_shell()
shell.send("ls\n")
time.sleep(2)
output = shell.recv(10000).decode()
print(output)

if ssh_client.get_transport().is_active() == True:
    ssh_client.close()