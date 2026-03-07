from redis_client import RedisClient


def main():
    # 创建redis客户端实例
    redis_client = RedisClient(host="localhost", port=6379, db=0)
    print("-- 基本操作 --")
    redis_client.set("myuser", "daheige1")
    print("获取username:%s" % (redis_client.get('myuser')))

    redis_client.hset("my_hash", "a", 2)
    redis_client.delete("myuser")

    redis_client.setex("myuser1", 1200, "abc")

    r = redis_client.get_client()
    r.set('foo', 5)
    redis_client.close()


# 执行main 函数
if __name__ == "__main__":
    main()
