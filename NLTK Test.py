import nltk
import numpy as np
# NOTE: had to use ndarrays for this project.  Organic Python lists were orders of magnitude slower when processing full text of corpora
import pickle

# Creates char arrays for Herman Melville's Moby Dick
# Creates (2) char arrays.  
# alph27arr includes alpha characters and space - all numeric and punctuation characters stripped
# alph26arr includes alpha characters only

ALPH26 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPH27 = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPH26ARR = np.array(list(ALPH26))
ALPH27ARR = np.array(list(ALPH27))
ALPH26FILE = 'alph26.txt'
ALPH27FILE = 'alph27.txt'

print("")
print("")
print("*********************START*********************")

def StrArrayToStr(strarr=np.empty(0)):
    #This function is not efficient needs to be rewritten to use Numpy efficiencies
    newstring = ""
    for i in range(len(strarr)):
        newstring = newstring + strarr[i]
    return newstring

def HStrArray(hstrarr, N=1):
    #calculates expected information for a sequence
    #Expects array of strings length 1 (i.e. char array)
    
    #init information events
    events= np.empty(0)     

    #get all events of length N (starting at 0, 1, 2, ... Total Length - N)            
    print(len(hstrarr))
    for i in range(len(hstrarr)-N):
        if i % 1000 == 0 : print(i)
        events = np.append(events, StrArrayToStr(hstrarr[i:i+N]))

    #get unique events and counts of occurrence
    unique, counts = np.unique(events, return_counts=True)
    print("DEBUG HStrArray Unique Counts ", dict(zip(unique, counts)))

    #calculate frequency distribution of all events
    dist = counts / len(hstrarr )
    #print (dist)
    
    #return Execpected Information
    return -sum(dist * np.log2(dist))




def MakeCharArrays(corpus):

    # Get raw text of Moby Dick
    if corpus == 'brown':
        raw = nltk.corpus.brown.raw()
    elif corpus == 'melville':
        raw = nltk.corpus.gutenberg.raw("melville-moby_dick.txt")
    elif corpus == 'gutenberg':
        raw = nltk.corpus.gutenberg.raw()
    else:
        return False

    # Convert raw text string to Numpy ndarray
    chararr = np.array(list((raw)))

    # Create boolean mask for alphabet + space characters in character array
    mask = np.isin(chararr, ALPH27ARR)
    
    # Remove non-alphabet / space characters
    nospecial = chararr[mask]

    # Write adjusted text to disk as char array
    with open(corpus + ALPH27FILE, 'wb') as filehandle:  
        pickle.dump(nospecial, filehandle)

    # Create boolean mask for alphabet characters in character array
    mask = np.isin(nospecial, ALPH26ARR)

    #Remove non-alphabet charcters
    nospace = nospecial[mask]

    # Write adjusted text to disk as char array
    with open(corpus + ALPH26FILE, 'wb') as filehandle:  
        pickle.dump(nospace, filehandle)
 
    # Code to read alph2Xfile
    # with open(alph27file, 'rb') as filehandle:  
    #     newlist = pickle.load(filehandle)
    
    return True

#MakeCharArrays('brown')

# raw = nltk.corpus.brown

# Code to read alph2Xfile
with open('melville' + ALPH26FILE, 'rb') as filehandle:  
   newlist = pickle.load(filehandle)




#print(newlist.tostring())
mylist = newlist[:20]
print (HStrArray(newlist, 3))

print("Done")


