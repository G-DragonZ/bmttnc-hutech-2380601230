from blockchain import Blockchain

my_blockchain = Blockchain()
my_blockchain.add_transaction('A', 'B', '10')
my_blockchain.add_transaction('B', 'C', '5')
my_blockchain.add_transaction('C', 'A', '3')
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)

# Create a new block with the proof of work
my_blockchain.createblock(proof=new_proof, previous_hash=previous_block.hash)

# Add more transactions
my_blockchain.add_transaction('A', 'C', '7')
my_blockchain.add_transaction('B', 'A', '2')
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof
new_proof = my_blockchain.proof_of_work(previous_proof)

# Create another block
my_blockchain.createblock(proof=new_proof, previous_hash=previous_block.hash)

# Display the blockchain
print("=== Blockchain ===")
chain = my_blockchain.get_chain()
for block in chain:
    print(f"\nBlock #{block.index}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Proof: {block.proof}")
    print(f"Hash: {block.hash}")

# Validate the blockchain
print("\n=== Chain Validation ===")
is_valid = my_blockchain.is_chain_valid(chain)
print(f"Is blockchain valid? {is_valid}")
