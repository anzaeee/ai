# %% [markdown]
# Question 1, Part (a)

# %%
#creating a variable for input bookings
n = int (input('Enter the total number of bookings: ') )

#creating an empty list to store our bookings
Car_Bookings = []

for i in range(0, n):
    booking = [ int (input("Enter start day: ") ), int(input("Enter end date: "))]
    Car_Bookings.append(booking)
    #print(booking)

current_val = Car_Bookings
min_cars = 0

for i in range(len(Car_Bookings)):
    if current_val [i][0] <= Car_Bookings[i][0] and current_val[i][1] >= Car_Bookings[i][0]:
        min_cars += 1

print(min_cars)

# %% [markdown]
# Question 1, Part (b)

# %%
#Function definition
def search(list, val):
    for i in range(len(list)):
        if list[i] == val:
            return True
    return False


def most_frequent_elements_in_lis(elem_list, left, right, frequency):
    #Assuming left is the starting point of our list, and right is the ending point of our iteration

    i = left #assigning the start of our list to iterator i
    dup_arr = []
    dup_freq = [] 
    #Here arr and freq are two lists that will store our results. They act parallel to each other.

    while i <= right:
        dup_arr.append(elem_list[i]) #creating the list we NEED from given 
        i += 1

    for i in range (len(dup_arr)):
        val = dup_arr[i]
        count = 0
        for i in range(len(dup_arr)):
            if dup_arr[i] == val:
                count += 1
        else:
            if count >= frequency:
                #print(count, ',', val)
                if search(dup_freq, val) == False:
                    dup_freq.append(val)
    return dup_freq

        

#The execuatable
lis = [2,2,4,2,4,5,6, 1 ,1]

print ( most_frequent_elements_in_lis(lis,0,7,2) )



# %%
#Function definition
def get_student_marks(input_list):
#{ output should look like
#'p18-1001': {'english': 61.5,
#'calculus': 38.5},
#'p18-1002': {'english': 38.5,
#'programming fundaments': 38.5},
#'p18-1003': {'calculus': 36.9,
#'programming fundamentals': 38.5}}
    
    new_dict = {}
    for i in range (len (input_list) ):
        new_dict[i] = {input_list[i]['roll_no']}
       # for j in range (len ( input_list[i]['marks'] )):
            

    print(new_dict)

