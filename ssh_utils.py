import paramiko


def connect_to_box (server, username, password,timeout=3) :
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username= username, password= password,timeout=timeout)
    except Exception,e:
        print e
        return None
    return ssh

def sftp_copy(ssh_session,from_path,to_path):
	try:
		sftp = ssh_session.open_sftp()
		sftp.put(from_path,to_path)
	except Exception,e:
		print e
		return "Error while copying file"

def execute(ssh_session,cmd):
	(stdin,out,err)=ssh_session.exec_command(cmd)
	if len(err.read()):
		return "Error while executing command"
	return out.read().splitlines()


if __name__=='__main__':
	# ssh to remote machine
	ssh_session = connect_to_box('127.0.0.1','user','password')

	# test copy from local machine to remote
	sftp_copy(ssh_session, "/home/ubuntu/test.txt", "/tmp/test.txt")

	# lets try some linux command execute
	result = execute(ssh_session, "free | grep Mem | awk '{print $3/$2 * 100.00}'")
	print result
