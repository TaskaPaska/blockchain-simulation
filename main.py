from blockchain import Blockchain, Block

# Example transactions
transaction1 = {'amount': '30', 'sender': 'Alice', 'receiver': 'Bob'}
transaction2 = {'amount': '200', 'sender': 'Bob', 'receiver': 'Alice'}
transaction3 = {'amount': '300', 'sender': 'Alice', 'receiver': 'Timothy'}
transaction4 = {'amount': '300', 'sender': 'Rodrigo', 'receiver': 'Thomas'}
transaction5 = {'amount': '200', 'sender': 'Timothy', 'receiver': 'Thomas'}
transaction6 = {'amount': '400', 'sender': 'Tiffany', 'receiver': 'Xavier'}

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

# Creating a blockchain object
blockchain = Blockchain()
blockchain.add_block([transaction1, transaction2, transaction3])

# Checking if chain validation works correctly
# Everything is working as expected so far
blockchain.print_chain()
print(blockchain.is_chain_valid())  # Returned True

# Changing one of the previous transactions
transaction1['amount'] = '0'
transaction1['sender'] = 'None'
transaction1['receiver'] = 'None'
blockchain.print_chain()
print(blockchain.is_chain_valid())  # Returned False


