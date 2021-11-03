import time


class MyQueue:
    def __init__(self, size=20):
        self._content = []
        self._size = size
        self._current = 0

    def setSize(self, size):
        if size < self._current:
            # 如果缩小队列，应删除后面的元素
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def put(self, v, timeout=4):
        # 模拟入队，在列表尾部追加元素
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
            return f'放入元素 {v} 成功'
        else:
            # 队列满，阻塞，超时放弃
            for i in range(timeout):
                time.sleep(1)
                if self._current < self._size:
                    self._content.append(v)
                    self._current = self._current + 1
                    break
            else:
                return '队列已满，超时放弃'

    def get(self, timeout=4):
        # 模拟出队，从列表头部弹出元素
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            # 队列为空，阻塞，超时放弃
            for i in range(timeout):
                time.sleep(1)
                if self._content:
                    self._current = self._current - 1
                    return self._content.pop(0)
            else:
                return '队列为空，超时放弃，无法出队'

    def show(self):
        # 如果列表非空，输出列表
        if self._content:
            print(f'当前队列：{self._content}')
        else:
            print('The queue is empty')

    def empty(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size


if __name__ == '__main__':
    print('please use me as a module')
