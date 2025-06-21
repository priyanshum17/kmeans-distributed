#!/usr/bin/env bash
export SPARK_WORKER_CORES=2
export SPARK_DAEMON_MEMORY=512m
export SPARK_DRIVER_MEMORY=512m
export SPARK_EXECUTOR_MEMORY=256m
export SPARK_MASTER_HOST=spark-master
export SPARK_LOCAL_DIRS=/tmp/spark
export SPARK_JARS_DIR=/opt/spark-jars
export SPARK_CONF_DIR=/opt/bitnami/spark/conf
export SPARK_PUBLIC_DNS=localhost
# Perf flags
export SPARK_JAVA_OPTS="-Dspark.shuffle.compress=true -Dspark.io.compression.codec=lz4"