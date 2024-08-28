
import pytest


def test_redis_cluster():
    print('-' * 20, 'test_redis_cluster')
    import redis
    from redis.exceptions import RedisError
    key = 'username'

    host = "127.0.0.1"
    port = 7777

    try:
        r = redis.Redis(host=host, port=port, decode_responses=True)
        result = r.get(key)
    except RedisError as e:
        print(e)
        print(e.__dict__)
        # if "MOVED" in str(e):
            # 解析错误信息，获取正确的节点
            # new_host, new_port = e.message.split()[1].split(':')
            # # 重新连接到正确的节点
            # r = redis.Redis(host=new_host, port=int(new_port), decode_responses=True)
            # result = r.get(key)

    except Exception as e:
        print(e)
        print(e.__dict__)
    # print(result)


pytest.main(["--rootdir", ".", "-s", "-v",
            #  "-ra","--color=yes","--capture=sys","--log-cli-level=DEBUG",
            ])
