set -e
chown -R 1001:0 /opt/bitnami/spark
exec /opt/bitnami/scripts/spark/entrypoint.sh "$@"
