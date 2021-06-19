# Infrastructure

- To build the infrastructure: `docker-compose up -d`

- To scale it:  `docker-compose scale <service>=<number_of_instances>`
                `<service> = rng, worker, hasher`

- To purge it and start fresh: `python3 .\shut_containers.py`
