#task 1

sequence = input("")


sequence = sequence.split(",")
sequence = [int(num) for num in sequence]


if len(sequence) > 2:

  if sequence[1] - sequence[0] == sequence[-1] - sequence[-2]:
    next_number = sequence[-1] + (sequence[-1] - sequence[-2])
    print(next_number)

  elif sequence[1] / sequence[0] == sequence[-1] / sequence[-2]:
    next_number = sequence[-1] * (sequence[-1] / sequence[-2])
    print(next_number)
  else:
    print("Последовательность не распознана")
else:
  print("Последовательность должна содержать как минимум 3 числа")


#task 2
def find_largest_palindrome():
    largest_palindrome = 0
    factors = (0, 0)

    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j

            if str(product) == str(product)[::-1]:

                if product > largest_palindrome:
                    largest_palindrome = product
                    factors = (i, j)


    return largest_palindrome, factors


largest_palindrome, factors = find_largest_palindrome()
print(largest_palindrome)
print("Этот палиндром получен умножением", factors[0], "и", factors[1])






