import copy # fork a chain
import datetime # get real time for timestamps
import hashlib
from select import select # hash

class MinimalBlock():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    
    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()
    
    def verify(self): # check data types of all info in a block
        instances = [self.index, self.timestamp, self.previous_hash, self.hash]
        types = [int, datetime.datetime, str, str]
        if sum(map(lambda inst_, type_: isinstance(inst_, type_), instances, types)) == len(instances):
            return True
        else:
            return False

class MinimalChain():
    def __init__(self): # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    
    def get_genesis_block(self): 
        return MinimalBlock(0, 
                            datetime.datetime.utcnow(), 
                            'Genesis', 
                            'B6216139_B6210526')
    
    def add_block(self, data):
        self.blocks.append(MinimalBlock(len(self.blocks), 
                                        datetime.datetime.utcnow(), 
                                        data, 
                                        self.blocks[len(self.blocks)-1].hash))
    
    def get_chain_size(self): # exclude genesis block
        return len(self.blocks)-1
    
    def verify(self, verbose=True): 
        flag = True
        for i in range(1,len(self.blocks)):
            if not self.blocks[i].verify(): # assume Genesis block integrity
                flag = False
                if verbose:
                    print(f'Wrong data type(s) at block {i}.')
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f'Wrong block index at block {i}.')
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f'Wrong previous hash at block {i}.')
            if self.blocks[i].hash != self.blocks[i].hashing():
                flag = False
                if verbose:
                    print(f'Wrong hash at block {i}.')
            if self.blocks[i-1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print(f'Backdating at block {i}.')
        return flag
    
    def fork(self, head='latest'):
        if head in ['latest', 'whole', 'all']:
            return copy.deepcopy(self) # deepcopy since they are mutable
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0:head+1]
            return c
    
    def get_root(self, chain_2):
        min_chain_size = min(self.get_chain_size(), chain_2.get_chain_size())
        for i in range(1,min_chain_size+1):
            if self.blocks[i] != chain_2.blocks[i]:
                return self.fork(i-1)
        return self.fork(min_chain_size)
    
c = MinimalChain() # Start a chain

'''
c_forked = c.fork('latest')
print(c_forked.blocks[9].index)

c_forked.blocks[9].index = -9
print(c_forked.blocks[9].index)'''
x=1
team_list = ['Thunder Predator', 
             'Team Aster', 
             'Evil Geniuses',
             'Team Undying', 
             'Alliance', 'T1',
             'OG', 'Virtus.pro', 
             'Invictus Gaming',
             'SG esports', 
             'Elephant', 
             'Fnatic', 
             'Quincy Crew',
             'beastcoast', 
             'Team Spirit', 
             'Vici Gaming', 
             'Team Secret', 
             'PSG.LGD']
tx_list=["Fnatic vs Team Undying in bo1 and the winner is Fnatic with score 1:0",
         "Quincy Crew vs Team Aster in bo1 and the winner is Quincy Crew  with score 1:0",
         "beastcoast vs Alliance in bo1 and the winner is Alliance with score 0:1",
         "Evil Geniuses vs Elephant in bo1 and the winner is Evil Geniuses with score 1:0",
         "Invictus Gaming vs Team Spirit in bo3 the winner is Invictus Gaming with score 2:1",
         "Team Secret vs OG in bo3 the winner is Invictus Gaming with score 2:0",
         "PSG.LGD vs T1 in bo3 the winner is PSG.LGD with score 2:1",
         "Virtus.pro vs Vici Gaming in bo3 the winner is Virtus.pro with score 2:1",
         "Team Spirit vs Fnatic in bo3 the winner is Team Spirit with score 2:0",
         "OG vs Quincy Crew in bo3 the winner is OG with score 2:0",
         "T1 vs Alliance in bo3 the winner is T1 with score 2:0"]

for i in range(len(tx_list)):
    c.add_block(tx_list[i])

