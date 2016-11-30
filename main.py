import os
import re
import string
from Trie import Trie
from P_Queue import PriorityQueue

###### Back Tarace ##################################################
#####################################################################

def BackTrace(i,j,S,back,Grammer,NT,tags,words):
    #print i," ",j," ",S
    file = open(Subdir+'output.txt', 'a')
    temp = back[i][j][DD(S,NT)]
    if(temp==[]):
        file.write("(")
        file.write(" ")
        file.write(S)
        file.write(" ")
        file.write("(")
        file.write(tags[j-1])
        file.write(" ")
        file.write(words[j-1])
        file.write(" )")
        return
    file.write("(")
    file.write(" ")
    #print S
    file.write(str(S))
    file.close()
    BackTrace(i,temp[0],NT[temp[1]],back,Grammer,NT,tags,words)
    file = open(Subdir+'output.txt', 'a')
    file.write(" ")
    file.close()
    BackTrace(temp[0],j,NT[temp[2]],back,Grammer,NT,tags,words)
    file = open(Subdir+'output.txt', 'a')
    file.write(")")
    file.close()

###### Key ##########################################################
#####################################################################

def DD(A,NT):
    for i in range(len(NT)):
        if(NT[i]==A):
            #print "key",i
            return i
    return -1

###### Grammer ######################################################
#####################################################################

Grammer = []
NT = []
def Gram():
    for subdir,dirs,files in os.walk('./'):
        for file in files:
            if(file=='cnf.txt'):
                with open(subdir+file) as grammer:
                    for line in grammer :
                        temp = []
                        this = line.split()
                        tag = True
                        for j in range(len(NT)):
                            #print this[0]
                            if(NT[j]==this[0]):
                                tag = False
                                break
                        if (tag == True):
                            NT.append(this[0])
                        for i in range(len(this)):
                            temp.append(this[i])
                        Grammer.append(this)
    print NT
    print Grammer
    return NT
###### CYK ##########################################################
#####################################################################
Subdir = ''
def CYK(line,tags,NT):
    #print "MIAAAY ???"
    #print line
    #print tags
    table = [[[0 for k in xrange(len(NT))] for j in xrange(len(line)+1)] for i in xrange(len(line)+1)]
    #print table
    back = [[[[] for k in xrange(len(NT))] for j in xrange(len(line)+1)] for i in xrange(len(line)+1)]

    ## initialazie
    #for j in range(1,len(line)+1):
    #    table[j-1][j][Key(tags[j-1],NT)] = 1

    for j in range(1,len(tags)+1):
        for rule in Grammer :
            if(len(rule)==3 and rule[2]==tags[j-1]):
                #print "OOOOOOOOOOOOO",rule[0],rule[2],tags[j-1]
                table[j-1][j][DD(rule[0],NT)] = 1

    #for i in range(len(back)):
    #    for j in range(len(back[i])):
    #        print table[i][j]
    
        X = j-2
        for i in range(0,j-1):
            for k in range((X-i)+1,j):
                for rule in Grammer:
                    if(len(rule)==4):
                        A = rule[0]
                        B = rule[2]
                        C = rule[3]
                        #p = float(rule[4])
                        #print table[X-i][k][DD(B,NT)],table[k][j][DD(C,NT)]
                        if(table[X-i][k][DD(B,NT)] == 1 ) and (table[k][j][DD(C,NT)] == 1):
                            #print "inja chi ?"
                            #if(table[X-i][j][DD(A,NT)] < 1*table[X-i][k][DD(B,NT)]*table[k][j][DD(C,NT)]):
                            table[X-i][j][DD(A,NT)] = 1*table[X-i][k][DD(B,NT)]*table[k][j][DD(C,NT)]
                            #print  [k,DD(B,NT),DD(C,NT)]
                            back[X-i][j][DD(A,NT)] = [k,DD(B,NT),DD(C,NT)]
                                                
            #print NT
                        #for i in range(len(table)):
                            #for j in range(len(table[0])):
                                #print table[i][j]
    #for i in range(len(back)):
    #    for j in range(len(back[i])):
    #        print table[i][j]
            
    #for i in range(len(back)):
    #    for j in range(len(back[i])):
    #        print back[i][j]
    for i in range(len(NT)):
        if(table[0][len(table)-1][DD(NT[i],NT)]==1):
            BackTrace(0,len(line),NT[i],back,Grammer,NT,tags,line)
            file = open(Subdir+'output.txt', 'a')
            file.write("\n")
            file.close()

##### Rec ###########################################################
#####################################################################
def Rec(words,tags,i,counter,NT):
    if(i==len(tags)):
        CYK(words,counter,NT)
    else:
        first = tags[i].split()
        for k in range(len(first)):
            counter[i] = first[k]
            Rec(words,tags,i+1,counter,NT)
            
