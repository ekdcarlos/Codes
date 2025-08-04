# Import necessary libraries
import heapq

print("Libraries imported. Ready to begin Huffman Coding and MST implementation.")
# Step 1: Frequency table
text = "Dedan Kimathi"
frequency = {}
for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies:", frequency)

# Step 2: Define Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Step 3: Build Huffman Tree
heap = [Node(char, freq) for char, freq in frequency.items()]
heapq.heapify(heap)

while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    merged = Node(None, left.freq + right.freq)
    merged.left = left
    merged.right = right
    heapq.heappush(heap, merged)

root = heap[0]

# Step 4: Generate Huffman Codes
def generate_codes(node, code="", code_map={}):
    if node:
        if node.char is not None:
            code_map[node.char] = code
        generate_codes(node.left, code + "0", code_map)
        generate_codes(node.right, code + "1", code_map)
    return code_map

codes = generate_codes(root)
print("Huffman Codes:", codes)

# Step 5: Encode and decode
encoded = ''.join([codes[c] for c in text if c != " "])
print("Encoded text:", encoded)

# Decode function
def decode(encoded, root):
    decoded = ''
    node = root
    for bit in encoded:
        node = node.left if bit == '0' else node.right
        if node.char:
            decoded += node.char
            node = root
    return decoded

decoded = decode(encoded, root)
print("Decoded text:", decoded)