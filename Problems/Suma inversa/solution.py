def addTwoArrays(l1, l2):
    aux = 0  # Carries the decimal
    result = []

    lx = l1 if len(l1) >= len(l2) else l2
    ly = l1 if len(l1) < len(l2) else l2

    for idx, val1 in enumerate(lx):
        val2 = ly[idx] if len(ly) > idx else 0

        r = val1 + val2 + aux
        # The new digit is the remainder of r divided by 10
        result.append(str(r % 10))
        # Update aux to be the carry (1 if r >= 10, 0 otherwise)
        aux = r // 10

    if aux:
        result.append(int(aux))

    # Print the values of result separated by space
    print(" ".join(map(str, result)))

# Test the function
if __name__ == '__main__':
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]

    addTwoArrays(l1, l2)