###### Minimum Edit Distance ########################################
#####################################################################

def Min_Edit_Distance(word):
    Alphabet = ['«','»','Å',' ','À','Ã','ç','Õ','Œ','œ','–','—','“','é','”','‘','’','÷','ÿ','Ÿ','⁄','€','›','ﬁ','ò','ê','·','„','‰','Ê','Â','Ì']
    queue = PriorityQueue()
    #print word[0]
    Condidate = Lexi.startsWith(word[0])
    for i in range(len(Condidate)):
        print Condidate[i]
    #to check if size of condodate isnot enough
    if(len(Condidate)<3):
        for i in Alphabet:
            if i != word[0]:
                temp = []
                temp = Lexi.startsWith(i)
                for k in range(len(temp)):
                    Condidate.append(temp[k])
                
    ins_cost = 1
    sub_cost = 2
    del_cost = 1

    #print "***",Condidate
    
    for WORD in Condidate :
        distance = [[0 for k in xrange(len(word)+1)] for j in xrange(len(WORD)+1)]
        distance [0][0] = 0
        for i in range(1,len(WORD)+1):
            distance[i][0] = distance[i-1][0]+ ins_cost
        for j in range(1,len(word)+1):
            distance[0][j] = distance[0][j-1]+ del_cost
        for j in range(1,len(word)+1):
            for i in range(1,len(WORD)+1):
                if(word[j-1]!=WORD[i-1]):
                    distance[i][j] = min( distance[i-1][j] + ins_cost,distance[i-1][j-1] + sub_cost,distance[i][j-1] + del_cost )
                else:
                    distance[i][j]=distance[i-1][j-1]
        #print "@@",distance[len(WORD)][len(word)]                    
        queue.push(WORD,distance[len(WORD)][len(word)])
        #print queue
                   
    result = []
    
    for i in range(3):
        temp = queue.pop()
        result.append(temp)
    #print "==========",result
    return result
                
###### Parse ########################################################
#####################################################################

def Parser():
    NT = Gram()
    line = raw_input("=====:: PARSER ::==================\n Enter your sentence\n ::")
    #### Tokenizer
    punc = string.punctuation
    first_step =  line.replace('!',' !').replace('#',' #').\
                 replace('(','( ').replace(')',' )').replace('/',' / ').\
                 replace(':',' :').replace(';',' ;').replace('?',' ?').\
                 replace('@',' @').replace('[','[ ').replace(']',' ]').\
                 replace('\\',' \\ ').replace('.',' . ').replace('{','{ ').\
                 replace('}',' }').replace('|',' | ').replace('~',' ~ ').split()

    #### POS Tagger
    words = []
    tags = []
    
    temp_tag = ""
    for k in range(len(first_step)):
        print ":::",first_step[k]
        
    for i in range(len(first_step)):
        flag = False
        print "++",first_step[i],"tag =",temp_tag
        
        # khode kalame bashe tu lexicon
        temp_tag = Lexi.search(first_step[i])
        if (temp_tag!="-"):
            #print "##1"
            words.append(first_step[i])
            tags.append(temp_tag)
            flag = True
        elif(0<i):
            temp_tag = Lexi.search(first_step[i-1]+" "+first_step[i])
            if(temp_tag!="-"):
                #print "##2",first_step[i-1]+" "+first_step[i]
                words[len(words)-1] = first_step[i-1]+" "+first_step[i]
                tags[len(tags)-1] = temp_tag
                flag = True
            else:
                temp_tag = Lexi.search(first_step[i-1]+first_step[i])
                if(temp_tag!="-"):
                    #print "##3"
                    words[len(words)-1] = first_step[i-1]+first_step[i]
                    tags[len(tags)-1] = temp_tag
                    flag = True
                    
        if(not flag and i < len(first_step)-1):
            #print "miay inja ???"
            temp_tag = Lexi.search(first_step[i]+" "+first_step[i+1])
            if(temp_tag!="-"):
                #print "##4"
                words.append(first_step[i]+" "+first_step[i+1])
                tags.append(temp_tag)
                i = i+2
                flag = True
            else:
                temp_tag = Lexi.search(first_step[i]+first_step[i+1])
                if(temp_tag!="-"):
                    #print "##5"
                    words.append(first_step[i]+first_step[i+1])
                    tags.append(temp_tag)
                    i = i+2
                    flag = True
        elif(True):
            for j in range(len(first_step[i])-1):
                part1 = first_step[i][0:j]
                part2 = first_step[i][j+1:len(first_step[i])-1]
                if(Lexi.search(part1)!="-" and Lexi.search(part2)!="-"):
                    #print "##6"
                    words.append(part1)
                    words.append(part2)
                    tags.append(Lexi.search(part1))
                    tags.append(Lexi.search(part2))
                    flag = True
        if (not flag):
            #print "##7"
            LIST = Min_Edit_Distance(first_step[i])
            #print "+",LIST
            print ">> ",first_step[i]," :: Do you mean !?\n"
            for k in range(len(LIST)):
                print k,".",LIST[k]
            print len(LIST),". NOne of them"
            choose = raw_input("\n Please enter true number: ::")
            if int(choose) < len(LIST):
                words.append(LIST[int(choose)])
                tags.append(Lexi.search(LIST[int(choose)]))
            elif int(choose) == len(LIST):
                tag = raw_input(":: Add this word to lexcon ::\n inter tag of this word :")
                Lexi.insert(first_step[i],tag)
            else:
                print "invalid input"
            
    # represent POS tag
    if("Y"==raw_input(".:: Wana see tokenize step ?? ::.\n enter Y if you want\n\n ::")):
        print "Pos Taggs ::"
        for i in range(len(words)) :
            print words[i],tags[i]
    ##
            
    counter = []
    for i in range(len(words)):
        counter.append(0)
    Rec(words,tags,0,counter,NT)

    ##
    for subdirs,dirs,files in os.walk('./'):
        for file in files:
            if file == 'output.txt':
                with open(subdirs+file) as answer:
                    for line in answer:
                        print line
    return

