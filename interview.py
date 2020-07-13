# Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
# For example, given the following object/dictionary as input:

# Your algorithm should return 41, the sum of the values 23 and 18.
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

#counter set to 0 
#for loop through the dict add the index of each value to the counter
# getting values will use the dictionary_name.values()

myDict = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}


def counter(myDict):
    count = 0
    for key, value in myDict.items(): #.values() method didnt work/ key, value was used instead of i because i wouldve gotten both keys and vlaues when you were just looking for values 
        if type(value) == int:
            count = count + value
    return count


print(counter(myDict))


