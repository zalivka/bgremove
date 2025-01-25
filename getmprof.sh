#!/bin/bash

# Create local directory if it doesn't exist
mkdir -p mprof

# Copy all files from remote mprof directory to local
scp -i keys/merez root@merez:/root/bgremove/mprof/* mprof/

# Clear remote mprof directory
ssh -i keys/merez root@merez "rm -rf /root/bgremove/mprof/*"
