def multiply(decimal_a, decimal_b):
    return decimal_a * decimal_b

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def check_answer(a, b, expected_result, system):
    if system == "bin":
        a_dec = binary_to_decimal(str(a))
        b_dec = binary_to_decimal(str(b))
        expected_result_dec = binary_to_decimal(str(expected_result))
    elif system == "oct":
        a_dec = int(str(a), 8)
        b_dec = int(str(b), 8)
        expected_result_dec = int(str(expected_result), 8)
    else:
        a_dec = a
        b_dec = b
        expected_result_dec = expected_result

    result_dec = multiply(a_dec, b_dec)
    if result_dec == expected_result_dec:
        return "YES"
    else:
        return "NO"

# Примеры проверки
print(check_answer(1, 8, 54, "bin"))  # YES
print(check_answer(2, 16, 19, "oct"))  # NO
