x, y = int(input()), int(input())
x1, y1 = y, x + y 
x, y = x_orig, y_orig 
x = y 
y = x + y
print("Одновременно:", x1, y1)
print("По очереди:", x, y) 
# тут я запутался, пишет ошибка, не могу разобраться