"""
Challenge #14
Consider a topology with multiple devices like this one.
Create a function called execute_command() that takes 2 arguments: a dictionary with information about the device (ip, port, credentials) and a show command to execute on the device.
Using a for loop iterate over the routers in the topology and call the function for each router.
"""
import paramiko
import time
import threading

def execute_command(device:dict,command):
    #getting the ssh client
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Connecting to {device['hostname']}....")
    ssh_client.connect(**device,allow_agent=False,look_for_keys=False)

    #getting the shell
    shell = ssh_client.invoke_shell()
    
    #sending command
    print(f"sending command {command} to {device['hostname']}...")
    shell.send("ter len 0\n")
    shell.send(f"{command}\n")
    time.sleep(1)
    output = shell.recv(100000).decode()
    print(output)

    if ssh_client.get_transport().is_active()==True:
        print(f"Closing connection to {device['hostname']}")
        ssh_client.close()

if __name__== "__main__":
    router1 = {"hostname":"192.168.123.10","username":"edem","password":"cisco","port":"22"}
    router2 = {"hostname":"192.168.123.20","username":"edem","password":"cisco","port":"22"}
    router3 = {"hostname":"192.168.123.30","username":"edem","password":"cisco","port":"22"}
    routers = [router1,router2,router3]

    for router in routers:
        execute_command(router,"show ip int br | e un")



