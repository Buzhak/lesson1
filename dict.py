dict_0 = {'city':'Moscow', 'temp':'20'}
print(dict_0['city'])

temp = int(dict_0['temp'])
dict_0['temp'] = str(temp-5)
print(dict_0)

print(dict_0.get('country'))
print(dict_0.get('country', 'Russia'))
dict_0['date']='27.05.2019'

print(len(dict_0))
print(dict_0)