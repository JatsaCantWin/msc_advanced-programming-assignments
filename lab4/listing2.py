#!/ usr / bin / env python3
# Klient i serwer UDP na hoście lokalnym
import argparse , socket
from datetime import datetime

MAX_BYTES = 65535
def serwer (port):
    sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind (('127.0.0.1', port ))
    print ( 'Sluchanie w {} '.format ( sock.getsockname ()))
    while True:
        data, adress = sock.recvfrom (MAX_BYTES)
        text = data.decode( 'utf-8' )
        print ( 'The klient w {} mowi {!r} '.format ( adress , text ))
        text = 'Twoj dane bylo {} bajtow long'.format ( len ( data ))
        data = text.encode ( 'utf-8' )
        sock.sendto ( data , adress )
def client ( port ):
    sock = socket.socket ( socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The czas to {} '.format ( datetime.now ())
    data = text.encode ( 'utf-8' )
    sock.sendto ( data , ('127.0.0.1', port ))
    print ( ' Przypisany system operacyjny ja ten adres {} '.format (
    sock.getsockname ()))
    data, adress = sock.recvfrom (MAX_BYTES) # Niebezpieczeństwo !
    text = data.decode ( 'utf-8' )
    print ( 'The serwer {} odpowiedział {!r} '.format ( adress , text ))

if __name__ == '__main__':
    choices = { 'klient' : client , 'serwer' : serwer }
    parser = argparse.ArgumentParser ( description='Wyślij oraz odbieraj UDP lokalnie' )
    parser.add_argument ( 'role' , choices=choices , help='co rola zegrac' )
    parser.add_argument ( '-p' , metavar='PORT' , type=int , default=1060, help='UDP port ( domyslnie 1060)')
    args = parser.parse_args ()
    function = choices [ args.role ]
    function ( args.p )