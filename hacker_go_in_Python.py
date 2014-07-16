def booting():
	print "\n\n********* Hacker GO *********\n\n"

	print "Greetings,"
	print "\tYou don't know who I am but I have been watching you for some time. Do not be alarmed, I am not connected with the authorities. I would like to hire you for something very important. I need to locate some information contained within the computer systems of an organization, and I believe you may know how to access it." 
	print "\tAccept my offer, and you will be generously rewarded."
	print "\nYour Future Employer"
	print "\n\tOne thing more... I would be very disappointed if you were to decline my offer; I strongly suggest you accept it."

	print "Press any key to accept the offer......"

	raw_input()

	print "Local System Startup"
	print "---------------------------->>100%"
	print "Bootup Complete"
	print "2014 all rights reserved"
	print "type 'help' for help"

def start():
	position = 0

	while True:
		if position == 0:
			cmd = raw_input("localhost$ ")
		elif position ==1:
			cmd = raw_input("hack$ ")
		elif position == 2:
			cmd = raw_input("gateway$ ")
		elif position == 3:
			cmd = raw_input("workspace$ ")
		else:
			print "Error!\aYou have entered an unknown place!"
			print "Press any key to reboot......"
			raw_input()
			position = 0

		if position == 1 and cmd == "atip":
			atip()
		elif cmd == "exit":
			exit0(position)
			position -= 1
			continue
		elif position == 1 and cmd =="gate":
			if gate(position):
				position = 2
		elif cmd == "help":
			show_help(position)
		elif position == 2 and cmd == "jump":
			if jackie_workspace(position):
				position = 3
		elif cmd == "ls":
			ls(position)
		elif position == 0 and cmd == "run":
			run(position)
			position = 1
		elif cmd == "type":
			show_type(position)
		else:
			print "%s: command not found" % cmd

def atip():
	print "You'll need a username and password to gain access to their systems, so I hope you'll be able to figure out Jackie's password."
	print "I don't think you'll mind me saying he's not very bright so figuring out his password should be a simple task for a senior hacker like you."

def exit0(position):
	if position == 1:
		print "Exited from the hack routine."
	elif position == 2:
		print "Disconnected from the gateway system."
	elif position == 3:
		print "Disconnected from Jackie's workspace."
	else:
		print "Shutting down......"
		exit(0)

def gate(position):
	print "Establishing a connection to the Gateway System..."
	print "Connection Established."
	print "Log in with your Gateway account"

	username = raw_input("username: ")
	if is_username_correct(username):
		password = raw_input("password: ")
		if is_password_correct(password):
			print "Successfully login!\nHello,Jackie!\nWelcome to the Gateway System\n"
			return True
		else:
			print "Invalid Password!\nDisconnected from the gateway system."
			return False
	else:
		print "Invalid Username!\nDisconnected from the gateway system."
		return False

def is_username_correct(username):
	return username == "Jackie" or username == "jackie"

def is_password_correct(password):
	return password == "password" or password == "789456123"

def show_help(position):
	if position == 0:
		print "localhost help menu:"
		print " exit         log out and shut down your localhost"
		print " run          run he employer's hack routine"
	elif position == 1:
		print "hack routine help menu:"
		print " atip         a tip on hacking"
		print " exit         exit this routine"
		print " gate         hack into the gateway"
	elif position == 2:
		print "Gateway help menu:"
		print " exit         exits this gateway"
		print " jump         jump to your workstation"
	elif position == 3:
		print "Workstation help menu:"
		print " exit         exits this workstation"
	print " help         display a list of system commands"
	print " ls           list files in this dir"
	print " type         type out all files' contents"

def jackie_workspace(position):
	print "Establishing a connection to Jackie's Workstation..."
	print "Connection Established.\nEnter your Workstation password."
	password = raw_input("password: ")
	if is_password_correct(password):
		print "Successfully login!\nLogged into Jackie's workstation"
		return True
	else:
		print "Invalid Password!\nDisconnected from the workspace."
		return False

def ls(position):
	print "File List:"
	if position == 0:
		print " readme       1k  -rw wwr r-x"
	elif position == 1:
		print " no file in this directory"
	elif position == 2:
		print " no file in this directory"
	elif position ==3:
		print " TopSecret    2k  -rw wwr r-x"
	else:
		print " Error!\aShutting down......"
		exit(0)

def run(position):
	print "running the hack routine...\nsuccessfully launched\n"
	print "type 'help' for help"

def show_type(position):
	if position == 0:
		print "I'm glad you decided to accept my offer. Trust me, I'll make it worth your while. By now the hack routine should be installed on your local system; just type 'run' to start it up."
	elif position == 1:
		print " no file to type out"
	elif position == 2:
		print " no file to type out"
	elif position == 3:
		print "********* Jackie's TopSecret *********"
		print "Jackie's Note:"
		print "Ok,this is very important!I have to remember this,and anyone else can know this!"
		print "Just now I found a very interesting website,http://jackiekuo.com"
		print "And I can just press any key to visit it now!!......"
		raw_input()
		raw_input()
		print "I was just kidding! ^-^\nCongratulations!\n"
		print "You amazing hacker!\nYou have just passed this demo!"
		print "Press any key to continue......"
		raw_input()


# let's begin!
booting()
start()
