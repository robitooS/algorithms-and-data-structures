import time
import random

class Node:
    def __init__(self, value, key):
        self.data = value
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(0, 0) 
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lenght = 0
        
    def add_node(self, node: Node):
        previous_node = self.tail.prev
        node.prev = previous_node
        node.next = self.tail
        previous_node.next = node
        self.tail.prev = node
        self.lenght += 1
        
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.lenght -= 1
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_map = {}
        self.dll = LinkedList()
        
    def get(self, key):
        node = self.cache_map.get(key)
        if not node:
            return -1
        self.dll.remove(node)
        self.dll.add_node(node)
        return node.data
        
    def put(self, key, value):
        node = self.cache_map.get(key)
        
        if node:
            node.data = value
            self.dll.remove(node)
            self.dll.add_node(node)
            return

        new_node = Node(value, key) 
        
        if self.dll.lenght == self.capacity: 
            lru_node = self.dll.head.next
            self.dll.remove(lru_node) 
            self.cache_map.pop(lru_node.key) 

        self.dll.add_node(new_node)
        self.cache_map[key] = new_node 

class SlowListCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        
    def get(self, key):
        for i, (k, v) in enumerate(self.list):
            if k == key:
                item = self.list.pop(i) 
                self.list.append(item) 
                return v
        return -1
        
    def put(self, key, value):
        if self.get(key) != -1: 
            return

        if len(self.list) >= self.capacity:
            self.list.pop(0)

        self.list.append((key, value)) 

class SlowHashMapCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.time_tracker = {}
        self.counter = 0 

    def get(self, key):
        if key in self.cache:
            self.time_tracker[key] = self.counter
            self.counter += 1
            return self.cache[key]
        return -1

    def put(self, key, value):
        self.counter += 1
        
        if key in self.cache:
            self.cache[key] = value
            self.time_tracker[key] = self.counter
            return

        if len(self.cache) >= self.capacity:
            lru_key = None
            min_time = float('inf')
            
            for k, t in self.time_tracker.items(): 
                if t < min_time:
                    min_time = t
                    lru_key = k
            
            if lru_key:
                del self.cache[lru_key]
                del self.time_tracker[lru_key]

        self.cache[key] = value
        self.time_tracker[key] = self.counter

def run_test(cache_class, num_operations, capacity, name):
    print(f"-> Testando {name}")
    start_time = time.time()
    cache = cache_class(capacity)
    
    for i in range(num_operations):
        key = random.randint(1, capacity * 2) 
        
        if random.random() < 0.7:
            cache.get(key)
        else:
            cache.put(key, i)
            
    end_time = time.time()
    return end_time - start_time

CAPACITY = 1000  
OPERATIONS = 50000 

print(f"--- Teste de Carga de Cache ({OPERATIONS} Ops) ---")
print(f"Capacidade do Cache: {CAPACITY}")
print("-" * 20)

time_hybrid = run_test(LRUCache, OPERATIONS, CAPACITY, "1. LRUCache Híbrido O(1)")
print(f"Resultado Híbrido O(1): {time_hybrid:.4f} segundos")

time_list = run_test(SlowListCache, OPERATIONS, CAPACITY, "2. SlowListCache (GET é O(N))")
print(f"Resultado Lista O(N): {time_list:.4f} segundos")

time_hashmap = run_test(SlowHashMapCache, OPERATIONS, CAPACITY, "3. SlowHashMapCache (PUT é O(N))")
print(f"Resultado Hash Map O(N): {time_hashmap:.4f} segundos")

print("-" * 20)
print("Fim do Teste. Observe a diferença de tempo.")