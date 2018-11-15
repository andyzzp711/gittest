##key words
key_world_list =["while","if","else","mcswitch","vobc","testcase","setval","int","getval","atetrain","ci",   "zc","check","route","signal","switch"   ,"addcar","arcmd","keyactive","dirhandle","speed"   ,"trainmode","doormode","masterhandle","atostart"  ]
key_translate_list =["t","w","u","r","z","y","s","x","g","e","l"   ,"a","d","c","b","k"   ,"f","h","i","j","m"  ,"n","o","q","p"]
##identifiers
flag_world_list=[chr(i) for i in range(97,99)]  #add a-c
## constant
constant_world_list = [chr(i) for i in range(48,57)]  #add 0-9
##operators
operator_world_list = ["+","-","*","/","=",">","<","==","!="]
##delimiters
delimiter_world_list = [";","{","}","(",")"]
##str list after lexical analysis
procedure_str_list =[]
##String style required for syntax analysis
procedure_str =""
 
##judge space or "\t"
def is_difference(world):
    if (world ==" ") or (world=="\t"):
        return True
    return False
    
##judge letter
def is_letter(letter):
    if (ord(letter)>96) and (ord(letter)<123):
        return True
    return False
    
#lexical analysis
def lex_word():
    for line in open("andytest.case"):
        step=0    
        flag=0   #specils deal with identifiers
        tmp=""    #temp var

        for single in line:
            if flag ==1:   #str identification
                tmp +=single
                flag =0
                step +=1
                continue
            elif flag ==2:
                tmp +=single
                procedure_str_list.append(tmp)
                flag=0
                tmp =""
                step +=1
                continue
            if single =="\n":        #analyse next sentance when touth "enter" key
                break
            elif is_difference(single)==False: #judge space or "/t"
                ##deal with letter
                if is_letter(single):    
                    tmp += single   #current letter to tmp
                    if is_letter(line[step+1]):  #find previous letter and check 
                        flag =1
                        step +=1
                        continue
                    else:
                        procedure_str_list.append(tmp) #previous isn't letter, stop check.  set " " to tmp
                        tmp=""
                        step +=1
                ##deal with not letter
                else:                       
                    if tmp!="":
                        procedure_str_list.append(tmp)
                        tmp =""
                    if single in delimiter_world_list:  #deal with delimiter
                        procedure_str_list.append(single)
                        step +=1
                    elif single in constant_world_list:   #deal with constant
                        step +=1
                        procedure_str_list.append(single)
                    elif single in operator_world_list:  #deal with operator
                        if line[step+1] == "=":    #deal with   ==
                            flag =2  #==,identifiers
                            tmp +=single
                            step +=1
                        else:
                             procedure_str_list.append(single)
                             step +=1
            else: 
                if tmp !="": 
                    procedure_str_list.append(tmp)
                    tmp =""
                step +=1
                
    ##result show after lexical analysis
    print(procedure_str_list)
    print("*"*50+"\n"+"lexical analysis result:  "+"\n")
    print("char".center(10)+"property".center(10))
    for single in procedure_str_list:
        if single in key_world_list:
            print(single.center(10)+"keywords".center(10))
        elif single in flag_world_list:
            print(single.center(10)+"identifiers".center(10))
        elif single in constant_world_list:
            print(single.center(10)+"constant".center(10))
        elif single in operator_world_list:
            print(single.center(10)+"operators".center(10))
        elif single in delimiter_world_list:
            print(single.center(10)+"delimiters".center(10))
    print("*"*50)

    ##Character into syntax analysis required style
    procedure_str =""
    for single in procedure_str_list:
        if single in key_world_list:
            procedure_str += key_translate_list[key_world_list.index(single)]   #according to index to translating
        else:
            procedure_str +=single
    procedure_str +="#"
    print("*"*50+"\n"+"String after program translating" +"\n"+procedure_str+"\n"+"*"*50)
    return procedure_str


