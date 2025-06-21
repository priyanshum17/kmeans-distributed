# experiments/run_two.sh
#!/usr/bin/env bash
set -e
docker compose up -d --build --scale spark-worker=2
sleep 10
docker compose exec spark-master \
  spark-submit /opt/spark-apps/spark_kmeans.py --input hdfs:///data/higgs/part-*.csv --k 20
