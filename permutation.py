#Python program prints all permutations with duplicates allowed 

def permutations(string, start, end):
    if start == end-1:
       	print(''.join(string))
    else:
        for current in range(start, end): 
            string[current], string[start] = string[start], string[current] #SWAP
            permutations(string, start+1, end)
            string[current],string[start] = string[start],string[current], # backtrack
def main():
    string = list("ABC")
    length = len(string) #ending index
    permutations(string, 0, length)
 
if __name__ == "__main__":
    main()
