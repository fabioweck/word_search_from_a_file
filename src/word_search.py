# Write your solution here
def find_words(search_term: str):

    letters = "abcdefghijklmnopqrstuvwxyz"  #letters list
    index = 0                               #index of found special character
    type_of_search = ""                     #indicates to the loop which search will be performed



    if search_term.find('.') != (-1):       #search words with others characters
        index = search_term.find('.')
        type_of_search = "all"
    elif search_term.find('*') != (-1):    
        index = search_term.find('*')
        if index == 0:                      #search words starting with search term
            search_term = search_term[index+1:]
            type_of_search = "end"
        else:                               #search words ending with search term
            search_term = search_term[:index]
            type_of_search = "start"

    with open('words.txt') as word_list:

        for word in word_list:
            word = word.strip()
            if type_of_search == "start":
                if word.startswith(search_term):
                    print(word)
            elif type_of_search == "end":
                if word.endswith(search_term):
                    print(word)
            elif type_of_search == "all":
                for char in letters:  
                    search_term = search_term[:index] + char + search_term[index+1:]
                    if search_term == word:
                        print(word)
            else:
                if word == search_term:
                    print(word)
                        
while True:
    term = input("Type a word or type 'zzz' to exit:")
    find_words(term)
    if term == "zzz":
        break
