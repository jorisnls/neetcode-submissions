class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.hashMap.append((key, value))
        else:
            oldVal = self.get(key)
            for i in range(len(self.hashMap)):
                if self.hashMap[i] == (key,oldVal):
                    self.hashMap[i] = (key, value)

    def get(self, key: int) -> int:
        for item in self.hashMap:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        value = self.get(key)
        try:
            self.hashMap.remove((key, value))
        except:
            pass
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)