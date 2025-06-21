FROM bitnami/spark:3.5

ARG JMX_EXPORTER_VERSION=0.20.0

RUN mkdir -p /opt/jmx && \
    curl -fsSL -o /opt/jmx/jmx_prometheus_javaagent.jar \
        https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/${JMX_EXPORTER_VERSION}/jmx_prometheus_javaagent-${JMX_EXPORTER_VERSION}.jar && \
    chmod 444 /opt/jmx/jmx_prometheus_javaagent.jar

COPY spark-env.sh            /opt/bitnami/spark/conf/spark-env.sh
COPY metrics.properties      /opt/bitnami/spark/conf/metrics.properties
COPY entrypoint.sh           /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]