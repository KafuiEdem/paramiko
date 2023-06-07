import paramiko
import getpass
import time


YES ="YES"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass("Enter password:")
ssh_client.connect(hostname="192.168.123.200",port="22",username="edem",password=password)
#ask the user to enter the name of the user to be crated
urser = input("Enter user to be crated:")
#let the user confirm his action
question = input(f"Are you sure you want to create this user {urser}? yes/no: ")

if question ==YES.lower():
    print(f"Creating the user {urser}...")
    time.sleep(1)
    #getting the shell
    stdin,stdout,stderr = ssh_client.exec_command(f"sudo useradd -m -d /home/{urser} -s /bin/bash {urser}\n",get_pty=True)
    stdin.write(f"{password}\n")
    time.sleep(2)
    stdin,stdout,stderr = ssh_client.exec_command("cat /etc/passwd")
    print(stdout.read().decode())
else:
    print(f"Creating of user {urser} has been aborted.")
#closing the ssh client 
if ssh_client.get_transport().is_active()==True:
    print(f"Closing the ssh client")
    ssh_client.close()
