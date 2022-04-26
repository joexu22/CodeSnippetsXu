import heapq

li = [5,7,9,1,3]

heapq.heapify(li)

heapq.heappush(li,4)

print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))

num = 4
max_heap = []
heapq.heappush(max_heap,(-num, 'x'))

print(max_heap)