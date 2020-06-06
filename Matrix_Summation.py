'''Matrix Summation:
The algorithm below is used to convert the "before matrix" to "after matrix".
find the "before matrix" given the "after matrix".
s = 0;

for (i = 0; i ≤ x; i += 1) {
    for (j = 0; j ≤ y; j += 1) {
        s = s + before(i, j);
    }
}

after(x, y) = s;
The algorithm is run for each after(x,y) to determine their values.

Example:
[[2,3],    [[2,5]
 [5,7]]     [7,17]]
 before     after
 
Solution:'''

def before(after):
    
    x_length = len(after)
    y_length = len(after[0])
    result = [[0 for j in range(y_length)] for i in range(x_length)] #initializing the result with zeroes
    result[0][0]=after[0][0] #copying the first (0,0) element from after to result
    
    #we use the formula to transform elements from (1,1) through (length-1,length-1)

    for x in range(1,x_length):
        for y in range(1, y_length):
            result[x][y] = (after[x][y]+after[x-1][y-1]) - (after[x-1][y]+after[x][y-1])
                
    #below code is to transform data from (0,1) through (0,n-1) and (1,0) through (n-1,0)
    for x in range(1,x_length):
        result[x][0] = after[x][0]-after[x-1][0]
        
    for y in range(1,y_length):
        result[0][y] = after[0][y]-after[0][y-1]
        
    return result
