# 🌳 Huffman Coding Visualizer
### *A Deep-Dive Educational Tool for Algorithmic Mechanics*

This application is a comprehensive educational platform designed to deconstruct the **Huffman Coding algorithm**. Unlike standard implementations, every component—from the priority queue to the bit-traversal—is manually implemented to demonstrate a transparent, ground-up understanding of data compression.

--------------------------------

## ✨ Key Features

### 🎮 Interactive Visualization
* **Step-by-Step Execution:** Full control with `Previous` and `Next` navigation.
* **Live Tree Construction:** Real-time rendering of the Huffman tree and internal node merging.
* **Memory State:** Visualizes the **Heap/Priority Queue** and **Frequency Tables** as they change.
* **Codec Testing:** Integrated panel to encode and decode custom text using your generated tree.

### 📖 Teaching & Theory
* **Logic Flow:** A dedicated window providing a technical walkthrough and pseudocode for every phase.
* **Formal Proofs:** Deep-dive into the mathematical derivation of Big O time and space complexity.
* **Dynamic Feedback:** Contextual explanations that update based on the current algorithm step.

### 🧪 Performance Driver (The "Chart of Truth")
* **Scalability Testing:** Automated benchmarks for $n$ = 10 to 100,000.
* **Empirical vs. Theoretical:** Real-time plotting of actual execution time (blue) against the theoretical $O(n \log n)$ curve (red dashed).
* **CSV Export:** Save raw performance data for further academic analysis.

---

## 🛠 Manual Implementation ("No Black Boxes")

To ensure total transparency, this project avoids high-level "magic" functions or built-in libraries like `heapq`.

| Operation | Manual Implementation Detail |
| :--- | :--- |
| **Frequency Map** | Linear search through keys (no `.get()` or `defaultdict`) |
| **Priority Queue** | Custom Min-Heap with manual bubble-up/down logic |
| **Encoding** | Character-by-character concatenation (no `.join()`) |
| **Decoding** | Bit-by-bit tree traversal with manual index tracking |
| **Sorting** | Custom Bubble Sort implementation for UI tables |

---

## 📊 Complexity Analysis

### Time Complexity
| Phase | Average Case | Worst Case |
| :--- | :--- | :--- |
| **Frequency Count** | $O(n)$ | $O(n^2)$ |
| **Tree Construction** | $O(k \log k)$ | $O(k \log k)$ |
| **Encoding/Decoding** | $O(n)$ | $O(n \cdot k)$ |
| **Total Pipeline** | **$O(n \log k)$** | **$O(n^2)$** |

> $n$: Length of input text | $k$: Number of unique characters.

### Space Complexity
| Component | Complexity |
| :--- | :--- |
| Huffman Tree / Map | $O(k)$ |
| Encoded String | $O(n \cdot L)$ |
| **Total Space** | **$O((n + k) \cdot L)$** |

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.6+**
* **Tkinter** (included in the Python Standard Library)

### Installation & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/huffman-visualizer.git
   ```
2. Navigate to the directory and run:
   ```bash
   python huffman_gui.py
   ```

---

## 📂 Project Structure
```text
huffman_gui.py
├── 🏗️ HuffmanNode          # Tree node data structure
├── 📊 build_frequency_map  # Manual frequency counting logic
├── 🌲 build_huffman_tree   # Custom heap & tree construction
├── 🔐 generate_codes       # Recursive prefix-code mapping
├── ⚡ encode/decode_manual  # Core manual traversal logic
└── 🖥️ HuffmanGUI           # Primary UI Controller
    ├── LogicFlowWindow     # Algorithm walkthrough
    ├── BigOProofWindow      # Complexity derivation
    └── DriverWindow        # Performance benchmarking & plotting
```

---

## 🎓 Educational Objectives
This tool was built to help students master:
1. **Greedy Algorithms:** Understanding the optimal substructure of Huffman trees.
2. **Data Structures:** Implementing heaps and trees without abstraction layers.
3. **Prefix Codes:** Why no code is a prefix of another.
4. **Empirical Analysis:** Proving that theoretical complexity matches real-world performance.

---
*Created for students, by a student of algorithms.*
