#!/usr/bin/env python

import os
import subprocess

folder = os.path.basename(os.path.realpath("."))

# Get all existing services for this application.
containers_data = subprocess.check_output([
    "docker", "ps",
    "-a", "-q"
])

for container_id in containers_data.decode().split('\n'):
    if not container_id:
        continue
    print("shutting down container {}".format(container_id))
    subprocess.check_output([
       "docker", "rm",
        "-f", "{}".format(container_id)
    ])
   
#remove the network and images(need to add checks and dynamic values)
for i in ["{}_appntw".format(folder)]:
    print("shutting down network {}".format(i))
    subprocess.check_output([ "docker", "network", "rm", "{}".format(i)])

for i in ["{}_webui".format(folder), "{}_hasher".format(folder), "{}_rng".format(folder), "{}_worker".format(folder), "redis"]:
    print("removing image {}".format(i))
    subprocess.check_output([ "docker", "rmi", "{}".format(i)])