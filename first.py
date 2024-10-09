# hours = input("Enter hours: ")
# rate = input("Enter rate: ")
# pay = float(hours) * float(rate)

# print(pay)
    
# --------------------
# Compute Overall Pay

# hrs = input("Enter Hours: ")
# h = float(hrs)
# rate = input("Enter rate: ")
# r = float(rate)


# def computepay():
#     c = h * r
#     if h <= 40:
#         return c
#     else:
#         d = float((40 * r) + ((h - 40) * (r * 1.5)))
#         return d

# p = computepay()

# print("Pay", p)

# ----------------------


# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done' :
#         break
#     print(line)
# print('Done!')

# ------------------------Blast Off!---------------------------

# name = input("Enter Name: ")

# import time
# def countDown():
#     for i in ["Hello!", "My name is " + name + "!", "I will be your guide today!", "Please fasten your seatbelts and prepare for lift-off.", "Here we go!",]:
#         print(i)
#         time.sleep(2.5)
#     for k in [5, 4, 3, 2, 1]:
#         print(k)
#         time.sleep(1)

# countDown()
# print("Blast off!")

# ------------------Find the Largest Number------------------

# largest_so_far = None

# for the_num in [9, 41, 12, 3, 74, 15]:
#     if largest_so_far is None :
#         largest_so_far = the_num
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)

# smallest_so_far = None
# while True :
#     num = input("Enter Number: ")
# print('After', largest_so_far)


# --------------------Counting in Loops------------------------

# vc = 0
# print('Before', vc)
# for this in [9, 41, 12, 3, 74, 15]:
#     vc = vc + 1
#     print(vc, this)
# print('After', vc)


# total = 0
# print('Before', total)
# for number in [9, 41, 12, 3, 74, 15]:
#     total = number + total
#     print(total, number)

# print('After', total)


# ---------------------Finding The Average---------------------

# num = 0
# total = 0.0
# while True:
#     sval = input('Enter a number: ')
#     if sval == 'done':
#         break
#     try:
#         ifval = float(sval)
#     except:
#             print('Invalid input')
#             continue
#     print(ifval)
#     num = num + 1
#     total = total + ifval

# print('All done!')
# print(total, num, total/num)

# ------------Finding the Largest AND Smallest------------

# smallest_so_far = None
# largest_so_far = None
# while True :
#     num = input("Enter number: ")
#     if num == 'done':
#         break
#     if smallest_so_far is None and largest_so_far is None :
#         smallest_so_far = num
#         largest_so_far = num
#         continue
#     try:
#         ifval = float(num)
#         largest = float(largest_so_far)
#         smallest = float(smallest_so_far)
#     except:
#         print("Invalid input")
#         continue
#     if ifval > largest :
#         largest = num
#         print("L" + largest, num)
#         continue
#     elif ifval < smallest :
#         smallest = num
#         print("S" + smallest, num)
#         continue


# print('Maximum is ' + str(largest), 'Minimum is ' + str(smallest))


# -----------------------Find the Smallest/Largest inputted-------------------------


# largest = None
# smallest = None

# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         num = int(num)
#     except:
#         print("Invalid Input")
#         continue

#     if largest is None:
#         largest = num
#     elif num > largest:
#         largest = num
    
#     if smallest is None:
#         smallest = num
#     elif num < smallest:
#         smallest = num
    
# print("Maximum is ", largest)
# print("Minimum is ", smallest)

# ----------------------BANANA--------------------

# fruit = 'avocados are a legendary \nfruit'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1



# greet = 'hello chris'
# zap = greet.capitalize()
# print(zap)



# text = "X-DSPAM-Confidence:    0.8475"
# score = text.find('0.8475')
# print(float(text[23:]))




# fname = input('Enter file name: ')
# try:
#     fhand = open(fname)
# except:
#         print('File cannot be opened:', fname)
#         quit()
# for line in fhand:
#     if line.startswith('Subject'):
#         print('There were', 'subject lines in', fname.rstrip())



# fhand = input('Enter File:  ')
# fh = open(fhand)
# fy = fh.read()
# for lx in fy:
#     ly = lx.rstrip()
#     continue
#     # Skip 'uninteresting lines'
#     # if not lx.startswith('From:'):
#     #     continue
#     # Process our 'interesting' line

# print(fy.upper())

# ---------------------Slicing-------------------------
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2, 4)
# print(a[x])

# --------------------Slicing Files---------------------

# Use the file name mbox-short.txt as the file name
# fname = input('Enter file name: ')
# fhand = open(fname)
# count = 0
# num = 0.0
# for line in fhand:
#     if not line.startswith('X-DSPAM-Confidence:'):
#         continue
#     else:
#         count=count+1
#         lineStrip = line.rstrip()
#         position = lineStrip.find(':')
#         number=float(lineStrip[position+1:])
#         num=float(number+num)
# avg=float(num/count)
# print('Average spam confidence:', avg)




