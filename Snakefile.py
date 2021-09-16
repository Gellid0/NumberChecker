

def checker(word):
    whitelist = [1,2,3,4,5,6,7,8,9,0]
    n = 0

    for l in word:
        
        for p in whitelist:
            #print(str(l) + " " + str(p))

            if str(l) == str(p):
                n += 1
            
                
                    
    if n == len(word):
        print("\n " + str(word) + " é válido \n")
        return True

    else:
        print("\n " + str(word) + " é inválido \n")
        return False     
        
palavra = input(str("\n qual a palavra? \n"))
checker(palavra)