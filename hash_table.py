class HashTable:
    def __init__(self):
        self.collection = {}# attr initialized as empty dictionary
    
    def hash(self, key):# loop through key|finds unicode value of each char|returns the sum
        key_sum = 0
        for char in key:
            key_sum += ord(char)
        return key_sum
    
    def add(self, key, value):
        # key_hash is holding unicode value of key
        key_hash = self.hash(key)
        # if hash value exists: store the key value pair within the existing hash value
        if key_hash in self.collection:
            self.collection[key_hash][key] = value
        else:
            # within collection dict a new dictionary is nested within under key_hash holding key value pair
            # this includes the value being dynamically added if the key_hash already exists
            self.collection[key_hash] = {key: value}

    def remove(self, key):
        # takes key then computes in unicode
        key_hash = self.hash(key)
        # confirm if key exists in collection, inner dictionary, after confirming the hash exists
        if key_hash in self.collection and key in self.collection[key_hash]:
            # goes into the unicode value holding key value pairs and removes it if it exists
            # if it doesn't exist the block is skipped and no error is thrown
            self.collection[key_hash].pop(key)

    def lookup(self, key):
        #compute the hash of the key once more
        key_hash = self.hash(key)
        #if the key exists return the key's value
        if key_hash in self.collection and key in self.collection[key_hash]:
            return self.collection[key_hash][key]
        # else return None
        else:
            return None