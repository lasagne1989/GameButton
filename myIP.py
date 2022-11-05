#!/usr/bin/env python

import socket

hostname = socket.gethostname()
hnlocal = f"{hostname}.local"
IPAddr = socket.gethostbyname(hnlocal)
print(IPAddr)
