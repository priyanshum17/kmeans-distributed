# Distributed PageRank on LiveJournal (Spark + Docker)

This repo demonstrates how to run PageRank on a 5 GB social-network graph using
only Docker Compose, **Spark 3.5**, and 256 MiB executors—complete with
Prometheus / Grafana monitoring.

## Quick start

```bash
git clone https://github.com/you/distributed-pagerank.git
cd distributed-pagerank

docker compose build

./experiments/run_single.sh          # ~7 min on a laptop

./experiments/run_five.sh            # ~2 min on the same laptop

open http://localhost:8080   # Spark UI
open http://localhost:9090   # Prometheus
open http://localhost:3000   # Grafana (admin/admin)
```

## Repo layout

```bash

docker/          – container specs & monitoring
src/             – PageRank driver code
experiments/     – helper scripts for 1-, 2- & 5-node runs
results/         – JSON speed-test output + sample screenshots
For design rationale, performance numbers, and lessons learned, see REPORT.md.
```
---