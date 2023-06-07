import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#getting the password from the user
password = getpass.getpass("Enter password:")
#setting up the ssh connecting parameters.
linux = {"hostname":"192.168.123.200","username":"edem","password":password,"port":"22"}
print(f"Connecting to {linux['hostname']}")
ssh_client.connect(**linux,allow_agent=False,look_for_keys=False)

stdin,stdout,stderr = ssh_client.exec_command("sudo useradd u2\n",get_pty=True)
stdin.write(f"{password}\n")
time.sleep(2)
stdin,stdout,stderr = ssh_client.exec_command("cat /etc/passwd | grep u2\n")
print(stdout.read().decode())
time.sleep(1)


if ssh_client.get_transport().is_active() == True:
    print("Closing connection")
    ssh_client.close()