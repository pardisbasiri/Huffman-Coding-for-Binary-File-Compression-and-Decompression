import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_nodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        print_nodes(node.left, newVal)
    if node.right:
        print_nodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")
        huffman_codes[node.symbol] = newVal

def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as file:
        bit_string = ''
        byte = file.read(1)
        while byte:
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)

    frequencies = {}
    for i in range(0, len(bit_string), 8):
        chunk = bit_string[i:i+8]
        frequencies[chunk] = frequencies.get(chunk, 0) + 1

    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1])

    nodes = [Node(freq, symbol) for symbol, freq in sorted_frequencies]

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = '0'
        right.huff = '1'
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    huffman_tree = nodes[0]

    print_nodes(huffman_tree)

    bit_string_out = ''
    for i in range(0, len(bit_string), 8):
        chunk = bit_string[i:i+8]
        bit_string_out += huffman_codes[chunk]

    output = bytearray()
    for i in range(0, len(bit_string_out), 8):
        output.append(int(bit_string_out[i:i+8], 2))

    with open(output_filename, 'wb') as file:
        file.write(output)

    compression_ratio = len(bit_string) / len(bit_string_out)
    print("CR:", compression_ratio)

def decompress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as file:
        bit_string = ''
        byte = file.read(1)
        while byte:
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)

    bit_string_out = ''
    i = 0
    pi = -1
    while i < len(bit_string):
        for key in huffman_codes:
            if bit_string[i:i+len(huffman_codes[key])] == huffman_codes[key]:
                bit_string_out += key
                i += len(huffman_codes[key])
                break
        if pi == i:
            break
        pi = i

    output = bytearray()
    for i in range(0, len(bit_string_out), 8):
        output.append(int(bit_string_out[i:i+8], 2))

    with open(output_filename, 'wb') as file:
        file.write(output)

input_filename = 'balloon.jpg'
output_filename = 'balloon_compressed.bin'

huffman_codes = {}
compress_file(input_filename, output_filename)

input_filename_decompressed = 'balloon_compressed.bin'
output_filename_decompressed = 'balloon_decompressed.jpg'

huffman_codes = {}
decompress_file(input_filename_decompressed, output_filename_decompressed)

