cp /etc/redis/redis.conf.template /etc/redis/redis.conf
sed -i "s/\$X_REDIS_PORT/$X_REDIS_PORT/g" /etc/redis/redis.conf
redis-server /etc/redis/redis.conf
