
# A Python program to connect to a Network Device via SSH

# Importing sys library to perform sys.exit() to exit the program
import sys

# Importing paramiko library to connect to devices using SSH
import paramiko

# Importing getpass library to take password as input
from getpass import getpass


# Definition of sshconnect method
def sshconnect(ip, username, password):

    # Putting the connection command in try block to catch the exception
    try:

        # Calling connect method to SSH to the device
        ssh.connect(hostname=ip, username=username, password=password, timeout=5)

        # Notifying user upon successful connection
        print("\nSSH Connection Successful!\n")

        # Returning true upon successful connection
        return True

    # Catching error if connection was unsuccessful
    except:

        # Notifying user upon unsuccessful connection
        print('\nCould not connect via SSH.\n')

        # Returning false upon unsuccessful connection
        return False


# Definition of sshexec method
def sshexec(command):

    # Putting the connection command in try block to catch the exception
    try:

        # Notifying user of the status
        print("\nFetching requested information.\n")

        # Calling the exec_command method and collectingthe response
        input, output, error = ssh.exec_command(command, get_pty=True)

        # Using for loop to print the response line by line
        for line in output.readlines():

            # Striping the \n part from the output & printing the line
            print(line.strip())

    # Catching error if collecting information was unsuccessful
    except:

        # Notifying user upon unsuccessful collection
        print("Could not get the information.\n")


# Main program
# Putting the user input lines in try block to handle KeyboardInterrupt exception
try:

    # input methods to collect user inputs
    ip = input("\nEnter IP Address: ")
    username = input("Enter username for " + ip + ": ")
    password = getpass("Enter password for " + ip + ": ")

# except block to handle KeyboardInterrupt exception
except KeyboardInterrupt:

    # Notifying the user and exiting the program
    print("\nInput interrupted by user.\n")
    sys.exit()

# Creating SSH Client object using paramiko
ssh = paramiko.SSHClient()

# Adding ssh host key to the machine automatically to avoid the error
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Checking if the SSH was successful to proceed further
if sshconnect(ip, username, password):

    # Collecting user input to run command on the connected device
    cmd = input("Enter the command you want to execute on the device: ")

    # Prepending the entered command with vbash (This is only specific to VyOS and might not be required to other devices)
    cmd = 'vbash -c -i "' + cmd + '"'

    # Calling the sshexec() method passing the user command
    sshexec(cmd)

    # Closing the SSH session after executing the command
    ssh.close()

# if the SSH connection was unsuccessful, notifying & exiting program
else:
    print("Exiting program.\n")
