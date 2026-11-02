  #python operators.
  #Six types of Python operators:

  #1.(python Arithmetic operators):-
#   | Operator | Name                | Example   | Result |
# | -------- | ------------------- | --------- | ------ |
# | `+`      | Addition            | `5 + 3`   | `8`    |
# | `-`      | Subtraction         | `10 - 4`  | `6`    |
# | `*`      | Multiplication      | `6 * 2`   | `12`   |
# | `/`      | Division            | `10 / 2`  | `5.0`  |
# | `//`     | Floor Division      | `10 // 3` | `3`    |
# | `%`      | Modulus (Remainder) | `10 % 3`  | `1`    |
# | `**`     | Exponent (Power)    | `2 ** 3`  | `8`    |

# #for addition example:
# a = 10
# b = 5
# print(a+b)

# #for subtraction example:
# print(a-b)

# #for multiplication example:
# print(a*b)

# #for division example:
# print(a/b)

# #for floor division example:
# print(a//b)

# #for modulus example:
# print(a%b)

# #for exponent example:
# print(a**b)

  #2.(python Assignment operators):
  
#    | Operator | Name                    | Example   | Same As      |
# | -------- | ----------------------- | --------- | ------------ |
# | `=`      | Assign                  | `x = 5`   | `x = 5`      |
# | `+=`     | Add and Assign          | `x += 3`  | `x = x + 3`  |
# | `-=`     | Subtract and Assign     | `x -= 2`  | `x = x - 2`  |
# | `*=`     | Multiply and Assign     | `x *= 4`  | `x = x * 4`  |
# | `/=`     | Divide and Assign       | `x /= 2`  | `x = x / 2`  |
# | `//=`    | Floor Divide and Assign | `x //= 2` | `x = x // 2` |
# | `%=`     | Modulus and Assign      | `x %= 3`  | `x = x % 3`  |
# | `**=`    | Exponent and Assign     | `x **= 2` | `x = x ** 2` |

#for assign example:
x = 10
print(x)
 
#for add and assign example:
x = 10
x += 5
print(x)

#for subtract and assign example:
x = 10
x -= 2
print(x)

#for multiply and assign example:
x = 10
x *= 4
print(x)

#for divide and assign example:
x = 10
x /= 2
print(x)

#for floor divide and assign example:
x = 10
x //= 2
print(x)

#for modulus and assign example:
x = 10
x %= 3
print(x)

#for exponent and assign example:
x = 10
x **= 2
print(x)
 
#3.(Comparison operators):
# | Operator | Name                  | Example  | Result |
# | -------- | --------------------- | -------- | ------ |
# | `==`     | Equal to              | `5 == 5` | `True` |
# | `!=`     | Not Equal to          | `5 != 3` | `True` |
# | `>`      | Greater Than          | `10 > 5` | `True` |
# | `<`      | Less Than             | `3 < 8`  | `True` |
# | `>=`     | Greater Than or Equal | `5 >= 5` | `True` |
# | `<=`     | Less Than or Equal    | `4 <= 6` | `True` |

#4.(Logical operators):
# | Operator | Name        | Meaning                                |
# | -------- | ----------- | -------------------------------------- |
# | `and`    | Logical AND | দুইটিই True হতে হবে                    |
# | `or`     | Logical OR  | যেকোনো একটা True হলেই হবে              |
# | `not`    | Logical NOT | True কে False এবং False কে True বানায় |

#Example:
# a = 10
# b = 5

# print(a > b and a == 10)   # True
# print(a > b and b > 10)    # False

# print(a > b or b > 10)     # True
# print(a < b or b > 10)     # False

# print(not(a > b))          # False
# print(not(a < b))          # True

  #5.(Identity operators):
#   | Operator | Name   | Meaning                  |
# | -------- | ------ | ------------------------ |
# | `is`     | Is     | একই object হলে `True`    |
# | `is not` | Is Not | একই object না হলে `True` |
# | Operator | কাজ                               |
# | -------- | --------------------------------- |
# | `==`     | value একই কি না check করে         |
# | `is`     | memory/object একই কি না check করে |

#example:
# a = [1, 2]
# b = [1, 2]
# c = a

# print(a == b)      # True
# print(a is b)      # False
# print(a is c)      # True
# print(a is not b)  # True

# a = 10
# b = 10
# c = 5

# print(a is b)        # True
# print(a is not c)    # True
# print(a == b)        # True
# print(a is c)        # False

#6.(Membership operators):
# | Operator | Meaning         |
# | -------- | --------------- |
# | `in`     | ভিতরে আছে কি না |
# | `not in` | ভিতরে নেই কি না |

#example:
# numbers = [10, 20, 30, 40]

# print(10 in numbers)        # True
# print(50 in numbers)        # False

# print(50 not in numbers)    # True
# print(20 not in numbers)    # False

#Swaping:
# একে অপরের সাথে মান পাল্টে যাবে ফলাফলে এটাই সোপিং
# example:
# x = 1
# y = 2

# x, y = y, x

# print(x, y)   # 2 1