num = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

def num_to_words(n):
    if n <= 20:
        return num[n]
    else:
        string = str(n)
        length = len(string)
        if length == 2:
            return two_digits(string)
        elif length == 3:
            if string[1:] == '00':
                return num[int(string[0])] + "hundred"
            else:
                return num[int(string[0])] + "hundredand" + two_digits(string[1:])
        elif length == 4:
            return "onethousand"
        else:
            print "You done goof'd son."

def two_digits(string):
    if string[0] == '0':
        string = string[1]
    if int(string) <= 20:
        return num[int(string)]
    elif string[1] != '0':
        return num[int(string[0]) * 10] + num[int(string[1])]
    else:
        return num[int(string[0]) * 10]

sum = 0
for i in range(1, 1001):
    sum += len(num_to_words(i))

print sum
