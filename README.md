# Infrastructure

- To build the infrastructure: `docker-compose up -d`

- To scale it:  `docker-compose scale <service>=<number_of_instances>`
                where `<service> = rng, worker, hasher`

- To purge it and start fresh: `python3 .\shut_containers.py`

## AWS Setup and Cost 

t2.medium (2 vCPU, 4GB RAM, Low to Moderate network performance) at $0.0464/hour
- 1 instance for UI and Redis
- 1 instance for Worker
- 1 instance for API 
i.e 3*(0.0464*24*30)/month = `100.224$ (+taxes)/month`
