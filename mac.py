#!/usr/bin/env python
import sys
import os
import random


def random_mac_address():
    # first octet/number must be even, apparently
    return ':'.join(['%0x' % (random.randint(0, 127) * 2)] + ['%0x' % random.randint(0, 255) for i in range(5)])

new_mac = random_mac_address()


def gen():
    print new_mac


def help():
    print '''
mac.py --gen
    will print a random MAC address
mac.py --display
    will print the current MAC address
sudo mac.py
    will reset the current en0 ether address
    (You must sudo / run this as root.)'''


def display(label):
    print label
    check = os.popen('ifconfig en0 | grep ether')
    print check.read()

if '--gen' in sys.argv or '--random' in sys.argv:
    gen()
elif '--help' in sys.argv:
    help()
elif '--display' in sys.argv:
    display('Current')
else:
    # if not root... kick out
    if not os.geteuid() == 0:
        print 'You must be root (0) to run this application (you are %d).' % os.geteuid()
        print 'Please use sudo and try again.'
        sys.exit()

    display('Before')
    # disassociate your wi-fi connection
    os.system('airport -z')
    # change your MAC address to something random
    os.system('ifconfig en0 ether %s' % new_mac)
    # make sure it took
    display('After')
