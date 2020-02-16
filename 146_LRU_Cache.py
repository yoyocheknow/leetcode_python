# -*- coding:utf-8 -*-
from collections import deque
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.dic={}
        self.queue = deque([])

    def queue_update(self, key):
        ## For every operation we want to update queue
        # 对于每个操作都要update 双向队列
        # 对于get操作，如果key在这个queue中，那么先删掉再append进去末尾，表示此key刚被使用过。
        # 对于put操作，如果要操作的key不在queue中，而且queue已满，此时需要淘汰最近没有使用过的key，
        # 那么就淘汰queue早就append进去的key，也就是popleft(),弹出最左边的key，再删掉字典中对应的key
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.queue_update(key)
        return self.dic.get(key,-1)


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dic.keys() and len(self.dic)>=self.capacity:
            while 1:
                try:
                    evacuate=self.queue.popleft()
                    del self.dic[evacuate]
                    break
                except Exception:
                    continue

        self.queue_update(key)
        self.dic[key]=value


if __name__ == "__main__":

    obj=LRUCache(4)
    param1=obj.get(1)
    print param1
    obj.put(1,'11')
    obj.put(2, '22')
    obj.put(3, '33')
    obj.put(4, '44')
    obj.put(5, '55')
    param1=obj.get(1)
    print param1