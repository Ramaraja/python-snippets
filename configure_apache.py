import shutil
import os,sys
import subprocess
import ConfigParser

def copy(src, dst):
    cmd = "cp -avr %s %s"%(src,dst)
    print cmd
    try:
        os.system(cmd)
    except Exception,e:
        print "Error while copying ...",e


configs = ConfigParser.ConfigParser()
configs.read('input.conf')

dir_to_copy = eval(configs.defaults().get('dir_to_copy'))
tomcat_path = configs.defaults().get('tomcat_path')
server_path = configs.defaults().get('server_path')

print configs.items('DEFAULT')

for section in configs.sections():
    instance_name = section
    count = int(configs.get(section, 'count'))
    port = int(configs.get(section, 'port'))

    for c in range(1, count+1):
        new_dir_name = instance_name + str(c)
        # dst = tomcat_path + os.sep + 'servers' + os.sep + new_dir_name
        dst = server_path + os.sep + new_dir_name
        if not os.path.exists(dst):
            os.mkdir(dst)
        else:
            print "Directory structure already exists.. cannot continue.."
            sys.exit()
        for item in dir_to_copy:
            src = tomcat_path + os.sep + item
            copy(src, dst)    