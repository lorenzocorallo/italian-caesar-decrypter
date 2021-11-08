from random import randint
class Match:
    def __init__(self, key, phrase):
        self.phrase = phrase
        self.key = key

    def log(self):
        print(f"\nKey:  {self.key}")
        print("Decrypted Phrase:")
        print(self.phrase)

def sort_by_string_length(arr, reverse=False):
    for x in arr:
        i = arr.index(x)
        temp = x
 
        # Insert arr[j] at its correct position
        j = i - 1
        while j >= 0 and len(temp) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
 
        arr[j + 1] = temp
    if reverse:
        arr.reverse()
 

def decrypt(key, crypted_phrase):
    key = int(key)
    decrypter = []

    # Sposto l'alfabeto indietro di "key"
    for i in range(key, len(alfabeto)):
        decrypter.append(alfabeto[i])

    for i in range(0, key):
        decrypter.append(alfabeto[i])

    # decrypto in base all'alfabeto decrypter
    decrypted = ""
    for char in crypted_phrase:
        if char == " ":
            decrypted += " "
        elif char in numbers:
            decrypted += char
        else:
            decrypted_letter = alfabeto[decrypter.index(char.upper())]
            if char.islower():
                decrypted += decrypted_letter.lower()
            else:
                decrypted += decrypted_letter

    return decrypted

def bruteforce(crypted_phrase):
    splitted = crypted_phrase.split(" ")
    words = []
    for x in splitted:
        if len(x) > 1 and not x in numbers:
            words.append(x)
    if len(words) == 0:
        print("Inserisci almeno una parola da due lettere")
        return
    
    sort_by_string_length(words, True) # order by word length
    matches = []
    i = 0

    while i < len(words) and len(matches) != 1:
        if not matches:
            word = words[i]
            for j in range(0, len(alfabeto)):
                dw = decrypt(j, word)    
                if dw.lower() in ITALIAN_WORDS: # time complexity O(n) n = len(ITALIAN_WORDS)
                    matches.append(j)
        else:
            prev_matches = matches.copy()
            matches = []
            word = words[i]
            for j in prev_matches:
                dw = decrypt(j, word)    
                if dw.lower() in ITALIAN_WORDS: # time complexity O(n) n = len(ITALIAN_WORDS)
                    matches.append(j)
        i += 1

    if matches:
        valids = []
        for key in matches:
           match = Match(key, decrypt(key, crypted_phrase)) 
           valids.append(match)
        return valids
    else: 
        return False





def statistics_sorter(el):
    return el.count
                
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5','6','7','8','9', '0']
ITALIAN_WORDS = []

#####################
# Execution
#####################


try:
    file = open("./bruteforce/italian.txt", "r")
    print("Caricando il dizionario...")
    words = file.readlines()
    for word in words: ITALIAN_WORDS.append(word.replace("\n", "").strip())
except FileNotFoundError:
    print('Please provide a file with italian words named "italian.txt" and place it in the bruteforce folder in the project directory')

crypted = input("Inserisci la stringa criptata [Cesare - Alfabeto completo]\n")

print("\nBruteforce:")


valids = bruteforce(crypted)
if valids:
    for valid in valids:
        valid.log()
else:
    print("Bruteforce fallito")
print("\n")



