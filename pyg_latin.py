import time
print ("This is a pig latin calculator!")
time.sleep(1)

try:
    while True:
        word = input("What word should I convert to pig latin? ")

        if word[0] not in ('a', 'e', 'i', 'o', 'u'):
            first = 0
        elif word[1] not in ('a', 'e', 'i', 'o', 'u'):
            first = 1
        elif word[2] not in ('a', 'e', 'i', 'o', 'u'):
            first = 2
        else:
            print('There are way too many vowels in that word')
            first = 'error'

        cut_word = word[(first + 1):len(word)]
        moved_letter = word[first]

        pyg_word = cut_word + moved_letter + "ay"

        print (pyg_word)

except KeyboardInterrupt:
    pass
        

