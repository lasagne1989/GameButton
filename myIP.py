#!/usr/bin/env python

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
