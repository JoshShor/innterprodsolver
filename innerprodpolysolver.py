# solve inner products

# p = x + x^3
# q = x + x^2

x = [1, 2, 3, 4]
p = 0;
q = 0;
holder = 0;
n = 0;

for i in range(len(x)):
    # print(str(x[i]) + " is the number")
    holder = (x[i] + x[i]**3)*(1 + x[i]**2)
    # print(str(holder) + " is the result")
    n += holder

print(n)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
