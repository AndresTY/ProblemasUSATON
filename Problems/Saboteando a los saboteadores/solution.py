def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    aux = [v for v in string_ if v not in vowels]
    
    print(''.join(map(str, aux))[::-1])
# Test the function

if __name__ == '__main__':
    test_input = input()
    disemvowel(test_input)


