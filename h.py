'''string = input()

print (list(c.isalnum() for c in string))
print (list(c.isalpha() for c in string))
print (list(c.isdigit() for c in string))
print (list(c.islower() for c in string))
print (list(c.isupper() for c in string))
'''
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    #result =
    #print(result)