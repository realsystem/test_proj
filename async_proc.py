def read_msg(sock):
    uname = sock.recv(NAME_SIZE)
    res = Result(uname)
    input_msg = sock.recv(INPUT_MSG_SIZE)
    while "BYE!" != input_msg:
        res.add_msg(input_msg)
        input_msg = sock.recv(INPUT_MSG_SIZE)
    return res
