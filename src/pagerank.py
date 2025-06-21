#!/usr/bin/env python3
"""
Distributed PageRank
--------------------
Run with:

spark-submit \
  --master ${SPARK_MASTER_URL} \
  --deploy-mode client \
  --total-executor-cores ${TOTAL_CORES} \
  --executor-memory 256m \
  /opt/spark-apps/pagerank.py hdfs:///soc-LiveJournal1.txt 10 320
"""
import sys
from pyspark.sql import SparkSession

def main(path, iterations, partitions):
    spark = (SparkSession.builder
             .appName("PageRank-LiveJournal")
             .getOrCreate())
    sc = spark.sparkContext

    # Load LiveJournal edges, filter comments, partition aggressively
    raw = sc.textFile(path, minPartitions=partitions)\
            .filter(lambda l: l and not l.startswith('#'))
    edges = raw.map(lambda l: tuple(map(int, l.split())))
    links = edges.distinct().groupByKey().cache()

    # Initialise rank = 1.0 for every node
    ranks = links.mapValues(lambda _: 1.0)

    for _ in range(iterations):
        contribs = (links.join(ranks)
                         .flatMap(lambda kv:
                                  [(dst, kv[1][1] / len(kv[1][0]))
                                   for dst in kv[1][0]]))
        ranks = contribs.reduceByKey(lambda a, b: a + b)\
                        .mapValues(lambda r: 0.15 + 0.85 * r)

    ranks.toDF(["node", "rank"])\
         .write.mode("overwrite")\
         .parquet("hdfs:///pagerank_out")

    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: pagerank.py <path> <iterations> <partitions>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
