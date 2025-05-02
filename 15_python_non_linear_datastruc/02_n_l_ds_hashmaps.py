class HashMap:
    def __init__(self, size=10):
        '''Initialize the hash map with a fixed number of buckets.'''
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    def hash_func(self, key):
        '''
        A simple hash function.
        For srtings, sum character ordinals mod the size.
        For integers, just mod by size.
        Otherwise, fallback to Python's build-in hash mod size.
        '''
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            return hash(key) % self.size
            
    def put(self, key, value):
        '''
        Insert or update the (key, value) pair into the map.
        '''
        index = self.hash_func(key)
        bucket = self.hash_func[index]
        
        # IF key exists, update its value.
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return # an empty return will finish the for loop inside the function
        
        # Otherwise, insert as new entry
        bucket.append((key, value))
        
    def get(self, key):
        '''
        Retrieve the value for the given key.
        Return 'None' if not found.
        '''
        index = self.hash_func(key)
        bucket = self.hash_func[index]
        
        for (k,v) in bucket:
            if k == key:
                return v
            
        return None
    
    def remove(self, key):
        '''
        Remove the (key, value) pair if it exists.
        '''
        
        index = self.hash_func(key)
        bucket = self.hash_func[index]
        
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
            
    def containsKey(self, key):
        '''
        Check if the map contains a particular key.
        '''
        return self.get(key) is not None

# Example usage:
my_map = HashMap()

my_map.put("Book", 12.99)
my_map.put("Laptop", 999.00) 
my_map.put("Book", 10.99) #Update the value

print("Book price:", my_map.get("Book")) # 10.99 
print("Laptop price:", my_map.get("Laptop")) # 999.00
print("Contains 'Phone'?", my_map.containsKey("Phone")) # False

my_map.remove("Book")
print("Book price after removal:", my_map.get("Book")) # None   