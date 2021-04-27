import paramiko

import sys

results = []

def ssh_conn():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('<ipaddress>', username='username',password='password')

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('uptime')

    for line in ssh_stdout:
        results.append(line.strip('\n'))


ssh_conn()

for i in results:
    print(i.strip())

sys.exit()
