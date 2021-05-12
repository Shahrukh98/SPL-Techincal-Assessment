
def initialize_table(strand_1,strand2):
    lcs_table = list()
    for x in range(len(strand_1)+1):
        lcs_table.append([0 for y in range(len(strand2)+1)])
    print("Initializing Table...")
    for x in lcs_table:
        print(x)
    return lcs_table

def populate_table(lcs_table,strand_1,strand_2):
    for i in range(len(strand_1)+1): 
        for j in range(len(strand_2)+1): 
            if i == 0 or j == 0: 
                lcs_table[i][j] = 0
            elif strand_1[i-1] == strand_2[j-1]: 
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else: 
                lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])
    print("Populating Table...")
    for x in lcs_table:
        print(x)

def backtrack_sequence(table,strand_1,strand_2):
    l_strand1=len(strand_1)
    l_strand2=len(strand_2)
    ind = table[l_strand1][l_strand2]
    longest_common_sequence = ""
    print("Calculating LCS...")
    while(l_strand1 != 0 and l_strand2 != 0):
        if(strand_1[l_strand1-1] == strand_2[l_strand2-1]):
            longest_common_sequence=strand_1[l_strand1-1]+longest_common_sequence
            l_strand1-=1
            l_strand2-=1
            ind-=1
        elif(table[l_strand1-1][l_strand2] > table[l_strand1][l_strand2-1]):
            l_strand1-=1
        else:
            l_strand2-=1
    return longest_common_sequence,len(longest_common_sequence)

def find_LCS(strand_1,strand_2):
    lcs_table = initialize_table(strand_1,strand_2)
    populate_table(lcs_table,strand_1,strand_2)
    return backtrack_sequence(lcs_table,strand_1,strand_2)


lcs=find_LCS("ABCDGH","AEDFHR")
print("The longest common sequence is",lcs[0], "and has length", lcs[1],".")

