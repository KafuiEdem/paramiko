"""
    Challenge #16
    Change the solution from Challenge #13 to use multithreading and automate the configuration of the routers concurrently.
"""
import myparamiko_13
import threading

#getting files with task path
ospf = "data_serialization\paramiko\challenge\\ospf.txt"
eigrp = "data_serialization\paramiko\challenge\\eigrp.txt"
router3_ = "data_serialization\paramiko\challenge\\router3.conf"

router1 = {"server_ip":"192.168.123.10","server_username":"edem","passwd":"cisco","server_port":"22",'config':ospf}
router2 = {"server_ip":"192.168.123.20","server_username":"edem","passwd":"cisco","server_port":"22",'config':eigrp}
router3 = {"server_ip":"192.168.123.30","server_username":"edem","passwd":"cisco","server_port":"22",'config':router3_}

routers = [router1,router2,router3]



def execute_command(router):
    ssh_client = myparamiko_13.connect(server_ip=router["server_ip"],server_username=router["server_username"],server_port=router["server_port"],passwd=router["passwd"])
    shell = myparamiko_13.get_shell(ssh_client)
    with open(router["config"],'r') as f:
        output = f.read()
        myparamiko_13.command_send(shell,"ter len 0")
        myparamiko_13.command_send(shell,output,timeout=4)
        myparamiko_13.show(shell)
        myparamiko_13.close(ssh_client)

thread = list()

for router in routers:
    th = threading.Thread(target=execute_command,args=(router,))
    thread.append(th)

for th in thread:
    th.start()

for th in thread:
    th.join()