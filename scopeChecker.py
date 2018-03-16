def isOpener(chara, openers):
    return (chara in openers)

def isCloser(chara, closers):
    return(chara in closers)
        



def scopeCheck(scopeSequence, scopeMatch):
    s = []

    for x,chara in enumerate(scopeSequence):
        print(chara)
        if isOpener(chara, scopeMatch.values()):
            print(chara, "was appended")
            s.append(chara)
        
        if isCloser(chara, scopeMatch.keys()):
            if s == []:
                print("got to closer but empty stack")
                return False

            else:
                if s[-1] == scopeMatch[chara]:
                    print("popped because", chara, "is paired to the top:", s[-1])
                    s.pop()
                    if s == [] and x == (len(scopeSequence)-1):
                        return True
                    else:
                        continue

                else:
                    print("failed because", chara, "is not equal to the top:", s[-1])

                    return False
    if s != []:
        print("failed because something left on the stack")
        return False


def main():
    scopeMatch = { ')':'(', ']':'[', '}':'{' } 
    scopeSeqs = ["{()[]}", "{([)]}", "{[()][]}", "{}]", "[{}"]

    for seq in scopeSeqs:
        print(seq, scopeCheck(seq, scopeMatch))







if __name__ == '__main__':
    main()


