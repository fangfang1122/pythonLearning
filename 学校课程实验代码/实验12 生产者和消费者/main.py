# （一）编写程序，创建生产者线程和消费者线程以及大小为5的缓冲区。--参考曦哥的代码
def demo1():
    import threading
    from time import sleep

    # 缓冲区
    class Buffer:
        mutex = threading.Condition()

        def __init__(self, max_size: int):
            self.buffer_size = 0
            self.max_size = max_size

        def add_sth(self) -> bool:
            if self.buffer_size != self.max_size:
                self.buffer_size += 1
                return True
            else:
                return False

        def take_sth(self) -> bool:
            if self.buffer_size > 0:
                self.buffer_size -= 1
                return True
            else:
                return False

    # 生产者
    class Producer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Producer, self).__init__(name=name)  # 为什么报错要加行这个？

        def run(self):
            while True:
                sleep(1)
                # 获取锁
                self.buffer.mutex.acquire()

                ok = self.buffer.add_sth()
                if ok:
                    print(f'{self.name} add sth to buffer, current buffer_size: {self.buffer.buffer_size}.')
                else:
                    print(f"{self.name} can not add,because the buffer is full")
                # 释放缩
                self.buffer.mutex.release()

    # 消费者
    class Consumer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Consumer, self).__init__(name=name)

        def run(self):
            while True:
                sleep(2)
                # 获取锁
                self.buffer.mutex.acquire()

                ok = self.buffer.take_sth()
                if ok:
                    print(f"{self.name} take sth from buffer,current buffer_size: {self.buffer.buffer_size}.")
                else:
                    print(f"{self.name} can not add,because the buffer is empty")
                # 释放缩
                self.buffer.mutex.release()

    buffer = Buffer(5)
    p = Producer('Producer', buffer)
    c = Consumer('Consumer', buffer)
    p.start()
    c.start()


# （二）生产者每隔1～3秒就产生一个数字放入缓冲区，如果缓冲区已满，则等待；消费者每隔1～3秒就从缓冲区里面取出一个生产日期较早的数字进行消费，如果缓冲区已空则等待。
def demo2():
    import threading
    from random import randint
    from time import sleep

    # 缓冲区
    class Buffer:
        x = []
        mutex = threading.Condition()

        def __init__(self, max_size: int):
            self.max_size = max_size

        def add_sth(self, num):
            if len(self.x) != self.max_size:
                self.x.append(num)
                return True
            else:
                return False

        def take_sth(self):
            if len(self.x) > 0:
                return True, self.x.pop()
            else:
                return False, 0

    # 生产者
    class Producer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Producer, self).__init__(name=name)  # 为什么报错要加行这个？

        def run(self):
            for i in range(0, 100):
                sleep(randint(1, 3))
                # 获取锁
                self.buffer.mutex.acquire()

                ok = self.buffer.add_sth(i)
                if ok:
                    print(f'{self.name} add "num_{i}" to buffer, current buffer_size: {len(self.buffer.x)}.')
                    self.buffer.mutex.notify()
                else:
                    print(f"{self.name} can not add,because the buffer is full")
                    self.buffer.mutex.wait()
                # 释放缩
                self.buffer.mutex.release()

    # 消费者
    class Consumer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Consumer, self).__init__(name=name)

        def run(self):
            while True:
                sleep(randint(2, 6))
                # 获取锁
                self.buffer.mutex.acquire()

                ok, num = self.buffer.take_sth()
                if ok:
                    print(f"{self.name} get 'num_{num}' from buffer,current buffer_size: {len(self.buffer.x)}.")
                    self.buffer.mutex.notify()
                else:
                    print(f"{self.name} can not get ,because the buffer is empty")
                    self.buffer.mutex.wait()
                # 释放缩
                self.buffer.mutex.release()

    buffer = Buffer(5)
    p = Producer('Producer', buffer)
    c = Consumer('Consumer', buffer)
    p.start()
    c.start()


# 曦哥的代码
def demo11():
    import threading
    from random import randint
    from time import sleep

    # 缓冲区
    class Buffer:
        x = []
        mutex = threading.Condition()

        def __init__(self, buffer_len: int):
            self.max_size = buffer_len

        def append(self, n) -> bool:
            if not self.full():
                self.x.append(n)
                return True
            return False

        def full(self):
            return len(self.x) >= self.max_size

        def empty(self):
            return len(self.x) == 0

        @property
        def len(self):
            return len(self.x)

    # 生产者
    class Producer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Producer, self).__init__(name=name)

        def run(self):
            while True:
                sleep(1)
                # 获取锁
                self.buffer.mutex.acquire()

                n = randint(1, 10)
                ok = self.buffer.append(n)
                if ok:
                    print('%s append %d to buffer, current length: %d.' % (self.name, n, self.buffer.len))
                # 释放缩
                self.buffer.mutex.release()

    # 消费者
    class Consumer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Consumer, self).__init__(name=name)

        def run(self):
            while True:
                sleep(3)
                # 获取锁
                self.buffer.mutex.acquire()
                if not self.buffer.empty():
                    print('Consumer get %d from buffer top.' % self.buffer.x.pop())
                else:
                    print('Consumer cannot get anythings because buffer is empty.')
                # 释放缩
                self.buffer.mutex.release()

    buffer = Buffer(5)
    p = Producer('Producer', buffer)
    c = Consumer('Consumer', buffer)
    p.start()
    c.start()


def demo22():
    import threading
    from random import randint
    from time import sleep

    # 缓冲区
    class Buffer:
        x = []
        mutex = threading.Condition()

        def __init__(self, buffer_len: int):
            self.max_size = buffer_len

        def append(self, n) -> bool:
            if not self.full():
                self.x.append(n)
                return True
            return False

        def full(self):
            return len(self.x) >= self.max_size

        def empty(self):
            return len(self.x) == 0

        @property
        def len(self):
            return len(self.x)

    # 生产者
    class Producer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Producer, self).__init__(name=name)

        def run(self):
            while True:
                sleep(randint(1, 3))
                # 获取锁
                self.buffer.mutex.acquire()

                if self.buffer.full():
                    print('%s waiting because buffer is full.' % self.name)
                    self.buffer.mutex.wait()
                else:
                    n = randint(1, 10)
                    ok = self.buffer.append(n)
                    if ok:
                        print('%s append %d to buffer, current length: %d.' % (self.name, n, self.buffer.len))
                    self.buffer.mutex.notify()
                # 释放缩
                self.buffer.mutex.release()

    # 消费者
    class Consumer(threading.Thread):
        def __init__(self, name: str, buffer: Buffer):
            self.buffer = buffer
            super(Consumer, self).__init__(name=name)

        def run(self):
            while True:
                sleep(randint(1, 3))
                # 获取锁
                self.buffer.mutex.acquire()
                if not self.buffer.empty():
                    print('%s get %d from buffer top.' % (self.name, self.buffer.x.pop(0)))
                    self.buffer.mutex.notify()
                else:
                    print('%s waiting because buffer is empty.' % self.name)
                    self.buffer.mutex.wait()
                # 释放缩
                self.buffer.mutex.release()

    buffer = Buffer(5)
    for i in range(5):
        Producer('Producer%d' % i, buffer).start()

    for i in range(3):
        Consumer('Consumer%d' % i, buffer).start()


if __name__ == "__main__":
    # demo1()
    demo2()
