# functions
last_name = "N"


# def function1(name, last_name, *args, key1=None, **kwargs):
#     # last_name = 'C'
#     print(f"My Function: {name}, {last_name}, with args: {args} and key_words: {key1} and kwargs: {kwargs}")
#     return None
#
# result = function1("F1", "F2", "NEW_ARGUMENT", key1="TEST", key2=True)
# print(result)
# print(last_name)

# def function1(key1=True, key2=False):
#     # last_name = 'C'
#     print(f"My Function:with  key_words: {key1} and: {key2}")
#     return None
#
#
# result = function1("F1", "F2", )
# print(result)
# print(last_name)

var1 = 1

def sum_numbers(number_a, number_b):
    global var1
    var1 = var1 + 1
    result = number_a + number_b + var1
    return result

result1 = sum_numbers(10, 20)
result2 = sum_numbers(10, 20)
result3 = sum_numbers(10, 20)
print(result3)
print(var1)