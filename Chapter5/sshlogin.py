import pexpect
mypassword='123456'
child = pexpect.spawn('scp hello.txt root@192.168.24.83:.')
#child = pexpect.spawn('scp hello.txt root@192.168.125.126:.')
child.expect('Password:')

child.sendline(mypassword)
