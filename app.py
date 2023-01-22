# omer khan 391007603
# sultan fahad 391002603

# use py 3.10 or higher


from grammer import * 

token = []
result = []

f = open("test.txt","r") # put file name here
scanner = f.read()
parser = scanner.split()

for t in parser:
    if t in verb:
        token.append("verb")
    elif t in adjective:
        token.append("adjective")
    elif t in objects:
        token.append("objects")
    elif t in noun:
        token.append("noun")
    else:
        token.append("notD")   

for i in range(len(token)):
    match token[i]:
        case "verb":
            # <verb sentence> 
            match token[i+1]:
                case "adjective":
                    if (i+2 <= len(token)-1):
                        match token[i+2]:
                            case "objects":
                                # <object> <adjective> <verb>
                                result.append(parser[i]+FATHA)
                                result.append(parser[i+1]+DAMMA)
                                result.append(parser[i+2]+FATHA)
                                result.append("\n")
                            case defult:
                                result.append(parser[i]+FATHA)
                                result.append(parser[i+1]+DAMMA)
                                result.append("\n")                                    
                    else:
                        # <adjective> <verb>
                        result.append(parser[i]+FATHA)
                        result.append(parser[i+1]+DAMMA)
                        result.append("\n")
        case "adjective":
            # <noun sentence>
            if (i+1 <= len(token)-1):
                match token[i+1]:
                    case "noun":
                        result.append(parser[i]+DAMMA)
                        result.append(parser[i+1]+DAMMATAN)
                        result.append("\n")                
        case "objects":
            # <noun sentence>
            if (i+1 <= len(token)-1):
                match token[i+1]:
                    case "noun":
                        result.append(parser[i]+DAMMA)
                        result.append(parser[i+1]+DAMMATAN)
                        result.append("\n") 

# =====================================================================================
# ======================== OUTPUT ===================================================== 
# =====================================================================================

r = " "
print("parser: {}".format(parser))
print("tokens: {}".format(token))            
print("result: \n  {}".format(r.join(result)))



# =====================================================================================
# ======================== TODO ===================================================== 
# =====================================================================================


# TODO counter
# token = {
#     "verb":"",
#     "adjective":"",
#     "objects":"",
#     "noun":"",
# }