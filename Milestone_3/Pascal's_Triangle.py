def get_triangle(rows: int):
  res = [[1], [1, 1]]
  current_row = [1]
  previous_row = [1, 1]
  for i in range(rows):
    for j in range(len(previous_row) - 1):
      current_row.append(previous_row[j] + previous_row[j+1])
    current_row.append(1)
    res.append(current_row)
    previous_row = current_row
    current_row = [1]

  return res[:-2]


print(get_triangle(5))


numbers = get_triangle(5)

numbers_str = []
for row in numbers:
  str_row = []
  for number in row:
    str_row.append(str(number))
  numbers_str.append(' '.join(str_row))

last_line_length = len(numbers_str[-1])

for row in numbers_str:
  print(row.center(last_line_length))