class MyHashMap():
    def __init__(self , size = 10):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _get_hash(self ,key):
        return hash(key) % self.size
    
    def put(self , key , value):
        index = self._get_hash(key)
        bucket = self.buckets[index]

        for i , (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return 
        bucket.append((key, value))
    def get(self,key):
        index = self._get_hash(key)
        bucket = self.buckets[index]

        for k , v in bucket:
            if k == key:
                return v
            
        return None
