#split a string to chars
s = "12345"
chars = list(s)


#String Trim
s1 = '  abc  ' 
print(f'String =\'{s1}\'')
print(f'After Removing Leading Whitespaces String =\'{s1.lstrip()}\'')
print(f'After Removing Trailing Whitespaces String =\'{s1.rstrip()}\'')
print(f'After Trimming Whitespaces String =\'{s1.strip()}\'')

#String replace
str = "this is string example....wow!!! this is really string"
print(str.replace("is", "was"))

#Lists Join to a String
s = "".join([1,2,3])

#String split to a list
l = ",".split("1,3,4,5")

#format String
var1 = "foo"
var2 = "bar"
var3 = f"{var1}{var2}"

#is vs == string comparison
#https://stackoverflow.com/questions/1504717/why-does-comparing-strings-using-either-or-is-sometimes-produce-a-differe

#Sort a list
l = [1,2,3]
l.sort() #O(nlogn) Timesort / mergesort