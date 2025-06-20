import argparse
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler


def main():
    parser = argparse.ArgumentParser(description="Distributed KMeans using PySpark")
    parser.add_argument("--input", required=True, help="Path to CSV dataset")
    parser.add_argument("--k", type=int, default=10, help="Number of clusters")
    parser.add_argument("--output", help="Path to save the model")
    args = parser.parse_args()

    spark = SparkSession.builder.appName("DistributedKMeans").getOrCreate()

    # Load CSV and assemble features
    df = spark.read.csv(args.input, header=True, inferSchema=True)
    features = df.columns
    assembler = VectorAssembler(inputCols=features, outputCol="features")
    assembled = assembler.transform(df).select("features")

    kmeans = KMeans(k=args.k, seed=1)
    model = kmeans.fit(assembled)

    if args.output:
        model.save(args.output)

    print("Cluster Centers:")
    for center in model.clusterCenters():
        print(center)

    spark.stop()


if __name__ == "__main__":
    main()
