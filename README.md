# Distributed KMeans with Spark & Docker

This repository demonstrates how to run K-Means clustering with Apache Spark using Docker Compose. Each Spark worker is limited to 256 MiB of memory and metrics are exported to Prometheus with a Grafana dashboard provided.

## Quick start

```bash
git clone https://github.com/you/kmeans-distributed.git
cd kmeans-distributed

docker compose build

./experiments/run_single.sh   # single worker
./experiments/run_five.sh     # 5 workers

open http://localhost:8080   # Spark UI
open http://localhost:9090   # Prometheus
open http://localhost:3000   # Grafana (admin/admin)
```

## Repo layout

```bash
docker/          – container specs & monitoring
spark_kmeans.py  – K-Means driver code
docs/            – additional usage docs
experiments/     – helper scripts for 1-, 2- & 5-node runs
results/         – JSON timing output
```

See `docs/USAGE.md` for detailed usage instructions.
