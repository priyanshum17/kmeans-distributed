# Usage Guide

This project demonstrates running K-Means clustering with Apache Spark.

## Prerequisites
- Python 3.8+
- Apache Spark with PySpark available in the `PATH`

## Running
Execute the following command from the repository root:

```bash
spark-submit spark_kmeans.py --input hdfs:///data/higgs/part-*.csv --k 20
```

Add `--output /path/to/save` to persist the trained model.
