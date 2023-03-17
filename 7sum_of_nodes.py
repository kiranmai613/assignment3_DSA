def sum_of_nodes(n):
    
    #Calculates the sum of all nodes in a perfect binary tree of height n.
    
    return 2**(n+1) - 1


print(sum_of_nodes(4))
