#!/usr/bin/env python

import os
import subprocess

project_name = os.path.basename(os.path.realpath("."))

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
for i in ["dockercoins_appntw"]:
    print("shutting down network {}".format(i))
    subprocess.check_output([ "docker", "network", "rm", "{}".format(i)])

for i in ["dockercoins_webui", "dockercoins_hasher", "dockercoins_rng", "dockercoins_worker", "redis"]:
    print("removing image {}".format(i))
    subprocess.check_output([ "docker", "rmi", "{}".format(i)])