#!/bin/sh
nohup python3 server.py > server.out  &
echo $! > pid.txt