# s = 'Monty Python: 23'
# p = s.split(': ')

# x = ['Joe', 'Chris', 'Tony', 'Sam']
# for i in range(len(x)):
#     z = x[i]
#     print(z)



# ///////////////////////////////////////////////////

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])


# ///////////////////SUCCESSFUL/////////////////////


# fname = input('Enter file name:')
# fh = open(fname)
# lst = list()
# for line in fh:
#     line = line.rstrip()
#     line = line.split()
#     for word in line:
#         if word not in lst:
#             lst.append(word)
#         else:
#             continue

# lst.sort()
# print(lst)


# ////////////////////SUCCESSFUL WITH TIPS/////////////////


# romeo = input("Enter file name: ") # creates handle to file inputed
# juliet = open(romeo) # opens file
# lst = list() # creates empty list
# for line in juliet: # for each line in file:
#     line = line.rstrip() # take away all whitespace
#     line = line.split() # split line into list
#     for words in line: # for each word in the line list:
#         if words not in lst: # if word isn't in the list:
#             lst.append(words) # attach word to list
            
# lst.sort() # observe indentation here. Sort list
# print(lst) # print list


# //////////////////////////COUNTING THINGS IN FILES/////////////////////////////


# fname = input('Enter file name:')
# fh = open(fname)
# count = 0
# for line in fh:
#     if not line.startswith('From '):
#         continue
#     else:
#         i = line.split()
#         count = count + 1
#         print(i[1])

# print('There were', count, 'lines in the file with From as the first word')





# han = open('mbox-short.txt')

# for line in han:
#     line = line.rstrip()
#     # print('Line:', line)
#     wds = line.split()
#     if len(wds) < 3 or wds[0] != 'From': # Guardian Pattern BEFORE
#         # print('Ignore')
#         continue
#     print(wds[2])





# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


# ///////////COUNTING PATTERN////////////////


# name = input('Enter file name: ') # Creates file handle
# handle = open(name) # opens file handle

# counts = dict() # creates dictionary
# for line in handle: # iterates through all lines in the file
#     words = line.split() # splits each line into lists of words
#     for word in words: # iterates through the lists
#         counts[word] = counts.get(word,0) + 1 # Makes the hystogram (adds one per word)

# bigcount = None
# bigword = None
# for word,count in counts.items(): # 'word' gioes through keys, 'count' goes through values
#     if bigcount is None or count > bigcount: # checks if value is the biggest/bigger than bigcount
#         bigword = word # assigns biggest word to here
#         bigcount = count # assigns biggest count to here

# print(bigword, bigcount)


# name = input('Enter file name: ')
# handle = open(name) 

# counts = dict() 
# for line in handle:
#     if not line.startswith('From '):
#         continue
#     else:
#         words = line.split()
#         piece = words[1]
#         counts[piece] = counts.get(piece,0) + 1 

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word 
#         bigcount = count 

# print(bigword, bigcount)


fname = input('Enter file:')
if len(fname) < 1 : fname = 'exterplo.txt'
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for w in words:
        oldcount = di.get(w,0)
        print(w,'old', oldcount)
        newcount = oldcount + 1
        di[w] = newcount


print(di)





# fhand = input('Enter file:')
# fh = open(fhand)

# counts = dict()
# for line in fh:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for val, key in lst[:10]:
#     print(key, val)

# # /////////////////////////////////////////////////////////////
# # ONE LINE WAY TO DO THIS:
# c = {'a':10,'b':1,'c':22}
# print( sorted( [ (v,k) for k,v in c.items() ] ) )   







# fhand = input('Enter file:')
# fh = open(fhand)

# counts = dict()
# for line in fh:
#     if not line.startswith('From ') or len(line) < 4:
#         continue
#     else:
#         words = line.split()
#         wordy = words[5]
#         word = wordy.split(':')
#         wordz = word[0]
#         counts[wordz] = counts.get(wordz, 0) + 1

# lst = list()
# for key, val in counts.items():
#     newtup = (key, val)
#     lst.append(newtup)

# lst = sorted(lst, reverse=False)

# for key, val in lst[:12]:
#     print(key, val)



# from os import linesep
# import re

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if not line.startswith('From'):
#         continue
#     else:
#         words = line.split()
#         email = words[1]
#         pieces = email.split('@')
#         print(pieces)


# hand = open('mbox-short.txt')
# for line in hand:
#     if not line.startswith('From'):
#         continue
#     else:
#         print(line)
#         piece = re.findall('^X.*:', line)
#         print(piece)


# re.search() # returns true/false if string matches regular expression

# x = 'From: Using the : character'
# y = re.findall('^F.+?:', x)
# print(y)

# lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# y = re.findall('@([^ ]*)',lin)
# print(y)

# hand = open('mbox-short.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^X=DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1:
#         continue
#     else:
#         num = float(stuff[0])
#         numlist.append(num)
# print('Maximum:',max(numlist))