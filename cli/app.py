# -*- coding: utf-8 -*-

# omer khan 391007603
# sultan fahad 391002603

# use py 3.10 or higher

import os
import sys
from grammer import * 


def shkl(text):
    token = []
    result = []
    parser = text.split()
    for t in parser:
        if t in verb:
            token.append("verb")
        elif t in name_human:
            token.append("name_human")
        elif t in name_object:
            token.append("name_object")
        elif t in noun:
            token.append("noun")
        else:
            token.append("notD")  
    for i in range(len(token)):
        match token[i]:
            case "verb":
                # <verb sentence> 
                match token[i+1]:
                    case "name_human":
                        if (i+2 <= len(token)-1):
                            match token[i+2]:
                                case "name_object":
                                    # <object> <name_human> <verb>
                                    result.append(parser[i]+FATHA)
                                    result.append(parser[i+1]+DAMMA)
                                    result.append(parser[i+2]+FATHA)
                                    result.append("\n")
                                case defult:
                                    result.append(parser[i]+FATHA)
                                    result.append(parser[i+1]+DAMMA)
                                    result.append("\n")                                    
                        else:
                            # <name_human> <verb>
                            result.append(parser[i]+FATHA)
                            result.append(parser[i+1]+DAMMA)
                            result.append("\n")
                    case "name_object":
                        if (i+2 <= len(token)-1):
                            match token[i+2]:
                                case "name_human":
                                    # <object> <name_human> <verb>
                                    result.append(parser[i]+FATHA)
                                    result.append(parser[i+1]+DAMMA)
                                    result.append(parser[i+2]+FATHA)
                                    result.append("\n")
                                case defult:
                                    result.append(parser[i]+FATHA)
                                    result.append(parser[i+1]+DAMMA)
                                    result.append("\n")                                    
                        else:
                            # <name_object> <verb>
                            result.append(parser[i]+FATHA)
                            result.append(parser[i+1]+DAMMA)
                            result.append("\n")
                    case defult:
                        result.append(parser[i])
                        result.append(parser[i+1])
                        result.append("تركيب خاطئ")
                        result.append("\n")
            case "name_human":
                # <noun sentence>
                if (i+1 <= len(token)-1):
                    match token[i+1]:
                        case "noun":
                            result.append(parser[i]+DAMMA)
                            result.append(parser[i+1]+DAMMATAN)
                            result.append("\n")  
            case "name_object":
                # <noun sentence>
                if (i+1 <= len(token)-1):
                    match token[i+1]:
                        case "noun":
                            result.append(parser[i]+DAMMA)
                            result.append(parser[i+1]+DAMMATAN)
                            result.append("\n")   
            case defult:
                result.append("تركيب خاطئ")
                result.append("\n")
                
    return parser,token,result    



loop = True
while loop == True:
    print("ادخال نص عن طريق")
    print("(1) ملف نصي")
    print("(2) ادخال النص")
    inM = input("ادخل رقم الخيار \n")

    match inM:
        case "1":
            try:
                if len(sys.argv) > 1:
                    f = open(sys.argv[1], 'r')
                    scanner = f.read()
                    parser,token,result = shkl(scanner)
                else:                
                    f = open("test.txt","r") # put file name here
                    scanner = f.read()
                    parser,token,result = shkl(scanner)    
            except Exception as ex:
                print(ex)   
        case "2":
            inT = input("اكتب النص المراد تشكيله \n")    
            parser,token,result = shkl(inT)

    print("حفظ النص المشكل لملف؟")
    print("(1) نعم")
    print("(2) لا")
    inO = input("ادخل رقم الخيار \n")

    match inO:
        case "1":
            try:
                output_dir = "output_directory"
                with open(os.path.join(output_dir, "mshkl_text.txt"), "w") as fout:
                    r = " "
                    fout.write(r.join(result))
                    print("تم حفظ النص في ")
                    print(os.path.abspath(os.path.join(output_dir, "mshkl_text.txt")))
            except Exception as ex:
                print(ex)
        case "2":
            r = " "
            print("parser: {}".format(parser))
            print("tokens: {}".format(token))            
            print("result: \n  {}".format(r.join(result)))

    print("تشكيل نص اخر؟")
    print("(1) نعم")
    print("(2) لا")
    inL = input("ادخل رقم الخيار \n")
    if inL == "2":
        loop = False
                    
