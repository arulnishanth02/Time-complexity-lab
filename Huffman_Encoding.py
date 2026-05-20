import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(root, code="", codes={}):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = code
    huffman_codes(root.left, code + "0", codes)
    huffman_codes(root.right, code + "1", codes)
    return codes

chars = input("Enter characters: ").split()
freqs = list(map(int, input("Enter frequencies: ").split()))

heap = [Node(chars[i], freqs[i]) for i in range(len(chars))]
heapq.heapify(heap)

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    merged = Node(None, left.freq + right.freq)
    merged.left = left
    merged.right = right
    heapq.heappush(heap, merged)

root = heap[0]
codes = huffman_codes(root)
print("Huffman Codes:", codes)