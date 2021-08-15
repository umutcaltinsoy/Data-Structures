# setdefault()

# This method returns the value of a key (if the key is in dict.)
# If not, it inserts key with a value to the dict.

# Syntax : dict.setdefault(key, default_value)
# Parameters : It takes two parameters : key- value(optional)



# Example 1 :
Dictionary1 = {'A' : 'Umut', 'B' : 'Cagri', 'C' : 'Altinsoy'}

# using setdefault() method
Third_value = Dictionary1.setdefault('C')
print("Third_value : ", Third_value)


# When key isn't in the dict.
Dictionary1 = {'A' : 'Umut', 'B' : 'Cagri'}

Third_value = Dictionary1.setdefault('C')
print("Dictionary : ", Dictionary1)
print("Third_value : ", Third_value)

# using setdefault() method
# when key is not in the Dictionary
# but default value is provided
Fourth_value = Dictionary1.setdefault('D', 'Zed')
print("Dictionary : ", Dictionary1)
print("Fourth_value : ", Fourth_value)
