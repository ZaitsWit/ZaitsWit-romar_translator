r_Dict, string, result, ded = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, str(input()).upper(), 0, 0
for i in range(0, len(string) - 1):
    if r_Dict[string[i]] < r_Dict[string[i + 1]]:
        for j in string[:i + 1]:
            if r_Dict[j] <= r_Dict[string[i]]:
                result -= r_Dict[j]
    elif r_Dict[string[i]] == r_Dict[string[i + 1]]:
        ded += r_Dict[string[i]]
    elif r_Dict[string[i]] > r_Dict[string[i + 1]]:
        result += r_Dict[string[i]] + ded
        ded = 0
print(result + r_Dict[string[-1:]] + ded)
