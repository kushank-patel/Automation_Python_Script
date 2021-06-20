import os
import getpass
import playsound
import getpass
import boto3
po  = boto3.client('polly')
print("\n\n")
def voice_output(msg):
    res = po.synthesize_speech(Text= msg , OutputFormat='mp3' , VoiceId='Joanna' )
    os.remove('myaudio.mp3')
    file = open('myaudio.mp3' , 'wb')
    file.write(res['AudioStream'].read() )
    file.close()
    playsound.playsound('myaudio.mp3', True)

def hdfs_file(node,location):
    if location == "remote":
        if node == "namenode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            name_dir = input("Enter the namenode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%name_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("scp  /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml"%remoteip)

        elif node == "datanode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            data_dir = input("Enter the datanode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%data_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("scp  /etc/hadoop/hdfs-site.xml 'root@%s':/etc/hadoop/hdfs-site.xml"%remoteip)

    elif location == "local":
        if node == "namenode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.name.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            name_dir = input("Enter the namenode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%name_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")

        elif node == "datanode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/hdfs-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo ' ' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
            data_dir = input("Enter the datanode folder name:")
            os.system("echo '<value>%s</value>' >> /etc/hadoop/hdfs-site.xml"%data_dir)
            os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")

#core file

def core_file(node,location):
    if location == "remote":
        if node == "namenode":
                    
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<value>hdfs://0.0.0.0:9001</value>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            os.system("scp  /etc/hadoop/core-site.xml 'root@%s':/etc/hadoop/core-site.xml"%remoteip)

        elif node == "datanode":
                    
            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            name_node_ip = input("Enter namenode ip:")
            os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml"%name_node_ip)
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
            os.system("scp  /etc/hadoop/core-site.xml 'root@%s':/etc/hadoop/core-site.xml"%remoteip)


    elif location == "local":
        if node == "namenode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            name_node_ip = input("Enter namenode ip:")
            os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml"%name_node_ip)
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")

        elif node == "datanode":

            os.system("echo '<?xml version=\"1.0\"?>' > /etc/hadoop/core-site.xml")
            os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")

            os.system("echo '<!-- Put site-specific property overrides in this file. -->' >> /etc/hadoop/core-site.xml")
            os.system("echo ' ' >> /etc/hadoop/core-site.xml")
            os.system("echo '<configuration>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
            name_node_ip = input("Enter namenode ip:")
            os.system("echo '<value>hdfs://%s:9001</value>' >> /etc/hadoop/core-site.xml"%name_node_ip)
            os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
            os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")

def menu():

    os.system("tput setaf 1")

    print("\t\t\t\t\t\tTECH-ASSISTANT MENU")


    os.system("tput setaf 7")
    print("\t\t\t\t\t=========----------------=========")

    os.system("tput setaf 2")
    print("""
            \t\t\t\tPress  1: To Run date command.
            \t\t\t\tPress  2: To Run cal command.
            \t\t\t\tPress  3: To Find ip of your computer.
            \t\t\t\tPress  4: To check connectivity of your internet.
            \t\t\t\tPress  5: To setup web-server for first time with httpd.
            \t\t\t\tPress  6: To setup webserver httpd.
            \t\t\t\tPress  7: TO create partition.
            \t\t\t\tPress  8: To format partition.
            \t\t\t\tPress  9: To mount partition.
            \t\t\t\tPress 10: To increase/decrese storage size.
            \t\t\t\tPress 11: To create hdfs cluster(change in hdfs file)
            \t\t\t\tPress 12: To format  namenode
            \t\t\t\tPress 13: To create hdfs cluster(change in core file).
            \t\t\t\tPress 14: To start (namenode/datanode).
            \t\t\t\tPress 15: To stop (namenode/datanode).
            \t\t\t\tPress 16: To store file in datanode.
            \t\t\t\tPress 17: To retrieve file stored in datanode.
            \t\t\t\tPress 18: To get report of cluster
            \t\t\t\tPress 19: To get docker menu list.
	    \t\t\t\tPress 20: To get aws menu list
            \t\t\t\tPress 21: To Exit.
            
            """)
    os.system("tput setaf 7")
    

#To use aws locally    
def aws():
    while True:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t           AWS-MENU")

        os.system("tput setaf 7")
        print("\t\t\t\t\t===========-----------------------===========")

        os.system("tput setaf 2")
        print("""
                \t\t\t\tPress  1:To create key-pairs.
                \t\t\t\tPress  2:To describe key-pairs 
	        \t\t\t\tPress  3:To create volumes. 
                \t\t\t\tPress  4:To create security groups.  
                \t\t\t\tPress  5:To launch ec2 instances
                \t\t\t\tPress  6:To describe ec2 instances.
                \t\t\t\tPress  7:To create s3 bucket.
                \t\t\t\tPress  8:To Exit.
                """)
        os.system("tput setaf 7")
	
        ch = input("Enter your choice:")
        if int(ch) == 1:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press one creating key pair initiated')
            a = "taskkey"
            os.system("aws ec2 create-key-pair --key-name {}".format(a))
            os.system("tput setaf 7") 
	 
        elif int(ch) == 2:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press two here is your key pairs')
            os.system("aws ec2 describe-key-pairs")
            os.system("tput setaf 7") 

        elif int(ch) == 3:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press three creating volume initiated')
            os.system("aws ec2 create-volume --availability-zone  us-east-1a --no-encrypted  --size 1")
            os.system("tput setaf 7") 
	
        elif int(ch) == 4:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press four creating security group initiated')
            os.system("aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-0df0ed77".format( "Tasksg","Allows"))
            os.system("tput setaf 7") 

	
        elif int(ch) == 5:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press five isnatnce creation process initiated')
            os.system("aws ec2 run-instances --image-id ami-098f16afa9edf40be --instance-type t2.micro --count 1 --subnet-id subnet-48d71869 --security-group-ids sg-97c523b5  --key-name taskkey ")
            os.system("tput setaf 7") 

        elif int(ch) == 6:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press six here is your instances')
            os.system("aws ec2 describe-instances")
            os.system("tput setaf 7") 

        elif int(ch) == 7:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press seven bucket creation initiated')
            os.system("aws s3 mb s3://aws-taskbucket-1234")
            os.system("tput setaf 7") 

        elif int(ch) == 8:
            voice_output('Thank you for using our AWS services bye bye')
            break

        else:

            os.system("tput setaf 1")
            print("""
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    """)
        voice_output('Press Enter to continue')            
        input("Press Enter to continue..........")
        os.system("clear")  
        os.system("tput setaf 7")

#To use aws remotely

def remoteaws():
    while True:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t           AWS-MENU")

        os.system("tput setaf 7")
        print("\t\t\t\t\t===========-----------------------===========")

        os.system("tput setaf 2")
        print("""
                \t\t\t\tPress  1:To create key-pairs.
                \t\t\t\tPress  2:To describe key-pairs 
                \t\t\t\tPress  3:To create volumes. 
                \t\t\t\tPress  4:To create security groups.  
                \t\t\t\tPress  5:To launch ec2 instances
                \t\t\t\tPress  6:To describe ec2 instances.
                \t\t\t\tPress  7:To create s3 bucket.
                \t\t\t\tPress  8:To Exit.
                """)
        os.system("tput setaf 7")
	
        ch = input("Enter your choice:")
        if int(ch) == 1:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press one creating key pair initiated')
            a = "taskkey"
            os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(remoteip,a))
            os.system("tput setaf 7") 
	 
        elif int(ch) == 2:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press two here is your key pairs')
            os.system("ssh {} aws ec2 describe-key-pairs".format(remoteip))
            os.system("tput setaf 7") 

        elif int(ch) == 3:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press three creating volume initiated')
            os.system("ssh {} aws ec2 create-volume --availability-zone  us-east-1a --no-encrypted  --size 1".format(remoteip))
            os.system("tput setaf 7") 
	
        elif int(ch) == 4:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press four creating security group initiated')
            os.system("ssh {0} aws ec2 create-security-group --group-name {1} --description {2} --vpc-id vpc-0df0ed77".format(remoteip, "Tasksg","Allows"))
            os.system("tput setaf 7") 

	
        elif int(ch) == 5:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press five isnatnce creation process initiated')
            os.system("ssh {} aws ec2 run-instances --image-id ami-098f16afa9edf40be --instance-type t2.micro --count 1 --subnet-id subnet-48d71869 --security-group-ids sg-97c523b5  --key-name taskkey ".format(remoteip))
            os.system("tput setaf 7") 

        elif int(ch) == 6:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press six here is your instances')
            os.system("ssh {} aws ec2 describe-instances".format(remoteip))
            os.system("tput setaf 7") 

        elif int(ch) == 7:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You press seven bucket creation initiated')
            os.system("ssh {} aws s3 mb s3://aws-taskbucket-1234".format(remoteip))
            os.system("tput setaf 7") 

        elif int(ch) == 8:
            voice_output('Thank you for using our AWS services bye bye')
            break

        else:

            os.system("tput setaf 1")
            print("""
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    """)
        voice_output('Press Enter to continue')            
        input("Press Enter to continue..........")
        os.system("clear")  
        os.system("tput setaf 7")

