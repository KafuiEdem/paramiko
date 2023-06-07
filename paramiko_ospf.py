import paramiko
import getpass
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass("Enter password:")#getting the password from the user

router1 = {"hostname":"192.168.123.10","username":"edem","password":password,"port":"22"}#setting the router login parameter
router2 = {"hostname":"192.168.123.20","username":"edem","password":password,"port":"22"}#setting the router login parameter
router3 = {"hostname":"192.168.123.30","username":"edem","password":password,"port":"22"}#setting the router login parameter

routers = [router1,router2,router3]

for router in routers:
    print(f"Connecting to {router['hostname']}")
    ssh_client.connect(**router,allow_agent=False,look_for_keys=False)#connecting to the ssh client
    #getting the output of the router on the shell
    shell = ssh_client.invoke_shell()
    shell.send("enable\n")
    shell.send("cisco\n")
    shell.send("config t\n")
    shell.send("router ospf 1\n")
    shell.send("net 0.0.0.0 0.0.0.0 area 0\n")
    shell.send("end\n")
    shell.send("terminal length 0\n")
    shell.send("sh ip protocols\n")
    time.sleep(10)
    output = shell.recv(10000).decode()
    print(output)

#closing the ssh client is there is an active session
if ssh_client.get_transport().is_active() == True:
    ssh_client.close()
