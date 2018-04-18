from __future__ import print_function
import math

'''Generates a list of integers from one to number.
   Sorts them so that all consecutive integers form
   a perfect square.
   
   ex:
       the whole numbers 1-15 can be sorted:
       9,7,2,14,11,5,4,12,13,3,6,10,15,1,8  
       
    Note:
        Enable print statements for really satisfying output. 
'''
     

# -- global variables

l = range(1,16)
s = []


# -- functions

def getPairs(list):
    matches = {}

    #print(list)
    for i in list:
        keyList = []
        for k in list:
            square = math.sqrt((i+k))
            
            if square.is_integer():
                keyList.append(k)
        matches[i] = keyList
    
    #print(list)    
    return matches

    
def tunnel(num, rank, target, used):

    
    used.append(num)
    moves = list(pairs[num])
    q = 0
    
    toRemove = []
    for i in moves:
        #print("I:", i)
        if i in used:
            #print("Used!!!!", i)
            toRemove.append(i)
            
    for k in toRemove:
        moves.remove(k)
        
    #print("Num:", num, " Rank:", rank, " Used", used, " Moves", moves)
    
    if rank == target:
        #print(" --- RANK REACHED: WRITING ---")
        s.append(num)
        return True
    else:       
        if len(moves) == 0:
            used.pop()
            return False
        else:
            while q < len(moves):
                if tunnel(moves[q], rank+1, target, used):
                    #print(" --- RETURNED TRUE: WRITING ---")
                    s.append(num)
                    return True
                q += 1
            used.pop()
            return False
                

# -- main

pairs = getPairs(l)
#print("PAIRS:", pairs)
stop = False
print("Tunneling...")
for i in l:
    if not stop:
        #print("------- NEW ROOT IS:", i, "--------")
        tunnel(i, 1, len(l), [])
        if len(s) == len(l):
            stop = True

    
print("SORTED ARRAY", s)
#print("PAIRS:", pairs)
