def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two).capitalize()
    return (f'{one}{delimiter}{two}')

print(get_summ('Learn','python'))

assert get_summ('Learn', 'Python', delimiter=' ') == 'Learn Python'
assert get_summ('Learn', 'python', delimiter=' ') == 'Learn Python'
assert get_summ('1', '1', delimiter='+') == '1+1'
assert get_summ('Batman', 'Robin') == 'Batman&Robin'