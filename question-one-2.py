orgKey =    '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
cipherKey = 'Cn9mcLX6U`v41(g\D8z~a<>:k"!S3GMf7d$%u{T?I#Osot|ry5]FN@2;BKe*[}Ww0.A,+-hPqHRZjVY=Jx)_lQb^/\'pE&i'

encryptDict = {} # Empty dictionary to build dictionary of encryption pairs 
for idx in range(len(orgKey)): # for every character in key create a pair for the dict
    encryptDict[cipherKey[idx]] = orgKey[idx]

fileHandler = open('some_encrypted.txt') # open a file into 
encryptedLines = fileHandler.readlines() # list encryptedLines 

countDict = {} # Create an empty dictionary to count all the characters in the encrypted message
decodedMessage = [] # Create a list to build the decoded message 
for line in encryptedLines: # for every char 
    for char in line: 
        if char not in ['\n', ' ']: # if character is not a space or newline 
            decodedMessage.append(encryptDict[char]) # throw the unencrypted version in decodedMessage
            if char not in countDict: # if the character is not yet in the dict, declare it
                countDict[char] = 1 
            else: # otherwise increment the value 
                countDict[char] += 1
        else: 
            decodedMessage.append(char) # otherwise just append the newline / space 

decodedMessage = ''.join(decodedMessage)
mostCommonChar = max(countDict, key=countDict.get)

print(decodedMessage) # output the decoded message joined into one string 

print("Most Frequently Used Character: ") # Output mostCommonChar etc
print("Encrypted:", mostCommonChar)
print("Decrypted:", encryptDict[mostCommonChar]) 

