import heapq
import os
import struct
import sys


class HuffmanNode:
    def __init__(self, freq, byte_value=None, left=None, right=None):
        self.freq = freq
        self.byte_value = byte_value
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(data: bytes) -> dict:
    frequency = {}
    for b in data:
        frequency[b] = frequency.get(b, 0) + 1
    return frequency


def build_huffman_tree(frequency: dict) -> HuffmanNode:
    heap = [HuffmanNode(freq, byte_value=byte_value) for byte_value, freq in frequency.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        only_node = heapq.heappop(heap)
        return HuffmanNode(only_node.freq, left=only_node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)


def build_codes(node: HuffmanNode, prefix: str = "", code_table=None) -> dict:
    if code_table is None:
        code_table = {}

    if node is None:
        return code_table

    if node.byte_value is not None:
        code_table[node.byte_value] = prefix or "0"
    else:
        build_codes(node.left, prefix + "0", code_table)
        build_codes(node.right, prefix + "1", code_table)

    return code_table


def encode_data(data: bytes, code_table: dict) -> str:
    encoded = []
    for b in data:
        encoded.append(code_table[b])
    return "".join(encoded)


def pad_encoded_text(encoded_text: str) -> tuple[str, int]:
    extra_padding = 8 - len(encoded_text) % 8
    if extra_padding == 8:
        extra_padding = 0

    encoded_text += "0" * extra_padding
    return encoded_text, extra_padding


def get_byte_array(padded_encoded_text: str) -> bytearray:
    if len(padded_encoded_text) % 8 != 0:
        raise ValueError("Encoded text length must be a multiple of 8.")

    byte_array = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
        byte = padded_encoded_text[i:i + 8]
        byte_array.append(int(byte, 2))
    return byte_array


def compress_file(input_path: str, output_path: str) -> None:
    with open(input_path, "rb") as file:
        data = file.read()

    if not data:
        raise ValueError("Input file is empty, nothing to compress.")

    frequency = build_frequency_table(data)
    tree = build_huffman_tree(frequency)
    codes = build_codes(tree)
    encoded_text = encode_data(data, codes)
    padded_text, extra_padding = pad_encoded_text(encoded_text)
    byte_array = get_byte_array(padded_text)

    with open(output_path, "wb") as output_file:
        output_file.write(struct.pack("H", len(frequency)))
        for byte_value, count in frequency.items():
            output_file.write(struct.pack("B", byte_value))
            output_file.write(struct.pack("I", count))
        output_file.write(struct.pack("B", extra_padding))
        output_file.write(byte_array)

    original_size = len(data)
    compressed_size = os.path.getsize(output_path)
    print(f"Compressed '{input_path}' -> '{output_path}'")
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    print(f"Compression ratio: {compressed_size / original_size:.3f}")


def decompress_file(input_path: str, output_path: str) -> None:
    with open(input_path, "rb") as file:
        header_count_data = file.read(2)
        if len(header_count_data) < 2:
            raise ValueError("Invalid compressed file format.")

        num_symbols = struct.unpack("H", header_count_data)[0]
        frequency = {}
        for _ in range(num_symbols):
            symbol_data = file.read(1)
            count_data = file.read(4)
            if len(symbol_data) < 1 or len(count_data) < 4:
                raise ValueError("Invalid compressed file format.")
            byte_value = struct.unpack("B", symbol_data)[0]
            count = struct.unpack("I", count_data)[0]
            frequency[byte_value] = count

        padding_data = file.read(1)
        if not padding_data:
            raise ValueError("Invalid compressed file format.")
        extra_padding = struct.unpack("B", padding_data)[0]
        compressed_bytes = file.read()

    bit_string = "".join(f"{byte:08b}" for byte in compressed_bytes)
    if extra_padding:
        bit_string = bit_string[:-extra_padding]

    tree = build_huffman_tree(frequency)
    output_data = bytearray()
    current_node = tree

    for bit in bit_string:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.byte_value is not None:
            output_data.append(current_node.byte_value)
            current_node = tree

    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

    print(f"Decompressed '{input_path}' -> '{output_path}'")
    print(f"Recovered size: {len(output_data)} bytes")


def print_usage() -> None:
    print("Usage:")
    print("  python Huffman.py compress <input_file> <output_file>")
    print("  python Huffman.py decompress <input_file> <output_file>")
    print("Example:")
    print("  python Huffman.py compress sample.txt sample.huff")
    print("  python Huffman.py decompress sample.huff recovered.txt")


def main() -> None:
    if len(sys.argv) != 4:
        print_usage()
        return

    mode = sys.argv[1].lower()
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    if mode == "compress":
        compress_file(input_path, output_path)
    elif mode == "decompress":
        decompress_file(input_path, output_path)
    else:
        print_usage()


if __name__ == "__main__":
    main()
