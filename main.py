import hashlib

class dataBlock:

    def __init__(self, previous_block_hash, transection_list, block_index):
        self.previous_block_hash = previous_block_hash # Previous Hash
        self.transection_list = transection_list

        self.block_index = block_index+1 #Block index
        self.block_data = " | ".join(transection_list) # Transection or Block Data
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # Block Hash

t_list1 = "Alice send 1 BTC to Bob"
t_list2 = "Bob send 20 BTC to Charlie"
t_list3 = "Charlie send 100 BTC to Elon"
t_list4 = "Elon send 10000 BTC to Pitch"
t_create = "Team1 VS Team2"
t_result = ""
team = ['BRU', 'BAC', 'VCF', 'PSG']

first_block = dataBlock("First Block", [t_list1, t_list2], 0)
second_block = dataBlock(first_block.block_hash, [t_list3,t_list4], first_block.block_index)

print("Block Data : " + first_block.block_data)
print("Previous Block Hash : " + first_block.previous_block_hash)
print("Block Hash : " + first_block.block_hash)
print("Block Index : %d" % (first_block.block_index))
print("")
print("Block Data : " + second_block.block_data)
print("Previous Block Hash : " + second_block.previous_block_hash)
print("Block Hash : " + second_block.block_hash)
print("Block Index : %d" % (second_block.block_index))
#print(hashlib.sha256('1234'.encode()).hexdigest())