###### Edit #########################################################
#####################################################################

def Edit():
    Key = int(raw_input(">> Edit ::\n 1.Grammer \n 2.Lexicon \n\n ::"))
    if(Key==1):
        print "HANU KAMEL NI"
        x = 0
        with open("BEFORE.txt") as infile:
            with open("AFTER.txt","w") as outfile:
                a = input("Do you want to update any rule in your grammer? 1 for yes and 0 for no:")
                if a == 1 :
                    print "which rule do you update in your grammer?"
                    x = input("Enter the number of line:")
                    print "Write the new rule:"
                    update = raw_input()
                elif a == 0 :
                    print "You don't want any updating in your grammer."
                b = input ("Do you want to delete any rule in your grammer? 1 for yes and 0 for no:")
                if b == 1:
                    print "which rule do you want to delete in your grammer?"
                    y = input("Enter the number of line:")

                elif b == 0:
                     print "You don't want any deletation in your grammer."

                c = input ("Do you want to insert a rule to your grammer? 1 for yes and 0 for no:")
                if c == 1:
                     print "Enter new rule:"                   
                     insert = raw_input()
                for i,line in enumerate(infile):    
                    if i == x-1:
                        outfile.write(update)
                        outfile.write("\n")
                    else:
                        outfile.write(line)

                if c == 1:
                         outfile.write("\n")
                         outfile.write(insert)

        ###########################3
    elif(Key==2):
        listt = []
        tags = []
        Alphabet = ['«','»','Å',' ','À','Ã','ç','Õ','Œ','œ','–','—','“','é','”','‘','’','÷','ÿ','Ÿ','⁄','€','›','ﬁ','ò','ê','·','„','‰','Ê','Â','Ì']
        for i in Alphabet:
            temp = []
            temp = Lexi.startsWith(i)
            for k in range(len(temp)):
                listt.append(temp[k])
                tags.append(Lexi.search(temp[k]))
        for i in range(len(listt)):
            print i," ",listt[i]," ",tags[i]
        Number = int(raw_input("\n Enter number of intry you want to edit\n ::"))
        print "\n ",Number," ",listt[Number]," ",tags[Number]
        action = int(raw_input("\n 1.Edit word\n 2.Edit tag\n 3.Insert\n 4.Del\n??\n ::"))
        if action == 1 :
            temp_word = listt[Number]
            temp_tag = tags[Number]
            Lexi.delet(temp_word)
            sub = raw_input("the correct form :: ")
            Lexi.insert(sub,temp_tag)
        elif action == 2 :
            temp_word = listt[Number]
            temp_tag = tags[Number]
            Lexi.delet(temp_word)
            print "::+",Lexi.search(temp_word)
            sub = raw_input("correct tag :: ")
            print ":::",temp_word,sub
            Lexi.insert(temp_word,sub)
        elif action == 3 :
            temp_word = raw_input("new word :: ")
            temp_tag = raw_input("tag :: ")
            Lexi.insert(temp_word,temp_tag)
        elif action == 4 :
            temp_word = listt[Number]
            Lexi.delet(temp_word)
        else :
            print "Invalid input"
        file1 = open(subdirs+"Lexicon.txt","w")
        for i in Alphabet :
            temp = Lexi.startsWith(i)
            for k in range(len(temp)):
                file1.write(temp[k])
                file1.write(" ")
                file1.write(Lexi.search(temp[k]))
                file1.write("\n")
    else:
        print "Invalid input"
    return

