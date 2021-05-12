def SimilarityIndexGenome(strandA,strandB):
    score = 0
    dissimilarity_indices=[]
    for i in range(len(strandA)):
        if(strandA[i]==strandB[i]):
            score+=1
        else:
            score-=1
            dissimilarity_indices.append(i)
    print(f"Dissimilar Indices: {dissimilarity_indices}")
    return score/len(strandA)*100

similarity = SimilarityIndexGenome("ATATGTATG","ATATATATG")
print(f"Similarity Index Genome: {similarity}")

# Questions: Can we find the positions of characters that do not match using this function?
#            Yes, we can check the index of the strand where the score is being deducted. The very reason for deduction is the dissimilarity of the value at that index, so we keep the note of indices where the characters do not match.