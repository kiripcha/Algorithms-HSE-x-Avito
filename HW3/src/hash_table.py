class HashTable:
    def __init__(self, size=8):
        '''
        заелизация хеш-таблицы
        с цепочками для разрешения коллизий
        '''
        self.size = size
        self.count = 0 
        self.buckets = [[] for _ in range(size)]  
        self.load_factor_threshold = 0.75 

    def _hash(self, key):
        '''вычисляет хеш-индекс для ключа'''
        return hash(key) % self.size

    def _resize(self):
        '''удваивает размер хеш-таблицы и перехеширует элементы'''
        old_buckets = self.buckets
        self.size *= 2
        self.buckets = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        '''вставляет пару ключ-значение в хеш-таблицу'''
        if (self.count + 1) / self.size > self.load_factor_threshold:
            self._resize()

        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = [key, value] 
                return

        bucket.append([key, value])
        self.count += 1

    def get(self, key):
        '''возвращает значение по ключу'''
        index = self._hash(key)
        bucket = self.buckets[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None

    def remove(self, key):
        '''удаляет пару ключ-значение по ключу'''
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)
                self.count -= 1
                return True
        return False