# Blockchain in Python

This repository contains a Python implementation of a basic blockchain. It includes features such as block mining with proof-of-work and chain validation. The code was written as an educational project inspired by the tutorial available on [drlee.io](https://drlee.io/building-your-own-blockchain-in-python-a-step-by-step-guide-ec10ea6c976d).

## Features

- **Genesis Block Creation**: Automatically generates the first block in the blockchain.
- **Proof-of-Work Mining**: Ensures that each block's hash starts with a specified prefix (`555` by default).
- **Blockchain Validation**: Verifies the integrity of the entire chain.
- **JSON Export**: Saves the blockchain data to a JSON file for further analysis or sharing.

### JSON Output

The blockchain is also saved to a `dane.json` file, where each block is represented as a dictionary.

Inspired by the tutorial from [Dr. Lee's blog](https://drlee.io/building-your-own-blockchain-in-python-a-step-by-step-guide-ec10ea6c976d).
