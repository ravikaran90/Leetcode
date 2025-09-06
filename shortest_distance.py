class Solution:
    def shortest_distance(self,wordsDict,word1,word2):
        diction={}
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                if word1 not in diction:
                    diction[word1]=i
                elif word1 in diction and word2 not in diction:
                    diction[word1]=i
                elif word1 in diction and abs(i-diction[word2])<abs(diction[word1]-diction[word2]):
                    diction[word1]=i
            elif wordsDict[i]==word2:
                if word2 not in diction:
                    diction[word2]=i
                elif word2 in diction and word1 not in diction:
                    diction[word2]=i
                elif word2 in diction and abs(i-diction[word1])<abs(diction[word1]-diction[word2]):
                    diction[word2]=i
        print(diction)
        return min(abs(diction[word1]-diction[word2]),abs(diction[word2]-diction[word1]))
       
                #print(diction[wordsDict[i]])
                    #print("Diction[i]:",i)
                    #print("First:",abs(i-diction[word2]))
                    #print("Second:",abs(diction[word1]-diction[word2]))
                    #print("Execute")     
                #print(wordsDict[i])
                #if word1 in diction and word2 in diction:
                #    short_dist=min(abs(diction[word1]-diction[word2]),abs(diction[word1]-diction[wordsDict[i]]))
                #    print(short_dist)
                
                    #print("Execute2")
                    
            #elif word2 not in diction:
            #        diction[word2]=i
                #elif wordsDict[i]==word2:
            #    elif word2 in diction and short_dist>abs(diction[word2]-diction[word1]):
            #        diction[word2]=i
            #    short_dist=min(abs(diction[word1]-diction[word2]),abs(diction[word2]-diction[word1]))
                    
            #if word1 in diction and word2 in diction:
        #print(diction)
        #return min(abs(diction[word1]-diction[word2]),abs(diction[word2]-diction[word1]))
        #short_dist=min(abs(diction[word1]-diction[word2]),abs(diction[word2]-diction[word1]))
        #return short_dist #min(abs(diction[word1]-diction[word2]),abs(diction[word2]-diction[word1]))
        #return listing[-1]-listing[-2]

def main():
    #wordsDict=["practice", "makes", "perfect", "coding", "makes"]
    #word1="makes"
    #word2="coding"
    #wordsDict=["practice","makes","perfect","coding","makes"]
    #word1="coding"
    #word2="practice"
    wordsDict=["a","c","b","b","a"]
    word1="a"
    word2="b"
    obj=Solution()
    dist=obj.shortest_distance(wordsDict,word1,word2)
    print("Shortest Distance:",dist)

if __name__=="__main__":
    main()







#Through Lists

#listing.append(word1)
                #listing[i]=word1
                #listing[i]=word1
                #if word2 in listing:
                #    listing[i]=word2
                #else:
                #    listing.append(word2)