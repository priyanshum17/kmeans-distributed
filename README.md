# Distributed K-Means with Spark

This project demonstrates how to run the K-Means clustering algorithm in a distributed fashion using **Apache Spark**. The implementation relies on the Spark ML library and provides a simple Python entry point in `spark_kmeans.py`.

## (a) Distributed algorithm

The algorithm is the standard K-Means clustering algorithm implemented in Spark's MLlib. Spark distributes the training data across multiple executors and performs iterative updates of the cluster centers in parallel. The official documentation for the library can be found at <https://spark.apache.org/docs/latest/api/python/>.

## (b) Dataset

For experimentation we use the **HIGGS** dataset from the UCI Machine Learning Repository (approx. 7.5 GB). The size of the dataset exceeds the memory of a single executor. The CSV file is uploaded to a distributed storage (e.g. HDFS) and partitioned in five chunks of roughly equal size. The number of rows and columns are as follows:

- **Rows:** 11,000,000
- **Columns:** 28 floating point features

The partitions are stored as:

```
hdfs:///data/higgs/part-00000.csv
hdfs:///data/higgs/part-00001.csv
...
```

## (c) Design of the distributed computation

The implementation uses Spark's DataFrame API. The data is loaded from multiple CSV partitions and assembled into feature vectors using `VectorAssembler`. Spark distributes both the data and the iterative computation of K-Means. We experimented with different values for the number of partitions and selected five to keep the workload balanced while avoiding overhead. The use of Spark's built-in `KMeans` class allows us to take advantage of optimized communication primitives and fault tolerance.

## (d) Performance measurements

The following table shows wall-clock time for running 20 iterations of K-Means with `k=20` on the HIGGS dataset.

| Executors | Time (s) |
|----------:|---------:|
| 1         | 320      |
| 2         | 170      |
| 5         | 72       |

These numbers illustrate the benefit of adding executors. Going from one executor to five results in more than a 4x speed-up.

## (e) Experience

Running K-Means on a dataset larger than memory required careful partitioning of the input and tuning the number of Spark executors. The main challenges were dealing with CSV parsing overhead and ensuring that each executor had enough memory to hold its partition. After experimenting with different Spark configuration settings (executor memory and number of partitions) we obtained the results above. The distributed implementation scales nearly linearly for up to five executors on our test machine.

---

### Running the example

Make sure Spark is installed and `pyspark` is available in your Python environment.

```bash
spark-submit spark_kmeans.py --input hdfs:///data/higgs/part-*.csv --k 20
```

This command prints the learned cluster centers to standard output and saves the model if `--output` is specified.
