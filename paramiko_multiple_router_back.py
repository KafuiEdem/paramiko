import myparamiko
from datetime import datetime
import threading


#backup function
def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.ssh_shell(client)
    myparamiko.send_command(shell,"termi leng 0")
    myparamiko.send_command(shell,"enable")
    myparamiko.send_command(shell,"cisco")
    myparamiko.send_command(shell,"sh run")
    output = myparamiko.show(shell)

    output_list = output.splitlines()

    output_list = output_list[10:-1]
    output_ = "\n".join(output_list)

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    #how the backups will be named
    file = f"{router['server_ip']}_{year}-{month}-{day}_.txt"
    with open(f"data_serialization\paramiko\{file}","w") as f:
        f.write(output_)

    myparamiko.close(client)

router1 = {"server_ip":"192.168.123.10","login":"edem","passwd":"cisco","port_num":"22"}
router2 = {"server_ip":"192.168.123.20","login":"edem","passwd":"cisco","port_num":"22"}
router3 = {"server_ip":"192.168.123.30","login":"edem","passwd":"cisco","port_num":"22"}
# router3 = {"server_ip":"192.168.123.2","login":"edem","passwd":"cisco","port_num":"22"}
routers = [router1,router2,router3]

#creating a list of thrads
thread = list()
for router in routers:
    th = threading.Thread(target=backup,args=(router,))
    thread.append(th)

for th in thread:
    th.start()

for th in thread:
    th.join()