import paramiko
import time


"""
    This is a module that allows you to connect to a cisco device and issue 
    commands without stressing your mind.
"""

def connect(server_ip,login,passwd,port_num):
    """
    This function allows you to connect to the device
    """
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=server_ip,username=login,password=passwd,port=port_num,allow_agent=False,look_for_keys=False)
    print(f"connecting to {server_ip}")
    return ssh_client
    
def ssh_shell(ssh_client):
    """
        this function invoke the shell
    """
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell,commend,timeout=1):
    """
        This function sends command to the device
    """
    shell.send(commend +'\n')
    time.sleep(timeout)
    print(f"sending command [{commend}]\n")

def show(shell, n=10000):
    """
        This function shows the output of the command
    """
    output = shell.recv(n).decode()
    return output

def close(ssh_client):
    """
        This function closes the connection
    """
    if ssh_client.get_transport().is_active() == True:
        print("Closing connection")
        ssh_client.close()

if __name__=="__main__":
    client = connect(server_ip="192.168.123.2",login="edem",passwd="cisco",port_num="22")
    shell = ssh_shell(ssh_client=client)
    send_command(shell,"ena")
    send_command(shell,"cisco")
    send_command(shell,"terminal leng 0")
    send_command(shell,"sho ver")
    send_command(shell, "show ip int br")

    output = show(shell=shell)
    print(output)
