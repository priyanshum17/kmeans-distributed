# experiments/run_single.sh
#!/usr/bin/env bash
set -e
docker compose up -d --build --scale spark-worker=1
sleep 10
docker compose exec spark-master \
  spark-submit /opt/spark-apps/pagerank.py hdfs:///soc-LiveJournal1.txt 10 64
