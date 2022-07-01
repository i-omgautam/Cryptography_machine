#!C:\Users\omgau\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9

def cryptomachine():
    # keys ~ Contains almost all the possible symbols generall used in messaging/conversing.
    keys = 'a@b#c$d9e^f&g*h(i)j_k-l?7m|n\o:p;q{r/s8t[u2v]w1!3x,.6y4~5 %'
    # values ~ Contains incremented list of values in keys to create a key that encrypts/decrypts the message into.
    values = keys[-1] + keys[0:-1]

    # encryptDict ~ Is a dictionary that stores almost all the key-value pair of keys & values for encryption
    encryptDict = dict(zip(keys, values))
    # decryptDict ~ Is a dictionary that stores almost all the value-key pair of keys & values for decryption
    decryptDict = dict(zip(values, keys))

    message = input("Plaese enter your secret message:\n")
    mode = input("Please enter the mode:\nE(Encode)/D(Decode)\n")

    if (mode.upper() == 'E'or mode.upper() == 'e'):
        newMessage1 = ''.join(
            [encryptDict[lttr] for lttr in message.lower()])  # Encrypting once
        newMessage = ''.join([encryptDict[nM1] for nM1 in newMessage1.lower()])
        
        # Encrypting twice
    elif (mode.upper() == 'D'or mode.upper() == 'd'):
        newMessage1 = ''.join(
            [decryptDict[lttr] for lttr in message.lower()])  # Decrypting once
        newMessage = ''.join([decryptDict[nM1] for nM1 in newMessage1.lower()
                              ])  # Decrypting twice
    else:
        # If the values in input is not matching with the keys
        print("please enter a correct choice!")

    return newMessage


if __name__ == "__main__":
    
    machine = cryptomachine();
    print(machine)