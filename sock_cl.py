import socket
'''client'''

SOCK_PORT = 8888
sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
print hostname
try:
    sock_client.connect((hostname, SOCK_PORT))
    print "connected to {}".format(hostname)
except socket.error as msg:
    sock_client = None
    print "not connected to {}: {}".format(hostname, msg)
if sock_client:
    try:
        (cmd, arg) = input("input: \"func\", arg\n")
        print "sending {}({})".format(cmd, arg)
        sock_client.sendall(cmd + str(arg))
        print "sent {} to {}".format(cmd, hostname)
    except socket.error as msg:
        print "can't send {} to {}: {}".format(cmd, hostname, msg)
if sock_client:
    sock_client.close()