#Function call and dictionary declaration
input_list = [{'roll_no': 'p18-1001', 'marks': {
'english': (1.4, 2.5, 15, 9.6, 33),
'calculus': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 88.4
},
{'roll_no': 'p18-1002', 'marks': {
'english': (2.4, 1.5, 12, 1.6, 21),
'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4
},
{'roll_no': 'p18-1003', 'marks': {
'calculus': (2.4, 1.5, 12, None, 21),
'programming fundamentals': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4 }]

get_student_marks(input_list)

# %% [markdown]
# Question 2, part (a)

# %%
import numpy as np

#Creating the array
np_arr = np.random.randint(1,10,size=(7,7))
print(np_arr)

# %% [markdown]
# (i)

# %%
def second_Max_RowSum(mat):
    row, column = mat.shape
    sum = []

    for i in range(row):
        sumofrow = 0
        for j in range(column):
            sumofrow += mat[i][j]
        sum.append(sumofrow)

#Now we have sum containing all sum of rows
    #print(sum)
    max_val = max(sum) 
    sum.remove(max_val)

    #As first maximum is removed, the second maximum value will now be the value returned by built-in function max
    return max(sum)
#execution
print(second_Max_RowSum(np_arr) )


# %% [markdown]
# ii)

# %%
def Upper_or_Lower(mat):
    upper = True
    lower = True
    for i in range(1, len(mat)):
        for j in range(0, i):
            if(mat[i][j] != 0):
                    upper = False
    
    for i in range(0, len(mat)):
        for j in range(i + 1, len(mat)):
            if(mat[i][j] != 0):
                    lower = False
    
    if upper == True and lower == True:
        return 'both'
    elif upper == True:
        return 'upper'
    elif lower == True:
        return 'lower'
    else:
        return 'neither'

# %% [markdown]
# iii)

# %%
def minimum_sum_of_row(mat):
    row, column = mat.shape
    sum = []

    for i in range(row):
        sumofrow = 0
        for j in range(column):
            sumofrow += mat[i][j]
        sum.append(sumofrow)

#Once sums are obtained
    return min(sum)

print(minimum_sum_of_row(np_arr))

# %% [markdown]
# iv)

# %%
def swap_Odd_Rows(mat):
    row, column = mat.shape

    # In array indexing 1st row is odd however will be 0th row in code. Hence condition here will be if I is even SWAP rows
    for i in range(row):
        if i % 2 == 0: #row is odd in actuality
            new_row = []
            for x in range(row):
                for j in range(column):
                    new_row.append( mat[x][j] )
            if i + 2 < row:
                for y in range(column):
                    mat[i][y] = mat[i+2][y]
                    mat[i+2][y] = new_row[y]
    return mat

print(swap_Odd_Rows(np_arr))

# %% [markdown]
# v)

# %%
def Mean_of_Rows(mat):
    row, column = mat.shape
    means = []

    for i in range(row):
        sumofrow = 0
        for j in range(column):
            sumofrow += mat[i][j]
        means.append(sumofrow / row)

    return means
Mean_of_Rows(np_arr)

# %% [markdown]
# vi)

# %%
def sortColumns(mat):
    row, column = mat.shape
    for j in range(column):
        cols = []
        for i in range(0, row):
            val = mat[i][j]
            cols.append(val)
        cols.sort() #sorts into ascending by default
        #print(cols)
        for x in range(row):
            mat[x][j] = cols[x]

    return mat

sortColumns(np_arr)

# %% [markdown]
# Question 2, part (b)

# %%
import numpy as np
def search(list, val):
    for i in range(len(list)):
        if list[i] == val:
            return True
    return False

n = np.random.randint(1,5)
arr_s = np.random.randint(65,127, 10)
searched = []
s = ""
#print(arr_s)

for i in range (n):
    if search(searched, i) == False:
        s += chr(arr_s[i])

print(s)


# %% [markdown]
# Question 2, part (c)

# %%
import numpy as np

#Creating the array
arr = np.random.randint(0,2,size=(6,6))
r,c = arr.shape
hourglass_sums = []
for i in range(0, r-2):
        for j in range(0, c-2):
            sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
        hourglass_sums.append(sum)
 
print( max(hourglass_sums) )

# %% [markdown]
# Question 2, part (d)

# %%
# part i

arr = np.array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]) 
arr[arr%2 == 1] = -1

print(arr)

# part ii

a = np.random.randint(0,18, 10)
np.where(np.logical_and(a>=5, a<=10))

# %% [markdown]
# Question 3, part (a)

# %%
import sys

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

if len(str1) != len(str2):
    sys.exit('Given strings are not anagrams as they are inequal of length')

str1 = sorted(str1)
str2 = sorted(str2)

for i in range(len(str1)):
    if str1[i] != str2[i]:
        sys.exit('Given strings are not anagrams')
else:
    print('Given strings are anagrams')


# %% [markdown]
# Question 3, part (b)

# %%
import sys

def checkRot(str1, str2):
    if len(str1) != len(str2):
        sys.exit('Given strings are not rotations as they are inequal in length')

    n = len(str2)

    if str2[n - 1] == str1[0] or str1[n-1] == str2[0]:
        return True
    else:
        return False

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

print(checkRot(str1,str2))


# %% [markdown]
# Question 3, part (c)

# %%
import numpy as np

asc_arr = np.arange(start=26, stop=0, step=-1)
arr_0s = np.zeros(26)
char_arr = []

for i in range(65,91):
    char_arr.append(chr(i))

str1 = input('Enter desired string:')
#In case string is not all caps
str1 = str1.upper()

for i in range(len(str1)):
    for j in range(len(char_arr)):
        if char_arr[j] == str1[i]:
            arr_0s[j] += 1

super_str = False
for i in range(len(char_arr)):
    if asc_arr[i] == arr_0s[i]:
        super_str = True
    else:
        super_str = False

if super_str == True:
    print(str1 + ' is SUPERSTRING')
elif super_str == False:
    print(str1 + ' not SUPERSTRING')


# %% [markdown]
# Question 4

# %%
class Game:
    def __init__(self):
        self.deck = []
        self.players = []
        self.cards_pickup = 0
        self.turns_to_wait = 0
        self.requested_value = None
        self.requested_suit = None
        self.actioncard = 0

def StartGame():
    p = input(int(p))
    

# %% [markdown]
# 


