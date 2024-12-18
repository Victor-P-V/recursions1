def get_multiplied_digits(number):
    str_number = str(number)
    first=int(str_number[0:+1])

    if len(str_number)!=1:
        return get_multiplied_digits(int(str_number[1:])) * first
    elif (first == 0 or get_multiplied_digits(int(str_number[1:])) == 0):
        return 1
    else:
        return first

result = get_multiplied_digits(402030)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
