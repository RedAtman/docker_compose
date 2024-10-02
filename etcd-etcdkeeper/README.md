# README

1. Start the server: `docker compose up -d`
   * If a k8s is running simultaneously, it may occupy port 2379.
2. ectdkeeper: Open your browser and go to http://localhost:8080
3. Change the host: `etcd:2379` or `IP:2379`
   * Get the IP: `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' etcdkeeper_etcd_1`
