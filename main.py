import hashlib

f = open ("datatest.txt","a")
'''
f = open ("datatest.txt","a")
f.write("test-message!\n")
f.close

f = open("datatest.txt","r")
print(f.read())
'''



class dataBlock:

    def __init__(self, previous_block_hash, transection_list, block_index):
        self.previous_block_hash = previous_block_hash # Previous Hash
        self.transection_list = transection_list

        self.block_index = block_index+1 #Block index
        self.block_data = " -----> ".join(transection_list) # Transection or Block Data
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() # Block Hash
    #blockCreate
    def blockCreate(self, previous_b_hash, data_list, b_index):
        self.new_block = self(previous_b_hash, data_list, b_index)
        return new_block
    #blockShow_selecIndex
    def blockSelect(self, b_index):
        pass
    #Database
#print all block from file
def printallblock(s):
    c=1
    for i in s:
        if(i =="["):
            
            if(c == 1):
                print("block data >>>",end ="")
            if(c == 2):
                print("previous block hash>>",end ="")
            if(c == 3):
                print("Blockindex>",end ="")
                c=0
            c+=1
        if (i!="]" and i!="[" and i!="\'"):
            print(i,end ="")
#blockPrint
def blockPrint(transections):
    print("")
    print("Block Data >> " + transections.block_data)
    print("Previous Block Hash >> " + transections.previous_block_hash)
    print("Block Hash >> " + transections.block_hash)
    print("Block Index >> %d" % (transections.block_index))
    print("")

#blockappend
def blockAppend(transections):
    lst = []
    write_data = ""
    lst.append(transections.block_data)
    lst.append(transections.previous_block_hash)
    lst.append(transections.block_hash)
    lst.append(transections.block_index)
    data_block.append(lst)
#write data to txt
    for i in lst:
        f = open ("datatest.txt","a") 
        write_data = (str(i).split(","))
        f.write(str(write_data))
        #print(str(i).split(","),end=(''))
    f.write("\n"+("-"*100))
    f.close
#data
team_list = ['Team Spirit', 'OG', 'T1', 'Vici Gaming', 'Virtus.pro', 'Invictus Gaming', 'PSG.LGD', 'Team Secret',]
data_block = []

#Genesis block
blocks = dataBlock("0", ["Genesis Block"], 0)
p_b_hash = blocks.block_hash
p_b_index = blocks.block_index
blockAppend(blocks)

#first_block = dataBlock("First Block", [t_list1, t_list2], 0)
#second_block = dataBlock(first_block.block_hash, [t_list3,t_list4], first_block.block_index)
print("\n======== First Block!!! ========")
blockPrint(blocks)
print("================================\n")

#UIs
#Set Variable
print("===== This is Dota2 Scoring with Blockchain =====\n")
block_transection = []
f1 = 99
team_number = 0
teamA = ""
teamB = ""
winner = ""
loser = ""
#Team Counting

while f1 != 0:
    print("[1] Add new Block")
    print("[2] Show current Block")
    print("[3] Show all Block")
    print("[4] Show Selected Block")
    print("[0] Exit")
    
    f1 = int(input(("\nSelect mode > ")))
    print("")

    if f1 == 1:
        team_number = 0
        for i in team_list:
            team_number += 1
            print("[%d]" % (team_number) + i)
        #Team Select
        while True:
            team1 = int(input("\nPick the first team : "))
            if team1 > len(team_list):
                print("please enter team name in tournaments!!!")
                continue
            team2 = int(input("Pick the second team : "))
            if team2 > len(team_list):
                print("please enter team name in tournaments!!!")
                continue
            teamA = team_list[team1-1]
            teamB = team_list[team2-1]
            if teamA != teamB:
                break
            else:
                print("Do not enter the same Team!!!")
        
        print("\n===== "+ teamA +" VS "+ teamB +" =====\n")
        #Select Best of 
        while True:
            bo = int(input("This match is Best of (1|3|5) : "))
            if bo == 1 or bo == 3 or bo == 5:
                break
            else:
                print("please insert best of 1 or 3 or 5!!!")
        #Enter Score
        while True:
            score1 = int(input("Insert " + teamA + " score : "))
            score2 = int(input("Insert " + teamB + " score : "))
            total_score = score1 + score2
            if bo == 1:
                if (score1 == 1 or score2 == 1) and (total_score == 1):
                    if score1 > score2:
                        winner = teamA
                        loser = teamB
                        print("===== The Winner is " + teamA + " =====")
                    else:
                        winner = teamB
                        loser = teamA
                        print("===== The Winner is " + teamB + " =====")
                    break
            if bo == 3:
                if (score1 == 2 or score2 == 2) and (total_score <= 3 and total_score > 1):
                    if score1 > score2:
                        winner = teamA
                        loser = teamB
                        print("===== The Winner is " + teamA + " =====")
                    else:
                        winner = teamB
                        loser = teamA
                        print("===== The Winner is " + teamB + " =====")
                    break
            elif bo == 5:
                if (score1 == 3 or score2 == 3) and (total_score <= 5 and total_score > 2):
                    if score1 > score2:
                        winner = teamA
                        loser = teamB
                        print("===== The Winner is " + teamA + " =====")
                    else:
                        winner = teamB
                        loser = teamA
                        print("===== The Winner is " + teamB + " =====")
                    break
            else:
                print("please enter correct score!!!")
        
        #Put match result into blockchain
        data_input = (teamA + ' ' + str(score1) + " : " + str(score2)+ ' ' + teamB + ' and The winner is ' + "\\" + winner + "/")
        print(teamA + ' ' + str(score1) + " : " + str(score2)+ ' ' + teamB + ' and The winner is ' + "\\" + winner + "/")
        block_transection.append(data_input)
        #blockPrint(blockCreate(p_b_hash, block_transection, p_b_index))
        blocks = dataBlock(p_b_hash, block_transection, p_b_index)
        blockAppend(blocks)
        print("\n====== Create New Block!!! ======")
        blockPrint(blocks)
        p_b_hash = blocks.block_hash
        p_b_index = blocks.block_index
        print("=================================\n")
    elif (f1 == 2):
        print("\n====== Show Current Block!!! ======")
        blockPrint(blocks)
        print("=================================\n")
    elif (f1 == 3):
        print("\n====== Show all Block!!! ======")
        with open("datatest.txt","r+") as rb:
            printallblock(rb.read())
        print("=================================\n")
    elif (f1 == 4):
        s_index = int(input("Please enter index of block > "))
        if s_index > len(data_block):
            print("Invalid index of block!!!")
        else:
            print("\n====== Show Block index %d =======\n" % (s_index))
            #print(data_block[s_index-1])
            j = len(data_block[s_index-1])
            for i in data_block[s_index-1]:
                if j == 4:
                    print("Block Data >> " + str(i))
                elif j == 3:
                    print("Previous Block Hash >> " + str(i))
                elif j == 2:
                    print("Block Hash >> " + str(i))
                elif j == 1:
                    print("Block Index >> " + str(i))
                else:
                    break
                j -= 1
            print("\n=================================\n")
    elif (f1 == 0):
        break
 


#print(hashlib.sha256('1234'.encode()).hexdigest())