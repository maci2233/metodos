#TODOS ESTOS VALORES SE SACARAN DE LO QUE INGRESE EL USUARIO EN LA GUI
a = 24
c = 68
m = 37
x0 = 85
N = 100

with open('random_nums.txt', 'w') as f:
    for _ in range(N):
        rand_num = ((a * x0 + c) % m) / m
        print(rand_num)
        f.write('{}\n'.format(rand_num))
        x0 = rand_num

with open('random_nums.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(line)
