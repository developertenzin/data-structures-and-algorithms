#'python3'

def main():
    user_input = input()
    content = user_input.split()
    a = int(content[0])
    b = int(content[1])
    print(a + b)

main()

'''
#Alternative Solution
import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
'''