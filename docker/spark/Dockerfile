FROM bitnami/spark:3.5

# Switch to root to perform installation steps. The parent image
# sets `USER 1001`, so build commands would otherwise run without
# sufficient privileges to modify files under `/`.
USER root

ARG JMX_EXPORTER_VERSION=0.20.0

RUN mkdir -p /opt/jmx && \
    curl -fsSL -o /opt/jmx/jmx_prometheus_javaagent.jar \
        https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/${JMX_EXPORTER_VERSION}/jmx_prometheus_javaagent-${JMX_EXPORTER_VERSION}.jar && \
    chmod 444 /opt/jmx/jmx_prometheus_javaagent.jar

COPY spark-env.sh            /opt/bitnami/spark/conf/spark-env.sh
COPY metrics.properties      /opt/bitnami/spark/conf/metrics.properties
COPY config.yaml             /opt/jmx/config.yaml

COPY entrypoint.sh           /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Switch back to the non-root Spark user for runtime
USER 1001

ENTRYPOINT ["/entrypoint.sh"]