#To use docker locally
def docker():
    while True:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t         DOCKER-MENU")

        os.system("tput setaf 7")
        print("\t\t\t\t\t===========-----------------------===========")

        os.system("tput setaf 2")
        print("""
                \t\t\tPress  1:To install docker in your RHEL8 os.
                \t\t\tPress  2:To start docker services. 
                \t\t\tPress  3:To check docker info.  
                \t\t\tPress  4:To pull os images from docker hub.
                \t\t\tPress  5:To check how many docker images you have.
                \t\t\tPress  6:To run your docker os(container).(to install newos on the top of docker) 
                \t\t\tPress  7:To start os(container).
                \t\t\tPress  8:To stop os(container).
                \t\t\tPress  9:To get terminal of os(container)which is just started with option no 20.
                \t\t\tPress 10:To show container state.
                \t\t\tPress 11:To remove any os(container) from docker.
                \t\t\tPress 12:To remove any os  images of docker.
                \t\t\tPress 13:To Exit.
                """)
        os.system("tput setaf 7")
    
        ch = input("Enter your choice:")
        if int(ch) == 1:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press one docker downloading initiated')
            os.system("sudo yum install docker-ce --nobest -y")
            os.system("tput setaf 7")

        elif int(ch) == 2:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press Two starting docker service')
            os.system("systemctl start docker")
            print("Docker services started successfully")
            os.system("tput setaf 7")
        
        elif int(ch) == 3:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press Three here is your docker info')
            os.system("sudo docker info")
            os.system("tput setaf 7")
    
        elif int(ch) == 4:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press four your image pulling initiated')
            voice_output('Write down your image name')
            os_name=input("image name:")
            voice_output('Write dwon your image version')
            os_version=input("image version:")
            os.system("sudo docker pull {0}:{1} ".format(os_name,os_version))
            os.system("tput setaf 7")
    
        elif int(ch) == 5:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press five here is your docker images')
            os.system("sudo docker images")
            os.system("tput setaf 7")

        elif int(ch) == 6:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press six your container creating process initiated')
            voice_output('Write down your container name')
            os_name=input("Write your os name:")
            voice_output('Write down your image name')
            img_name=input("Write your image name:")
            voice_output('Write dwon your image version')
            img_version=input("Write your image version:")
            os.system("sudo docker run -it --name {}  {}:{}".format(os_name,img_name,img_version))
            os.system("tput setaf 7")     
        
        elif int(ch) == 7:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press seven your container starting process initiated')
            voice_output('Write down your container name that you want to start')
            os_name=input("Write your osname that you want to start:")
            os.system("sudo docker start {}".format(os_name))
            os.system("tput setaf 7") 

        elif int(ch) == 8:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press eight your container starting process initiated')
            voice_output('Write down your container name that you want to stop')
            os_name=input("Write your osname that you want to stop:")
            os.system("sudo docker stop {}".format(os_name))

            os.system("tput setaf 7")

        elif int(ch) == 9:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press nine your container terminal attaching process initiated')
            voice_output('Write down your container name that you want to attach')
            os_name=input("write os name to get terminal of that os: ")
            os.system("sudo docker attach {}".format(os_name))
            os.system("tput setaf 7")

        elif int(ch) == 10:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press ten here is your container state')
            os.system("sudo docker ps -a")
            os.system("tput setaf 7")

        elif int(ch) == 11:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press eleven your container removing process initiated')
            voice_output('Write down your container name that you want to remove')
            os_name=input("Container name that you want to remove:")
            os.system("sudo docker rm {}".format(os_name))
            os.system("tput setaf 7")

        elif int(ch) == 12:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press twelve your image removing process initiated')
            voice_output('Write down your image name that you want to remove')
            image_name=input("Image name that you want to remove:")
            voice_output('Write down your image version that you want to remove')
            image_version=input("Image version that you want to remove:")
            os.system("sudo docker rmi -f {}:{}".format(image_name,image_version))
            os.system("tput setaf 7")

        elif int(ch) == 13:
            voice_output('Thank you for using our docker services bye bye')
            break

        else:

            os.system("tput setaf 1")
            print("""
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    """)
        voice_output('Press Enter to continue')
        input("Press Enter to continue..........")
        os.system("clear")
        os.system("tput setaf 7")

