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

    for x in range(x_length):
        for y in range(y_length):
            if x==0 and y==0:
                result[x][y]=after[x][y]
            elif y==0:
                result[x][y] = after[x][y]-after[x-1][y]
            elif x==0:
                result[x][y] = after[x][y]-after[x][y-1]
            else:
                result[x][y] = (after[x][y]+after[x-1][y-1]) - (after[x-1][y]+after[x][y-1])
        
    return result
