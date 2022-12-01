def solution(src, dest):
    #Your code here
    l1 = []
    for x in range(8):
        for y in range(8):
            l1.append([x,y,0])

    s=l1[src]
    d=l1[dest]
    #print(s.x,s.y)
    moves=[]
    
    knightx=[1,2,-1,-2,1,2,-1,-2]
    knighty=[2,1,-2,-1,-2,-1,2,1]
    
    #used = [[False for i in range(8)] for j in range(8)]
    used=[]
    for k in range(8):
        used.append([False]*8)
    #print(used)    
   
    moves.append(s)
    used[s[0]][s[1]]=True
    
    while(len(moves)>0):
        pos=moves[0]
        del moves[0]
        num=pos[2]
        if (pos[0]==d[0] and pos[1]==d[1]):
            return pos[2]
        
        for j in range(8):
            newx=pos[0] + knightx[j]
            newy=pos[1] + knighty[j]
    
            if newx<8 and newy<8 and used[newx][newy]==False:
                used[newx][newy]=True
                moves.append([newx,newy,num+1])
                #print(newx,newy,d1+1)
                
    
print(solution(19,36)) 
print(solution(0,1))
