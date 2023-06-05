#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter08/queuepi.py
# Small application that uses several different message queues

import random
import threading
import time
import zmq

B = 32  # The number of bits used to represent each coordinate

def ones_and_zeros(digits):
    """Express `n` in at least `d` binary digits, with no special prefix."""
    return bin(random.getrandbits(digits)).lstrip('0b').zfill(digits)

def bitsource(zcontext, url):
    """Produce random points in the unit square."""
    zsock = zcontext.socket(zmq.PUB)  # Create a publisher socket
    zsock.bind(url)  # Bind the socket to the specified URL
    while True:
        zsock.send_string(ones_and_zeros(B * 2))  # Generate random points and send them as strings
        time.sleep(0.01)

def always_yes(zcontext, in_url, out_url):
    """Coordinates in the lower-left quadrant are inside the unit circle."""
    isock = zcontext.socket(zmq.SUB)  # Create a subscriber socket
    isock.connect(in_url)  # Connect the socket to the specified URL
    isock.setsockopt(zmq.SUBSCRIBE, b'00')  # Subscribe to messages with prefix '00'
    osock = zcontext.socket(zmq.PUSH)  # Create a push socket
    osock.connect(out_url)  # Connect the socket to the specified URL
    while True:
        isock.recv_string()  # Receive a message as a string
        osock.send_string('Y')  # Send a response 'Y'

def judge(zcontext, in_url, pythagoras_url, out_url):
    """Determine whether each input coordinate is inside the unit circle."""
    isock = zcontext.socket(zmq.SUB)  # Create a subscriber socket
    isock.connect(in_url)  # Connect the socket to the specified URL
    for prefix in b'01', b'10', b'11':
        isock.setsockopt(zmq.SUBSCRIBE, prefix)  # Subscribe to messages with prefixes '01', '10', and '11'
    psock = zcontext.socket(zmq.REQ)  # Create a request socket
    psock.connect(pythagoras_url)  # Connect the socket to the specified URL
    osock = zcontext.socket(zmq.PUSH)  # Create a push socket
    osock.connect(out_url)  # Connect the socket to the specified URL
    unit = 2 ** (B * 2)  # The upper bound for the sum of squares
    while True:
        bits = isock.recv_string()  # Receive a message as a string
        n, m = int(bits[::2], 2), int(bits[1::2], 2)  # Extract two numbers from the message
        psock.send_json((n, m))  # Send the numbers to the pythagoras function for computation
        sumsquares = psock.recv_json()  # Receive the sum of squares from the pythagoras function
        osock.send_string('Y' if sumsquares < unit else 'N')  # Send a response 'Y' or 'N' based on the condition

def pythagoras(zcontext, url):
    """Return the sum-of-squares of number sequences."""
    zsock = zcontext.socket(zmq.REP)  # Create a reply socket
    zsock.bind(url)  # Bind the socket to the specified URL
    while True:
        numbers = zsock.recv_json()  # Receive a list of numbers as JSON
        zsock.send_json(sum(n * n for n in numbers))  # Compute and send the sum of squares as JSON

def tally(zcontext, url):
    """Tally how many points fall within the unit circle, and print pi."""
    zsock = zcontext.socket(zmq.PULL)  # Create a pull socket
    zsock.bind(url)  # Bind the socket to the specified URL
    p = q = 0  # Variables to keep track of points
    while True:
        decision = zsock.recv_string()  # Receive a decision as a string ('Y' or 'N')
        q += 1  # Increment the total number of points
        if decision == 'Y':
            p += 4  # Increment the number of points inside the unit circle by 4
        print(decision, p / q)  # Print the decision and the approximate value of pi

def start_thread(function, *args):
    thread = threading.Thread(target=function, args=args)  # Create a new thread for the specified function with arguments
    thread.daemon = True  # Set the thread as daemon to allow Ctrl-C to terminate the program
    thread.start()  # Start the thread

def main(zcontext):
    pubsub = 'tcp://127.0.0.1:6700'  # URL for the publisher-subscriber pattern
    reqrep = 'tcp://127.0.0.1:6701'  # URL for the request-reply pattern
    pushpull = 'tcp://127.0.0.1:6702'  # URL for the push-pull pattern
    start_thread(bitsource, zcontext, pubsub)  # Start the bitsource thread
    start_thread(always_yes, zcontext, pubsub, pushpull)  # Start the always_yes thread
    start_thread(judge, zcontext, pubsub, reqrep, pushpull)  # Start the judge thread
    start_thread(pythagoras, zcontext, reqrep)  # Start the pythagoras thread
    start_thread(tally, zcontext, pushpull)  # Start the tally thread
    time.sleep(30)  # Wait for 30 seconds

if __name__ == '__main__':
    main(zmq.Context())  # Start the main function with a ZeroMQ context