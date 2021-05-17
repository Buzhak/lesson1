def compare_str(str0,str1) -> int:
    if type(str0) != str or type(str1) != str:
        return 0
    elif str0 != str1 and len(str0)>len(str1):
        return 2
    elif str0 != str1 and str1 == 'learn':
        return 3
    else: return 1


str0 = '222'
str1 = 'learn'
print(compare_str(str0, str1))