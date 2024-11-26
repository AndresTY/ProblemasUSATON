def reduce_string(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the last element if it matches the current character
        else:
            stack.append(char)  # Add current character to the stack
    
    # Join the remaining characters in the stack to form the reduced string
    reduced_string = ''.join(stack)
    return reduced_string if reduced_string else "fake file"

# Test the function

if __name__ == '__main__':


    s = input()

    result = reduce_string(s)

    print(result)

