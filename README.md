# Blockchain in Python

This repository contains a Python implementation of a basic blockchain. It includes features such as block mining with proof-of-work and chain validation. The code was written as an educational project inspired by the tutorial available on [drlee.io](https://drlee.io/building-your-own-blockchain-in-python-a-step-by-step-guide-ec10ea6c976d).

## Features

- **Genesis Block Creation**: Automatically generates the first block in the blockchain.
- **Proof-of-Work Mining**: Ensures that each block's hash starts with a specified prefix (`555` by default).
- **Blockchain Validation**: Verifies the integrity of the entire chain.
- **JSON Export**: Saves the blockchain data to a JSON file for further analysis or sharing.

## Getting Started

### Prerequisites

You need Python 3.x installed on your system. No external libraries are required as the implementation relies on Python's standard library.

### Running the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockchain-python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd blockchain-python
   ```
3. Run the script:
   ```bash
   python blockchain.py
   ```

### Example Output

The script will:
1. Generate a genesis block.
2. Add several blocks with sample data.
3. Print the blockchain data in JSON format.
4. Save the blockchain to a file named `dane.json`.

### Sample Execution

```json
[
    {
        "index": 0,
        "timestamp": "01/20/2025",
        "data": "Genesis Block",
        "prior_hash": "0000000000000000000000000000000000000000000000000000000000000000",
        "nonce": 5536,
        "hash": "555...",
        "mining_time": 2.34
    },
    {
        "index": 1,
        "timestamp": "01/20/2025",
        "data": "Dane: 100",
        "prior_hash": "555...",
        "nonce": 8721,
        "hash": "555...",
        "mining_time": 3.21
    }
]
```

### JSON Output

The blockchain is also saved to a `dane.json` file, where each block is represented as a dictionary.

## Customization

- **Difficulty Adjustment**: Modify the `suffix` variable in the `Blockchain` class to change the mining difficulty (e.g., `suffix = '5555'`).
- **Data Input**: Replace the sample data with your own in the `add_block` calls.

## License

This project is for educational purposes and is free to use under the MIT license.

---

Inspired by the tutorial from [Dr. Lee's blog](https://drlee.io/building-your-own-blockchain-in-python-a-step-by-step-guide-ec10ea6c976d).
