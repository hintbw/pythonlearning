string = "hello world"
strings_with_o = [s for s in string.split() if 'o' in s]
print(strings_with_o)  # ['world']