###### Show #########################################################
#####################################################################

def Show():
    flag = True
    while(flag):
        Key = int(raw_input(" 1.Represent Grammer\n 2.Represent Lexicon\n 3.Exit\n\n ::"))
        if Key == 1:
            for subdirs,dirs,files in os.walk('./'):
                for file in files:
                    if (file=='cnf.txt'):
                        with open (subdirs+file) as grammer:
                            for line in grammer:
                                print line
        
        elif Key == 2:
            for subdirs,dirs,files in os.walk('./'):
                for file in files:
                    if (file=='Lexicon.txt'):
                        with open (subdirs+file) as lexicon:
                            for line in lexicon:
                                print line
        elif Key ==3:
            flag = False
        else:
            print "Invalid input"
    return

###### Load Lexicon #################################################
#####################################################################

Lexi = Trie()
for subdirs,dirs,files in os.walk('./'):
    for file in files:
        if (file=='Lexicon.txt'):
            with open (subdirs+file) as lexicon:
                for LINE in lexicon:
                    word = []
                    tag = []
                    line = LINE.split()
                    for i in range(len(line)):
                        if(line[i][0]!='A' and line[i][0]!='B' and line[i][0]!='C' and line[i][0]!='D' and \
                           line[i][0]!='E' and line[i][0]!='F' and line[i][0]!='G' and line[i][0]!='H' and \
                           line[i][0]!='I' and line[i][0]!='J' and line[i][0]!='K' and line[i][0]!='L' and \
                           line[i][0]!='M' and line[i][0]!='N' and line[i][0]!='O' and line[i][0]!='P' and \
                           line[i][0]!='Q' and line[i][0]!='R' and line[i][0]!='S' and line[i][0]!='T' and \
                           line[i][0]!='U' and line[i][0]!='V' and line[i][0]!='W' and line[i][0]!='X' and \
                           line[i][0]!='Y' and line[i][0]!='Z' and line[i][0]!='a' and line[i][0]!='b' and \
                           line[i][0]!='c' and line[i][0]!='d' and line[i][0]!='e' and line[i][0]!='f' and \
                           line[i][0]!='g' and line[i][0]!='h' and line[i][0]!='i' and line[i][0]!='j' and \
                           line[i][0]!='k' and line[i][0]!='l' and line[i][0]!='m' and line[i][0]!='n' and \
                           line[i][0]!='o' and line[i][0]!='p' and line[i][0]!='q' and line[i][0]!='r' and \
                           line[i][0]!='s' and line[i][0]!='t' and line[i][0]!='u' and line[i][0]!='v' and \
                           line[i][0]!='w' and line[i][0]!='x' and line[i][0]!='y' and line[i][0]!='z' ):
                            word.append(line[i])
                        else:
                            tag.append(line[i])
                    temp_tag = ""
                    if len(tag) == 1 :
                        temp_tag = tag[0]
                    elif len(tag) == 2 :
                        temp_tag = tag[0]+" "+tag[1]
                    elif len(tag) == 3 :
                        temp_tag = tag[0]+" "+tag[1]+" "+tag[2]
                    elif len(tag) == 4 :
                        temp_tag = tag[0]+" "+tag[1]+" "+tag[2]+" "+tag[3]
                    elif len(tag) == 5 :
                        temp_tag = tag[0]+" "+tag[1]+" "+tag[2]+" "+tag[3]+" "+tag[4]
                    elif len(tag) == 6 :
                        temp_tag = tag[0]+" "+tag[1]+" "+tag[2]+" "+tag[3]+" "+tag[4]+" "+tag[5]
                        
                    if(len(word)==1):
                        Lexi.insert(word[0],temp_tag)
                    elif(len(word)==2):
                        Lexi.insert(word[0]+" "+word[1],temp_tag)
                    elif(len(word)==3):
                        Lexi.insert(word[0]+" "+word[1]+" "+word[2],temp_tag)
                    
###### Main Menu ####################################################
#####################################################################

Exit = False                    
while(not Exit):
    Key = raw_input("=====:: Main Menu ::===============\n\n 1.Parse\n 2.Edit Gammer Or Lexicon\n 3.Represent Data Or Grammer\n 4.Exit\n\n :: ")
    if(int(Key)==1):
        print "==================================="
        Parser()
        print "==================================="
    elif(int(Key)==2):
        print "==================================="
        Edit()
        print "==================================="
    elif(int(Key)==3):
        print "==================================="
        Show()
        print "==================================="
    elif(int(Key)==4):
        print "==================================="
        Exit = True
        print "==================================="
    else:
        print "Invalid Input"
        
#####################################################################
#####################################################################