#To use docker remotely
def remotedocker():
    while True:
        os.system("tput setaf 1")
        print("\t\t\t\t\t\t         DOCKER-MENU")

        os.system("tput setaf 7")
        print("\t\t\t\t\t===========-----------------------===========")

        os.system("tput setaf 2")
        print("""
                \t\t\tPress  1:To install docker in your RHEL8 os.
                \t\t\tPress  2:To start docker services.
                \t\t\tPress  3:To check docker info.  
                \t\t\tPress  4:To pull os images from docker hub.
                \t\t\tPress  5:To check how many docker images you have.
                \t\t\tPress  6:To run your docker os(container).(to install newos on the top of docker) 
                \t\t\tPress  7:To start os(container).
                \t\t\tPress  8:To stop os(container).
                \t\t\tPress  9:To get terminal of os(container)which is just started with option no 20.
                \t\t\tPress 10:To show container state.
                \t\t\tPress 11:To remove any os(container) from docker.
                \t\t\tPress 12:To remove any os  images of docker.
                \t\t\tPress 13:To Exit.
                """)
        os.system("tput setaf 7")
    
        ch = input("Enter your choice:")
        if int(ch) == 1:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press one docker downloading initiated')
            os.system("ssh {} sudo yum install docker-ce --nobest".format(remoteip))
            os.system("tput setaf 7")

        elif int(ch) == 2:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press Two starting docker service')
            os.system("ssh {} sudo systemctl start docker".format(remoteip))
            print("Docker services started successfully")
            os.system("tput setaf 7")
        
        elif int(ch) == 3:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press Three here is your docker info')
            os.system("ssh {} sudo docker info".format(remoteip))
            os.system("tput setaf 7")
    
        elif int(ch) == 4:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press four your image pulling initiated')
            voice_output('Write down your image name')
            os_name=input("image name:")
            voice_output('Write dwon your image version')
            os_version=input("image version:")
            os.system("ssh {0} sudo docker pull {1}:{2} ".format(remoteip,os_name,os_version))
            os.system("tput setaf 7")
    
        elif int(ch) == 5:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press five here is your docker images')
            os.system("ssh {} sudo docker images".format(remoteip))
            os.system("tput setaf 7")

        elif int(ch) == 6:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press six your container creating process initiated')
            voice_output('Write down your container name')
            os_name=input("Write your os name:")
            voice_output('Write down your image name')
            img_name=input("Write your image name:")
            voice_output('Write dwon your image version')
            img_version=input("Write your image version:")
            os.system("ssh {0} sudo docker run -it --name {1}  {2}:{3}".format(remoteip,os_name,img_name,img_version))
            os.system("tput setaf 7")     
        
        elif int(ch) == 7:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press seven your container starting process initiated')
            voice_output('Write down your container name that you want to start')
            os_name=input("Write your osname that you want to start:")
            os.system("ssh {0} sudo docker start {1}".format(remoteip,os_name))
            os.system("tput setaf 7") 

        elif int(ch) == 8:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press eight your container starting process initiated')
            voice_output('Write down your container name that you want to stop')
            os_name=input("Write your osname that you want to stop:")
            os.system("ssh {0} sudo docker stop {1}".format(remoteip,os_name))
            os.system("tput setaf 7")

        elif int(ch) == 9:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press nine your container terminal attaching process initiated')
            voice_output('Write down your container name that you want to attach')
            os_name=input("write os name to get terminal of that os: ")
            os.system("ssh {0} sudo docker attach {1}".format(remoteip,os_name))
            os.system("tput setaf 7")

        elif int(ch) == 10:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press ten here is your container state')
            os.system("ssh {} sudo docker ps -a".format(remoteip))
            os.system("tput setaf 7")

        elif int(ch) == 11:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press eleven your container removing process initiated')
            voice_output('Write down your container name that you want to remove')
            os_name=input("Container name that you want to remove:")
            os.system("ssh {0} sudo docker rm {1}".format(remoteip,os_name))
            os.system("tput setaf 7")

        elif int(ch) == 12:
            os.system("tput setaf 2")
            print("you press {} here is your requested  command".format(ch))
            print("\n")
            voice_output('You Press twelve your image removing process initiated')
            voice_output('Write down your image name that you want to remove')
            image_name=input("Image name that you want to remove:")
            voice_output('Write down your image version that you want to remove')
            image_version=input("Image version that you want to remove:")
            os.system("ssh {0} sudo docker rmi -f {1}:{2}".format(remoteip,image_name,image_version))
            os.system("tput setaf 7")

        elif int(ch) == 13:
            voice_output('Thank you for using our docker services bye bye')
            break

        else:

            os.system("tput setaf 1")
            print("""
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    \t.....Wrong input.....
                    """)
        voice_output('Press Enter to continue')
        input("Press Enter to continue..........")
        os.system("clear")
        os.system("tput setaf 7")
    

