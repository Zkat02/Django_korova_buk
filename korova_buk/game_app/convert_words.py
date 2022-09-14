rez_file = open('file_with_words.txt','w',encoding='utf-8')

with open('../слова.txt', 'r',encoding='utf-8') as words:
    for word in words:

        word = word.split('. ')[1][:-1:]
        rez_file.write(f"('{word}'),\n")



