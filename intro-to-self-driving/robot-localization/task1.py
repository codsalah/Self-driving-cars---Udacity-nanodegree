#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

# sol
for i in range(len(p)):
    if i + 1 in [1, 2]:  
        p[i] *= pHit
    else:
        p[i] *= pMiss

# Output the updated list
print(p)
print(sum(p))