def conditions():
    if int(ch) == 1:
        os.system("tput setaf 2")
        print("you press {} here is your requested date command".format(ch))
        print("\n")
        voice_output('You Press one here is your date command output')
        os.system("date")
        os.system("tput setaf 7")

    elif int(ch) == 2:
        os.system("tput setaf 2")
        print("you press {} here is your requested cal command".format(ch))
        print("\n")
        voice_output('You Press two here is your cal command output')
        os.system("cal")
        os.system("tput setaf 7")

    elif int(ch) == 3:
        os.system("tput setaf 2")
        print("you press {} here is your requested ip command".format(ch))
        print("\n")
        voice_output('You press three Here is your ip address')
        os.system("ifconfig enp0s3")
        os.system("tput setaf 7")
	
    elif int(ch) == 4:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press four Checking your connectivity')
        os.system("ping -c 4 www.google.com")
        os.system("tput setaf 7")

    elif int(ch) == 5:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n") 
        voice_output('You Press five Starting your web server')
        os.system("yum install httpd -y")
        os.system("systemctl start httpd")
        os.system("systemctl status httpd")
        os.system("tput setaf 7")
	
    elif int(ch) == 6:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press six Starting your web server')
        os.system("systemctl start httpd")
        os.system("systemctl status httpd")
        os.system("tput setaf 7")

    elif int(ch) == 7:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press seven creting your partition initiated')
        os.system("pvcreate /dev/sdb")
        os.system("pvcreate /dev/sdc")
        os.system("vgcreate arthvg1 /dev/sdb  /dev/sdc")
        os.system("lvcreate --size 12G --name arthlv1 arthvg1")
        os.system("lvdisplay arthvg1/arthlv1")
        os.system("tput setaf 7")
		
    elif int(ch) == 8:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press eight your partition is now formated')
        os.system("mkfs.ext4 /dev/arthvg1/arthlv1")
        os.system("tput setaf 7")
	
    elif int(ch) == 9:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press nine Your logical volume is now mounting')
        os.system("mount /dev/arthvg1/arthlv1  /master")
        os.system("df -h")
        os.system("tput setaf 7")

    elif int(ch) == 10:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press ten Here is your required service')
        voice_output('How much storage you want to add or remove please write down')
        size = input("How much storage you want to <add/remove> in gb:")
        voice_output('What do you want to do extend or reduce logical volume size please write down')
        di = input("what do you want to do<extend/reduce>:")  
        os.system("lv{0} --size {1}G /dev/arthvg1/arthlv1".format(di,size)) 
        os.system("resize2fs /dev/arthvg1/arthlv1")
        os.system("tput setaf 7")

    elif int(ch) == 11:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press eleven Here is your required service')
        voice_output('what do you want to configer namenode or datanode write it down')
        node = input("what do you want to configer<namenode/datanode>:")
        hdfs_file(node,location)
        os.system("tput setaf 7")
       
    elif int(ch) == 12:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press twele here is your required service')
        os.system("hadoop namenode -format")
        os.system("tput setaf 7")
	    
    elif int(ch) == 13:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press thirteen here is your required service')
        voice_output('what do you want to configer namenode or datanode write it down')
        node = input("what do you want to configer<namenode/datanode>:")
        core_file(node,location)
        os.system("tput setaf 7")

    elif int(ch) == 14:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press fourteen here is your required service')
        voice_output('what do you want to start namenode or datanode write it down')
        nodestart = input("what do you want to start(namenode/datanode):")   
        os.system("hadoop-daemon.sh start {}".format(nodestart))
        os.system("jps")
        os.system("tput setaf 7")

    elif int(ch) == 15:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press fifteen here is your required service')
        voice_output('what do you want to stop namenode or datanode write it down')
        nodestop = input("what do you want to stop(namenode/datanode):")
        os.system("hadoop-daemon.sh stop {}".format(nodestop))
        os.system("jps")
        os.system("tput setaf 7")

    elif int(ch) == 16:
        os.system("tput setaf 2")
        print("you press {} here is your requested command".format(ch))
        print("\n")
        voice_output('You Press sixteen here is your required service')
        voice_output('Please Enter your file name')
        file_name = input("Your file name:")
        os.system("hadoop dfsadmin -safemode leave")
        os.system("hadoop fs -put {} /".format(file_name))
        os.system("tput setaf 7")

    elif int(ch) == 17:
        os.system("tput setaf 2")
        print("you press {} here is your requested file".format(ch))
        print("\n")
        voice_output('You Press seventeen here is your required service')
        os.system("hadoop fs -ls  /")
        voice_output('Please Enter your file name')
        file_name = input("Your file name:")
        os.system("hadoop fs -cat /{}".format(file_name))
        os.system("tput setaf 7")

    elif int(ch) == 18:
        os.system("tput setaf 2")
        print("you press {} here is your requested file".format(ch))
        print("\n")
        voice_output('You Press eighteen here is your required service')
        os.system("hadoop dfsadmin -report | less")
        os.system("tput setaf 7")
        

    elif int(ch) == 19:
        os.system("clear")  
        voice_output('You Press nineteen here is your required docker service')
        voice_output('Welcome to your Docker Menu')
        docker()

    elif int(ch) == 20:
        os.system("clear")
        voice_output('You Press twenty here is your required aws service')
        voice_output('Welcome to your AWS Menu')
        aws()

    elif int(ch) == 21:
        voice_output('Thank you for using our services')
        voice_output('Bye Bye')     
        exit()
        


    else:

        os.system("tput setaf 1")		
        print("""
                \t.....Wrong input.....
                \t.....Wrong input.....
                \t.....Wrong input.....
                """)
    voice_output('Press Enter to continue')    
    input("Press Enter to continue..........")
    os.system("clear")	

