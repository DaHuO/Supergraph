fileout = open('B-large.out',"w")

with open('B-large.in') as file:
    T = int(file.readline())
    
    for case in range(1, T+1): 
        N = int(file.readline())
        grid = []
        for i in range(2 * N - 1):
            grid = grid + file.readline().strip().split()
        
        newgrid = [int(grid[k]) for k in range(len(grid))]
        grid = newgrid    
        #grid = list(grid)
        grid.sort()
        h = ""
        count = 1
        for j in range(len(grid)):
            if grid[j] == ' ': continue
            if grid[j] != grid[j - 1]:
                count = 1
            else:
                count += 1
            if j != len(grid) - 1:
                if grid[j] != grid[j+1]:
                    if count % 2 ==1:
                        h = h + str(grid[j]) + " "
            else:
                if count % 2 ==1:
                    h = h + str(grid[j])
            
                
      
            
        fileout.write("Case #" + str(case) + ": " + h + "\n")
    
fileout.close()
