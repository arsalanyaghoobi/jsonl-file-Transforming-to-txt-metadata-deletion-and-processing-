import pip
import nltk
import jsonlines
import string
import os # for opening,reading and processing data


base_directory = "D:\Pycharm Folder\pythonProject3\data"
files=os.listdir(base_directory)
print(files)
Result = open("result.txt","w+")
for items in files:
    with jsonlines.open(os.path.join(base_directory,items)) as f :
        for line in f:
            Result.write(line.get('context'))
            if line.get('text'):
                Result.write(line.get('text'))
            Result.write('\n')
            #print(line)

from nltk.tokenize import word_tokenize
text = open('result.txt','r')
text = text.read()
#print(text)
words = word_tokenize(text)
numb_words = len(words)
print('number of words in the dataset is ', numb_words)
words_set=set(words)
numb_set_words=len(words_set)
print('number of words of our set is ' , numb_set_words)
print(words_set)
set = open('words_set.txt','w+')
punctuation = string.punctuation
print(punctuation)
for items in words_set:
    if items in punctuation:
        set.write('')
    else:
        set.write(items)
        set.write('\n')



















# Helpful Link = "https://www.w3schools.com/python/python_json.asp"
#1)Note that dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to
# which the bytes will be written.
#2)Turning python into json use "json.dump(data, write_file)"
#3)Turning json file into python use "json.load(s)"
#4) Encoding and Decoding to and fro json doesnt represent us with a same code.
