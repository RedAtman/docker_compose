# redis-cluster

## depoly

1. launch
`docker-compose up`
OR in demonized mode:
`docker-compose up -d`
2. Stop
`docker-compose down`

Or
```bash
docker compose down && docker compose up -d
```

## usage

### How to direct access one redis cluster node
Each cluster node is isolated on a container on custom network
To lauch redis-cli on master redis1 (for exemple):
`docker run -it --network redis-network --rm redis:6-alpine redis-cli -h redis1`

### How to access cluster via redis-cluster-proxy
with redis-cli on host:
`redis-cli -p 7777`

or with docker:
`docker run -it --network redis-network --rm redis:6-alpine redis-cli -h redis-proxy -p 7777`

## Services Links

**Cluster Proxy**
redis-cluster-proxy: redis://127.0.0.1:7777

**Cluster WebUI**
redisinsight: http://127.0.0.1:5540
