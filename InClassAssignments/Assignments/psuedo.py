def myAtoi(str1):
    posRange = (2**31) -1
    negRange = (2**31)
    negflag = False
    if len(str1) == 0:
        return 0

    str1 = str1.strip()
    if str[0] == '-':
        negflag = True
        str1 = str[1:]
    elif str1[0] == '+':
        str1 = str[1:]
    
    if len(str1) == 0:
        return 0

    val = 0
    if not str1[0].isnumeric():
        return 0
    for ch in str1:
        if negflag:
            if val > negRange//10 or (val == negRange//10 and int(ch)>8):
                return negRange*(-1)
        else:
            if val > posRange//10 or (val == posRange//10 and int(ch)>8):
                return posRange
            else:
                val = val *10 + int(ch)
            val = val *10 +int(ch)
    return val*(-1) if negflag else val
    if negflag:
        return val*(-1)
    else:
        return val