while(x!=0):
    c_forked = c.fork('latest')
    print("=======================================================")
    m=int(input("Mode1: print all block\nMode2: add new block\nMode3: print last block \nMode4: test edit\nMode5: exit\n\nselect mode:"))
    print("=======================================================")
    if(m==1):
        
        for i in range (len(c.blocks)):
            print("\n================================================")
            print("block timestamp:" +str(c.blocks[i].timestamp) + "\nblock nuber :" + str(c.blocks[i].index) +"\nblock data: "+ c.blocks[i].data + "\nblock data hash :" + c.blocks[i].hash + "\nblock previous_hash" + str(c.blocks[i].previous_hash) + "}")
            print("================================================\n")

    if(m==2):
        
        print("select team")
        for i in range (len(team_list)):
            print("team " + str(i+1) + ":" + team_list[i])
        select_team =True
        select_bo=True
        select_score=True
        while(select_team):
            t1=int(input("team1 is :"))-1
            print("team1 is"+ team_list[t1])
            if(t1>len(team_list)-1):
                print("please enter exist team")
                continue
        
            t2=int(input("team2 is :"))-1
            print("team2 is"+ team_list[t2])
            if(t2>len(team_list)-1):
                print("please enter exist team")
                continue
            if(t1<0):
                print("cannot select negative number")
            if(t2<0):
                print("cannot select negative number")
            if(t2==t1):
                print("do not select the same team")
                continue
            if(t2!=t1):
                print("team "+ team_list[t1]+ " vs " +  team_list[t2])
                select_team=False
        while(select_bo):
            print("select the match is Best of (1|3|5) ")
            bo=int(input("This match is Best of (1|3|5) :"))
            if(bo==1 or bo==3 or bo==5):
                print("This match is BO "+ str(bo))
                select_bo=False
                
            else:
                print("enter 1 3 or 5")
                continue
        while(select_score):
            if(bo==1):
                s1=int(input("enter team "+team_list[t1]+"score:"))
                if(s1>1):
                    print("enter the possible score in bo1")
                    continue
                if(s1==1):
                    s2=0
                    winner=team_list[t1]
                    select_score=False
                elif(s1==0):
                    s2=1
                    winner=team_list[t2]
                    select_score=False
            if(bo==3):
                s1=int(input("enter team "+team_list[t1]+"score:"))
                s2=int(input("enter team "+team_list[t2]+"score:"))
                if(s1+s2>3):
                    print("enter the possible score in bo3")
                    continue
                if(s1>s2):
                    winner=team_list[t1]
                    select_score=False
                else:
                    winner=team_list[t2]
                    select_score=False
            if(bo==5):
                s1=int(input("enter team "+team_list[t1]+"score:"))
                s2=int(input("enter team "+team_list[t2]+"score:"))
                if(s1+s2>5):
                    print("enter the possible score in bo3")
                    continue
                if(s1>s2):
                    winner=team_list[t1]
                    select_score=False
                else:
                    winner=team_list[t2]
                    select_score=False
                
                
                
                
                
        print(team_list[t1] + " vs " +  team_list[t2] + " in best of" + str(bo) +" and the winner is " + winner + "with score " + str(s1) + ":" + str(s2))
        c.add_block(team_list[t1] + " vs " +  team_list[t2] + " in best of" + str(bo) +" and the winner is " + winner + "with score " + str(s1) + ":" + str(s2))
        
    if(m==3):
        print("block timestamp :"+str(c.blocks[len(c.blocks)-1].timestamp))
        print("block number :"+str(c.blocks[len(c.blocks)-1].index))
        print("block data :"+c.blocks[len(c.blocks)-1].data)
        print("block data hash :"+c.blocks[len(c.blocks)-1].hash)
        print("block privious_hash :"+c.blocks[len(c.blocks)-1].previous_hash)
        
    if(m==4):
        
        print("you selected edit mode\n")
        ed=int(input("select the number of block that you want to edit in the chain (now we have " + str(len(c.blocks)-1) + "block)"))
        print("you select block "+ str(ed))
        print("select data type in the block you want to change")
        cd=int(input("1:index\n2:blockdata\n3:block previous_hash"))
        if(cd==1):
            print("old data is " + str(c.blocks[ed].index))
            temp=int(input("change to:"))
            c_forked = c.fork('latest')
            c_forked.blocks[ed].index = temp
            c_forked.verify()
        if(cd==2):
            print("old data is " + str(c.blocks[ed].data))
            temp=input("change to:")
            c_forked = c.fork('latest')
            c_forked.blocks[ed].data = temp
            c_forked.verify()
        if(cd==3):
            print("old data is " + str(c.blocks[ed].previous_hash))
            temp=int(input("change to:"))
            c_forked = c.fork('latest')
            c_forked.blocks[ed].previous_hash = temp
            c_forked.verify()
    if(m==5):
        print("-- verifing data --")
        c_forked.verify()
        break
        
   
        