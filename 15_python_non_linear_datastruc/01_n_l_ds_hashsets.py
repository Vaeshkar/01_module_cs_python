class HashSet:
    def __init__(self, size=10):
        '''Initialise the hash set with a fixed number of buckets.'''
        self.size = size
        self.buckets = [[] for _ in range(size)]
        
    def hash_func(self, key):
        '''
        A simple hash function that sums character ordinals.
        Then takes modulo with self.size to get an index.
        '''
        # For strings:
        if isinstance(key, str):
            return sum(ord(ch) for ch in key) % self.size
        # For intergers, we can just mod by size directly
        if isinstance(key, int):
            return key % self.size
        # Fallback / naive approach: yes, of course there's a build-in hash function :D
        return hash(key) % self.size
    
    def add(self, key):
        '''
        Insert a key into the set if its not already present.
        '''
        index = self.hash_func(key) # parentheses 
        bucket = self.buckets[index] # square brackets
        
        # check if key already exists
        if key not in bucket:
            bucket.append(key)
            
    def remove(self, key):
        '''
        Remove a key from the set if it exists.
        '''
        index = self.hash_func(key)
        bucket = self.buckets[index]
        
        try:
            bucket.remove(key)
        except ValueError:
            pass # Key wasn't in the bucket, so do nothing
        
    def contains(self, key):
        '''
        Return True if the key is in the set, False otherwise.
        '''
        index = self.hash_func(key)
        bucket = self.buckets[index]
        return key in bucket
    
# Example usage:
my_set = HashSet()

my_set.add("Piano")
my_set.add("Running")
my_set.add("Piano") # Duplicate, won' be inserted twice

print("Contains 'Piano'?", my_set.contains("Piano")) # True
print("Contains 'Skiing'?", my_set.contains("Skiing")) # False

my_set.remove("Piano")
print("Contains 'Piano' after removal?", my_set.contains("Piano")) # False

