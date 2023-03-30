
###Q1




def my_func(x1,x2,x3):


    if isinstance(x1, str) or isinstance(x1, str) or isinstance(x3, str):
        print("None")

      
        
    elif isinstance(x1, float) and isinstance(x1, float) and isinstance(x3, float):
        

        mehane= x1+x2+x3
        moneA=x2+x3
        return ((mehane*moneA*x3)/mehane)
          

        


    else:

        print('Error: parameters should be float')


###Q2

def revword(wordre):
       
    correct=''
    length_of_wordre=len(wordre)

    for letter in range(length_of_wordre-1,-1,-1):
        
        correct=correct+wordre[letter]
        

    return correct    


def countword():

    file_name=input("Enter file name")
    fn=open(file_name,'r')
    first_line=fn.readline()
    word=first_line.split()[0].upper()
    
    
    mylist=[]
    count=0
    for line in fn:
        words=line.split()

        for one_word in words:
            a=revword(one_word)
            a=a.upper()
            mylist.append(a)
            
            
    for i in mylist:
        if i==word:
            count+=1

    return count+1















