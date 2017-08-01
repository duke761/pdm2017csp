                        # this is setting up the values for each letter in roman numerals
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

                         #defining the function
def num2roman(num):     #this is what you type to runt he program
                        #setting the intial parameters for the variable
    roman = ''
                        #while loop deconstucts the number using the num_map from abov e
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
                        # returns the result
    return roman