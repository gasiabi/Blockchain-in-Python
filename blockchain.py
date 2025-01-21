import hashlib
import json
import time


class Block:
    def __init__(self, index, timestamp, data, prior_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prior_hash = prior_hash
        self.nonce = 0  # Zmienna "nonce" potrzebna do dowodu pracy
        self.hash = self.create_hash()  # Hash aktualnego bloku
        self.mining_time = 0  # Czas potrzebny na wydobycie bloku

    def create_hash(self):
        # Funkcja tworząca hash bloku z uwzględnieniem "nonce"
        return hashlib.sha256(f"{self.index}{self.prior_hash}{self.timestamp}{self.data}{self.nonce}".encode()).hexdigest()

    def mine_block(self, suffix):
        # Poszukiwanie zmiennej "nonce", aby hash zaczynał się na podane znaki
        start_time = time.time()
        while not self.hash.startswith(suffix):
            self.nonce += 1
            self.hash = self.create_hash()
        end_time = time.time()
        self.mining_time = end_time - start_time


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Tworzenie bloku Genesis
        self.suffix = '555'  # Wymaganie: skróty mają zaczynać się od 555

    def create_genesis_block(self):
        self.suffix = '555'  # Wymaganie: skróty mają zaczynać się od 555
        # Tworzenie pierwszego bloku
        genesis_index_hash = str(000000).zfill(64)
        genesis_block = Block(0, '01/20/2025', 'Genesis Block', genesis_index_hash)
        genesis_block.mine_block(self.suffix)
        return genesis_block

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.prior_hash = self.get_last_block().hash
        new_block.mine_block(self.suffix)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Weryfikacja spójności łańcucha
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.create_hash():
                return False

            if current_block.prior_hash != previous_block.hash:
                return False

        return True


if __name__ == "__main__":

    my_chain = Blockchain()

    my_chain.add_block(Block(1, '01/20/2025', 'Dane: 100'))
    my_chain.add_block(Block(2, '01/21/2025', 'Dane: 200'))
    my_chain.add_block(Block(3, '01/22/2025', 'Dane: 300'))
    my_chain.add_block(Block(4, '01/23/2025', 'Dane: 400'))
    my_chain.add_block(Block(5, '01/24/2025', 'Dane: 500'))

    print(json.dumps(my_chain.chain, default=lambda o: o.__dict__, indent=4))

    for block in my_chain.chain:
        print(f"Blok {block.index} wygenerowany w {block.mining_time:.4f} sekund")

    # Zapis do pliku
    with open("dane.json", "w") as file:
        json.dump([block.__dict__ for block in my_chain.chain], file, indent=4)
