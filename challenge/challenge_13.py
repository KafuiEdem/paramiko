"""
Challenge #13
Consider a topology with multiple devices like this one.
For each device in the topology, you have a Python dictionary that stores the SSH connection information (IP, port, username, password) but also a filename that contains the commands to be sent to that device.
Example:
router1 = {'server_ip': '192.168.122.10', 'server_port': '22', 'user':'u1', 'passwd':'cisco', 'config':'ospf.txt'}
router2 = {'server_ip': '192.168.122.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco', 'config':'eigrp.txt'}
router3 = {'server_ip': '192.168.122.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco', 'config':'router3.conf'}

Create a Python script that connects to each device using SSH and Paramiko and executes the commands from the file (which is the value of the dictionary config key).
Use myparamiko.py that was developed in the course or create the script from scratch.
"""
import myparamiko_13 

#getting files with task path
ospf = "data_serialization\paramiko\challenge\\ospf.txt"
eigrp = "data_serialization\paramiko\challenge\\eigrp.txt"
router3_ = "data_serialization\paramiko\challenge\\router3.conf"

router1 = {"server_ip":"192.168.123.10","server_username":"edem","passwd":"cisco","server_port":"22",'config':ospf}
router2 = {"server_ip":"192.168.123.20","server_username":"edem","passwd":"cisco","server_port":"22",'config':eigrp}
router3 = {"server_ip":"192.168.123.30","server_username":"edem","passwd":"cisco","server_port":"22",'config':router3_}

routers = [router1,router2,router3]



for router in routers:
    ssh_client = myparamiko_13.connect(server_ip=router["server_ip"],server_username=router["server_username"],server_port=router["server_port"],passwd=router["passwd"])
    shell = myparamiko_13.get_shell(ssh_client)

    with open(router["config"],'r') as f:
        output = f.read()
        myparamiko_13.command_send(shell,"ter len 0")
        myparamiko_13.command_send(shell,output,timeout=4)
        myparamiko_13.show(shell)
        myparamiko_13.close(ssh_client)