import socket
'''server'''

SOCK_PORT=8888
MAX_CONN = 1
MAX_TRY = 10
MAX_MSG_LEN = 32
CMD_REPLY = "OK"
hostname = socket.gethostname()
print hostname

def S(conn, val):
    print "called {} with arg {}".format(S.__name__, val)
    conn.sendall(CMD_REPLY)

sock_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock_srv.bind((hostname, SOCK_PORT))
    print "bind {} for {}".format(SOCK_PORT, hostname)
    try:
        sock_srv.listen(MAX_CONN)
        print "start listening {} connections on port {}".format(MAX_CONN, SOCK_PORT)
        tries = 0
        while tries < MAX_TRY:
            connection, (client_addr, client_port) = sock_srv.accept()
            print "connected {} on port {}".format(client_addr, client_port)
            while True:
                data = connection.recv(MAX_MSG_LEN)
                if not data:
                    print "no data"
                    break
                print "received {}".format(data)
                if data[0] == "S":
                    print "parsing message: func = {}, arg = {}".format(data[0], data[1])
                    S(connection, data[1])
            tries += 1
        else:
            print "finished on port {}".format(SOCK_PORT)
    except socket.error as msg:
        print "can't listening on port {}: {}". format(SOCK_PORT, msg)
except socket.error as msg:
    print "can't work port {} for {}: {}".format(SOCK_PORT, hostname, msg)
sock_srv.close()
