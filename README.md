# File Squeezer: Huffman Coding Compressor

A Python-based lossless file compression utility that uses the **Huffman Coding Algorithm**. This project was developed for a **Design and Analysis of Algorithms** course to demonstrate greedy programming and efficient data structures.

## 💡 How it Works
Huffman coding is a greedy algorithm that assigns variable-length binary codes to characters based on their frequencies. 
1. **Frequency Analysis**: The program scans the input file and counts occurrences of each byte.
2. **Tree Construction**: Using a **Priority Queue (Min-Heap)**, it builds a binary tree where the most frequent characters are closer to the root.
3. **Encoding**: Shorter bit-sequences are assigned to frequent characters, and longer sequences to rare ones.
4. **Serialization**: The frequency table is stored in the file header so the "squeezer" can reconstruct the tree for decompression.



---

## 🚀 Features
* **Lossless Compression**: Perfectly reconstructs original files bit-by-bit.
* **Binary Support**: Not just for `.txt` files! It can compress images, PDFs, and executables by processing raw bytes.
* **Efficient Header**: Uses Python's `struct` module to write a compact binary header.
* **Dynamic Padding**: Automatically handles bit-alignment to ensure files stay byte-aligned.

---

## 🛠️ Usage

### Compression
To "squeeze" a file:
```bash
python Huffman.py compress <input_file> <output_file>
```
*Example:* `python Huffman.py compress document.pdf document.huff`

### Decompression
To restore a file:
```bash
python Huffman.py decompress <compressed_file> <restored_file>
```
*Example:* `python Huffman.py decompress document.huff restored_document.pdf`

---

## 📊 Performance Metrics
The program outputs the following statistics after each operation:
* **Original Size**: Size in bytes before compression.
* **Compressed Size**: Size in bytes after compression (including header).
* **Compression Ratio**: The efficiency of the "squeeze" (lower is better).

---

## 🏗️ Technical Implementation Details
* **Language**: Python 3.x
* **Core Libraries**: 
    * `heapq`: For the Min-Heap priority queue.
    * `struct`: For packing binary data into the file header.
    * `os`: For file size calculations and path handling.
* **Complexity**: 
    * **Time**: $O(n \log n)$ where $n$ is the number of unique symbols.
    * **Space**: $O(n)$ to store the tree and frequency map.
---

## 🛠️ Getting Started

### Prerequisites
* **Python 3.6 or higher**: This project uses type hinting and the `struct` module, which are standard in modern Python installations.
* No external dependencies (like `pip install`) are required!

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/file-squeezer-huffman.git
   cd file-squeezer-huffman
   ```
2. **Prepare a test file:**
   Create a simple text file named `test.txt` or use any existing file (image, pdf, etc.).

---

## 🖥️ How to Run

The script operates via the command line. Open your terminal or command prompt and use the following syntax:

### 1. Compressing a File
This will take your original file and "squeeze" it into a `.huff` file.
```bash
python Huffman.py compress test.txt test.huff
```

### 2. Decompressing a File
This reads the `.huff` file and reconstructs the original data.
```bash
python Huffman.py decompress test.huff restored_test.txt
```

### 3. Verification
You can verify the project worked by checking if the original and restored files are identical:
* **Windows (PowerShell):** `Compare-Object -ReferenceObject (Get-Content test.txt) -DifferenceObject (Get-Content restored_test.txt)`
* **Linux/Mac:** `diff test.txt restored_test.txt`

---

## 📂 Project Structure
* `Huffman.py` — The main source code containing the `HuffmanNode` class and compression logic.
* `README.md` — Documentation and instructions.
* `*.huff` — (Generated) The compressed binary output.

---

## ⚖️ License
This project is for educational purposes under the Design Algorithm course. Feel free to use and modify!