def menu2():
    os.system("clear")
    os.system("tput setaf 1")
    print("\t\t\t\t\tWELCOME TO YOUR TECH -- ASSISTANT")

    os.system("tput setaf 7")
    print("\t\t\t\t\t=========----------------=========")

    print("\n")

menu2()
voice_output('Please Enter your credentials')
passwd = getpass.getpass("Enter your password: ")
os.system("clear")
if passwd != "redhat":
    exit()

menu2()
voice_output('Please Enter Where you want to run your code')
location = input("select your location where you want to run your code(remote/local):")
print("\n")
if location == "remote":
    remoteip = input("Enter your remote IP:")

os.system("clear")
menu()
voice_output('Welcome to Your Tech assistant Menu Program')
voice_output('Please write down service number from menu to run service')

while True:        
        
        os.system("clear")        
        menu()
        if location == "local":
            print("\n")	
            ch = input("Enter your choice:")
            conditions()        
            

#remote login

        elif location == "remote":
            
            print("\n")
            ch = input("Enter your choice:")
            if int(ch) == 1:
                os.system("tput setaf 2")
                print("you press {} here is your requested date command".format(ch))
                print("\n")
                voice_output('You Press one here is your date command output')
                os.system("ssh {} date".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 2:
                os.system("tput setaf 2")
                print("you press {} here is your requested cal command".format(ch))
                print("\n")
                voice_output('You Press two here is your cal command output')
                os.system("ssh {} cal".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 3:
                os.system("tput setaf 2")
                print("you press {} here is your requested ip command".format(ch))
                print("\n")
                voice_output('You press three Here is your ip address')
                os.system("ssh {} ifconfig enp0s3".format(remoteip))
                os.system("tput setaf 7")
	
            elif int(ch) == 4:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press four Checking your connectivity')
                os.system("ssh {} ping -c 4 www.google.com".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 5:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n") 
                voice_output('You Press five Starting your web server')
                os.system("ssh {} yum install httpd -y".format(remoteip))
                os.system("ssh {} systemctl start httpd".format(remoteip))
                os.system("ssh {} systemctl status httpd".format(remoteip))
                os.system("tput setaf 7")
	
            elif int(ch) == 6:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press six Starting your web server')
                os.system("ssh {} systemctl start httpd".format(remoteip))
                os.system("ssh {} systemctl status httpd".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 7:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press seven creting your partition initiated')
                os.system("ssh {} pvcreate /dev/sdb".format(remoteip))
                os.system("ssh {} pvcreate /dev/sdc".format(remoteip))
                os.system("ssh {} vgcreate arthvg1 /dev/sdb  /dev/sdc".format(remoteip))
                os.system("ssh {} lvcreate --size 12G --name arthlv1 arthvg1".format(remoteip))
                os.system("ssh {} lvdisplay arthvg1/arthlv1".format(remoteip))
                os.system("tput setaf 7")
                
            elif int(ch) == 8:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press eight your partition is now formated')
                os.system("ssh {} mkfs.ext4 /dev/arthvg1/arthlv1".format(remoteip))
                os.system("tput setaf 7")		
	
            elif int(ch) == 9:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press nine Your logical volume is now mounting')
                os.system("ssh {} mount /dev/arthvg1/arthlv1  /master".format(remoteip))
                os.system("ssh {} df -h".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 10:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press ten Here is your required service')
                voice_output('How much storage you want to add or remove please write down')
                size = input("How much storage you want to <add/remove> in gb:")
                voice_output('What do you want to do extend or reduce logical volume size please write down')
                di = input("what do you want to do<extend/reduce>:")
                os.system("ssh {0} lv{1} --size {2}G /dev/arthvg1/arthlv1".format(remoteip,di,size)) 
                os.system("ssh {} resize2fs /dev/arthvg1/arthlv1".format(remoteip))
                os.system("tput setaf 7")  
	   
            elif int(ch) == 11:
                os.system("tput setaf 2")   
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press eleven Here is your required service')
                voice_output('what do you want to configer namenode or datanode write it down')
                node = input("what do you want to configer<namenode/datanode>:")
                hdfs_file(node,location)
                os.system("tput setaf 7")
       
            elif int(ch) == 12:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press twele here is your required service')
                os.system("ssh {} hadoop namenode -format".format(remoteip))
                os.system("tput setaf 7")
	    
            elif int(ch) == 13:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press thirteen here is your required service')
                voice_output('what do you want to configer namenode or datanode write it down')
                node = input("what do you want to configer<namenode/datanode>:")
                core_file(node,location)
                os.system("tput setaf 7")

            elif int(ch) == 14:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press fourteen here is your required service')
                voice_output('what do you want to start namenode or datanode write it down')
                nodestart = input("what do you want to start(namenode/datanode):")
                os.system("ssh {0} hadoop-daemon.sh start {1}".format(remoteip,nodestart))
                os.system("ssh {} jps".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 15:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press fifteen here is your required service')
                voice_output('what do you want to stop namenode or datanode write it down')
                nodestop = input("what do you want to stop(namenode/datanode):")
                os.system("ssh {0} hadoop-daemon.sh stop {1}".format(remoteip,nodestop))
                os.system("ssh {} jps".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 16:
                os.system("tput setaf 2")
                print("you press {} here is your requested command".format(ch))
                print("\n")
                voice_output('You Press sixteen here is your required service')
                voice_output('Please Enter your file name')
                file_name = input("Your file name:")
                os.system("ssh {0} hadoop fs -put {1} /".format(remoteip,file_name))
                os.system("tput setaf 7")

            elif int(ch) == 17:
                os.system("tput setaf 2")
                print("you press {} here is your requested file".format(ch))
                print("\n")
                voice_output('You Press seventeen here is your required service')
                os.system("hadoop fs -ls  /")
                voice_output('Please Enter your file name')
                file_name = input("Your file name:")
                os.system("ssh {0} hadoop fs -cat /{1}".format(remoteip,file_name))
                os.system("tput setaf 7")
            
            elif int(ch) == 18:
                os.system("tput setaf 2")
                print("you press {} here is your requested file".format(ch))
                print("\n")
                voice_output('You Press eighteen here is your required service')
                os.system("ssh {} hadoop dfsadmin -report | less".format(remoteip))
                os.system("tput setaf 7")

            elif int(ch) == 19:
                os.system("clear")  
                voice_output('You Press nineteen here is your required docker service')
                voice_output('Welcome to your Docker Menu')
                remotedocker()

            elif int(ch) == 20:
                os.system("clear")
                voice_output('You Press twenty here is your required aws service')
                voice_output('Welcome to your AWS Menu')
                remoteaws()

            elif int(ch) == 21:
                voice_output('Thank you for using our services')
                voice_output('Bye Bye')     
                exit()     
                           
            else:

                os.system("tput setaf 1")		
                print("""
                        \t.....Wrong input.....
                        \t.....Wrong input.....
                        \t.....Wrong input.....
                        """)
            input("Press Enter to continue..........")
            os.system("clear")	        

