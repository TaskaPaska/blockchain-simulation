from datetime import datetime
from hashlib import sha256


class Block:
  def __init__(self, transactions, previous_hash, nonce=0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()

  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())

  def generate_hash(self):
    # hash the blocks contents
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)

    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()


transaction1 = {
  'amount': '30',
  'sender': 'Alice',
  'receiver': 'Bob'}
transaction2 = {
  'amount': '200',
  'sender': 'Bob',
  'receiver': 'Alice'}
transaction3 = {
  'amount': '300',
  'sender': 'Alice',
  'receiver': 'Timothy' }
transaction4 = {
  'amount': '300',
  'sender': 'Rodrigo',
  'receiver': 'Thomas' }
transaction5 = {
  'amount': '200',
  'sender': 'Timothy',
  'receiver': 'Thomas' }
transaction6 = {
  'amount': '400',
  'sender': 'Tiffany',
  'receiver': 'Xavier' }

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]
