#Script Powered by Amarant0s
#Script to copy files and folders using sftp protocol & Execute commands.
import paramiko
import sys
import time
import subprocess
import os
from sys import argv
#Set the home directory
home_dir = '/path'
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
#Set the username and password
username = 'username'
password = 'password'
#Create Log file
paramiko.util.log_to_file('log-path/ssh.log')
#script, ip_addr_file = argv
#Ip list of the tills
ip_addr_file = open('path/files-to-read-the-ip.txt' , 'r')
#Sets the loop of reading the ip list from file and create deirectories.
for host in ip_addr_file:
    host = host.strip()
    newfolder = (home_dir + '/' + host)
    print ('Folder Name ' + newfolder)
    if not os.path.exists(newfolder):
        os.makedirs(newfolder)
        os.chdir(newfolder)
    ssh.connect(hostname = host, username = username, password = password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('execute command')
    output = ssh_stdout.read()
    #sftp transfer
    sftp = ssh.open_sftp()
    sftp.get('local path', newfolder + '/' + 'nameoffile to create locally')
    #prints the output from terminal
    print output
    ssh.close()

