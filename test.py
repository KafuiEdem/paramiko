import paramiko
import time
import getpass


ssh_client = paramiko.SSHClient()

password = getpass.getpass("Enter password:")
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname="192.168.123.2",username="edem",password="cisco",port="22",look_for_keys=False,allow_agent=False)

router = {"hostname":"192.168.123.2","username":"edem","password": password,"port":"22"}
ssh_client.connect(**router,look_for_keys=False,allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int br\n')
time.sleep(1)
output = shell.recv(10000)
# print(type(output))
output = output.decode("utf-8")
print(output)
if ssh_client.get_transport().is_active() == True:
    print("Closing connection")
    ssh_client.close()