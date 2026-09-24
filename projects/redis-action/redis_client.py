import json
from typing import Any

import redis


class RedisClient:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: str | None = None,
    ):
        """
        初始化Redis连接
        :param host: Redis服务器地址
        :param port: Redis端口
        :param db: 数据库编号
        :param password: 密码（如有）
        """
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            decode_responses=True,  # 自动解码响应为字符串
        )

    def get_client(self) -> Any:
        return self.client

    def set(self, key: str, value: Any, expire: int | None = None) -> bool:
        """
        设置键值对
        :param key: 键
        :param value: 值（可序列化对象）
        :param expire: 过期时间（秒）
        :return: 是否设置成功
        """
        try:
            serialized_value = (
                json.dumps(value) if isinstance(value, (dict, list)) else str(value)
            )
            return self.client.set(key, serialized_value, ex=expire)
        except Exception as e:
            print(f"设置键值失败: {e}")
            return False

    def get(self, key: str) -> Any | None:
        """
        获取键对应的值
        :param key: 键
        :return: 值或None
        """
        try:
            value = self.client.get(key)
            if value is None:
                return None

            # 尝试反序列化JSON
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        except Exception as e:
            print(f"获取键值失败: {e}")
            return None

    def setex(self, key: str, expire: int, value: Any) -> bool:
        """
        设置键值对并设置过期时间
        :param key: 键
        :param expire: 过期时间（秒）
        :param value: 值（可序列化对象）
        :return: 是否设置成功
        """
        try:
            serialized_value = (
                json.dumps(value) if isinstance(value, (dict, list)) else str(value)
            )
            return self.client.setex(key, expire, serialized_value)
        except Exception as e:
            print(f"设置键值失败: {e}")
            return False

    def delete(self, *keys: str) -> int:
        """
        删除一个或多个键
        :param keys: 键列表
        :return: 成功删除的键数量
        """
        try:
            return self.client.delete(*keys)
        except Exception as e:
            print(f"删除键失败: {e}")
            return 0

    def exists(self, key: str) -> bool:
        """
        判断键是否存在
        :param key: 键
        :return: 是否存在
        """
        try:
            return self.client.exists(key) > 0
        except Exception as e:
            print(f"检查键存在性失败: {e}")
            return False

    def expire(self, key: str, expire: int) -> bool:
        """
        设置key有效期
        :param key: 键
        :return: 是否存在
        """
        try:
            return self.client.expire(key, expire) > 0
        except Exception as e:
            print(f"设置key expire失败: {e}")
            return False

    def hset(self, key: str, field: str, value: Any) -> bool:
        """
        设置哈希键值对
        :param key: 哈希键
        :param field: field字段
        :param value: 值（可序列化对象）
        :return: 是否设置成功
        """
        try:
            serialized_value = (
                json.dumps(value) if isinstance(value, (dict, list)) else str(value)
            )
            return self.client.hset(key, field, serialized_value)
        except Exception as e:
            print(f"设置键值失败: {e}")
            return False

    def hmset(self, name: str, mapping: dict[str, Any]) -> bool:
        """
        批量设置哈希表
        :param name: 哈希表名称
        :param mapping: 字段映射
        :return: 是否设置成功
        """
        try:
            pipe = self.client.pipeline()
            for field, value in mapping.items():
                serialized_value = (
                    json.dumps(value) if isinstance(value, (dict, list)) else str(value)
                )
                pipe.hset(name, field, serialized_value)
            pipe.execute()
            return True
        except Exception as e:
            print(f"设置哈希表失败: {e}")
            return False

    def hget(self, key: str, field: str) -> Any | None:
        """
        获取哈希键对应的值
        :param key: 键
        :return: 值或None
        """
        try:
            value = self.client.hget(key)
            if value is None:
                return None
            else:
                return value
        except Exception as e:
            print(f"获取键值失败: {e}")
            return None

    def hgetall(self, name: str) -> dict[str, Any]:
        """
        获取哈希表所有字段和值
        :param name: 哈希表名称
        :return: 字段映射
        """
        try:
            fields = self.client.hgetall(name)
            result = {}
            for field, value in fields.items():
                try:
                    result[field] = json.loads(value)
                except json.JSONDecodeError:
                    result[field] = value
            return result
        except Exception as e:
            print(f"获取哈希表失败: {e}")
            return {}

    def push(self, name: str, *values: Any, left: bool = False) -> int:
        """
        向列表推入元素
        :param name: 列表名称
        :param values: 值列表
        :param left: 是否从左侧推入
        :return: 推入后的列表长度
        """
        try:
            serialized_values = []
            for value in values:
                serialized_values.append(
                    json.dumps(value) if isinstance(value, (dict, list)) else str(value)
                )

            if left:
                return self.client.lpush(name, *serialized_values)
            else:
                return self.client.rpush(name, *serialized_values)
        except Exception as e:
            print(f"推入列表失败: {e}")
            return 0

    def pop(self, name: str, left: bool = True) -> Any | None:
        """
        从列表弹出元素
        :param name: 列表名称
        :param left: 是否从左侧弹出
        :return: 弹出的元素或None
        """
        try:
            if left:
                value = self.client.lpop(name)
            else:
                value = self.client.rpop(name)

            if value is None:
                return None

            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        except Exception as e:
            print(f"弹出列表失败: {e}")
            return None

    def lrange(self, name: str, start: int = 0, end: int = -1) -> list[Any]:
        """
        获取列表范围内的元素
        :param name: 列表名称
        :param start: 起始索引
        :param end: 结束索引(-1表示最后一个)
        :return: 元素列表
        """
        try:
            values = self.client.lrange(name, start, end)
            result = []
            for value in values:
                try:
                    result.append(json.loads(value))
                except json.JSONDecodeError:
                    result.append(value)
            return result
        except Exception as e:
            print(f"获取列表范围失败: {e}")
            return []

    def sadd(self, name: str, *members: Any) -> int:
        """
        向集合添加成员
        :param name: 集合名称
        :param members: 成员列表
        :return: 添加的新成员数
        """
        try:
            serialized_members = []
            for member in members:
                serialized_members.append(
                    json.dumps(member)
                    if isinstance(member, (dict, list))
                    else str(member)
                )
            return self.client.sadd(name, *serialized_members)
        except Exception as e:
            print(f"添加集合成员失败: {e}")
            return 0

    def get_members(self, name: str) -> set:
        """
        获取集合所有成员
        :param name: 集合名称
        :return: 成员集合
        """
        try:
            members = self.client.smembers(name)
            result = set()
            for member in members:
                try:
                    result.add(json.loads(member))
                except json.JSONDecodeError:
                    result.add(member)
            return result
        except Exception as e:
            print(f"获取集合失败: {e}")
            return set()

    def close(self):
        """关闭Redis连接"""
        try:
            self.client.close()
        except Exception as e:
            print(f"关闭连接失败: {e}")
