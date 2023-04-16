#!/usr/bin/env python3
# Client that sends data then closes the socket, not expecting a reply.

import socket
from argparse import ArgumentParser

def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    print('Run this script in another window with "-c" to connect')
    print('Listening at', sock.getsockname())
    sc, sockname = sock.accept()
    print('Accepted connection from', sockname)
    sc.shutdown(socket.SHUT_WR)
    message = b''
    while True:
        more = sc.recv(8192)  # arbitrary value of 8k
        if not more:  # socket has closed when recv() returns ''
            print('Received zero bytes - end of file')
            break
        print('Received {} bytes'.format(len(more)))
        message += more
    print('Message:\n')
    print(message.decode('utf-8'))
    sc.close()
    sock.close()

def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    sock.sendall(b'I like my toast done on one side\n')
    sock.sendall(b'And you can hear it in my accent when I talk\n')
    sock.sendall(b'I\'m an Englishman in New York\n')
    sock.close()

if __name__ == '__main__':
    parser = ArgumentParser(description='Transmit & receive a data stream')
    parser.add_argument('hostname', nargs='?', default='127.0.0.1',
                        help='IP address or hostname (default: %(default)s)')
    parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060,
                        help='TCP port number (default: %(default)s)')
    args = parser.parse_args()
    function = client if args.c else server
    function((args.hostname, args.p))