from tkinter import *
import scipy.stats as st


def prueba_rachas(nums, n, f, alpha):
    high = 0
    low = 0
    R = 0
    last_change = ''
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            low += 1
            if last_change != '-':
                R += 1
                last_change = '-'
        elif nums[i] < nums[i + 1]:
            high += 1
            if last_change != '+':
                R += 1
                last_change = '+'
    f.write("----- PRUEBA DE RACHAS -----\n\n")
    try:
        u = ((2 * high * low) / (high + low)) + 1
        o2 = ((2 * high * low) * ((2 * high * low) - high - low)) / ((high + low) ** 2 * (high + low - 1))
        o = o2 ** (1 / 2)
        ZR = abs((R - u) / o)
        #alpha = 0.05  # ESTE DATO DESPUES SE TIENE QUE LEER DESDE TKINTER
        z_value = st.norm.ppf(1 - (alpha / 2))

        f.write("Valor Crítico Obtenido = {}\n".format(ZR))
        f.write("Valor de la Tabla = {}\n".format(z_value))
        if ZR > z_value:
            f.write("¿¿ {} > {} ?? SI, por lo tanto se ACEPTA\n\n".format(ZR, z_value))
        else:
            f.write("¿¿ {} > {} ?? NO, por lo tanto se RECHAZA\n\n".format(ZR, z_value))
    except ZeroDivisionError:
        f.write("La prueba no se puede llevar a cabo\n\n")



def kolmogorov_smirnov(numbers, n, f):
    isobreNmenosRi = []  # Creamos una lista que va a contener los valores de i/N-Ri
    riMenosiMenosUnoSobreN = []  # Creamos una lista que va a contener los valores de Ri-(i-1)/N
    alpha: float = 0.21012  # Este numero va a cambiar
    print(numbers)

    for i in range(n - 1):  # loop que pasa por todos los numeros de la lista
        isobreNmenosRi.append(((i / n) - numbers[i]))  # Agrega los numeros de i/N-Ri a la lista
        riMenosiMenosUnoSobreN.append((numbers[i] - (i - 1)) / n)  # Agrega los numeros Ri-(i-1)/N a la lista

    dPlus = max(isobreNmenosRi)  # Agarra el valor máximo de la lista
    dMinus = max(riMenosiMenosUnoSobreN)  # Agarra el valor máximo de la lista
    d = max(dPlus, dMinus)  # Agarra el valor máximo de ambas listas
    f.write("----- PRUEBA DE Kolmogorov_Smirnov-----\n\n")
    f.write("{}".format(d)) #< -Aqui se imprime el valor de D
    if d<=alpha: #El valor máximo de ambas listas es comparado con alpha
        f.write("La hipotesis es aceptada")
    else:
        f.write("La hipotesis es rechazada")

def scale_to_interval(nums, min, max):
    with open("random_nums_interval.txt", "w") as f:
        for num in nums:
            scaled_num = (max - min) * num + min
            f.write("{}\n".format(scaled_num))

root = Tk()
root.title("Proyecto")

answer_label = Label(root, text="---")
answer_label.grid(row=0, column=0)

label1 = Label(root, text="Introduce a")
label1.grid(row=1, column=0)

num1_txtbx = Entry(root)
num1_txtbx.grid(row=1, column=1)

label2 = Label(root, text="Introduce c")
label2.grid(row=2, column=0)

num2_txtbx = Entry(root)
num2_txtbx.grid(row=2, column=1)

label3 = Label(root, text="Introduce m")
label3.grid(row=3, column=0)

num3_txtbx = Entry(root)
num3_txtbx.grid(row=3, column=1)

label4 = Label(root, text="Introduce x0")
label4.grid(row=4, column=0)

num4_txtbx = Entry(root)
num4_txtbx.grid(row=4, column=1)

label5 = Label(root, text="Introduce N")
label5.grid(row=5, column=0)

num5_txtbx = Entry(root)
num5_txtbx.grid(row=5, column=1)

label6 = Label(root, text="Introduce alpha")
label6.grid(row=6, column=0)

num6_txtbx = Entry(root)
num6_txtbx.grid(row=6, column=1)

label7 = Label(root, text="Introduce min")
label7.grid(row=7, column=0)

num7_txtbx = Entry(root)
num7_txtbx.grid(row=7, column=1)

label8 = Label(root, text="Introduce max")
label8.grid(row=8, column=0)

num8_txtbx = Entry(root)
num8_txtbx.grid(row=8, column=1)


def addF():
    if (num1_txtbx.get() != "" and num2_txtbx.get() != "" and num3_txtbx.get() != "" and num4_txtbx.get() != "" \
        and num5_txtbx.get() != "" and num6_txtbx.get() != "" and num7_txtbx.get() != "" and num8_txtbx.get() != ""):
        try:
            numA = int(num1_txtbx.get())
            numC = int(num2_txtbx.get())
            numM = int(num3_txtbx.get())
            num_x = int(num4_txtbx.get())
            num_n = int(num5_txtbx.get())
            num_alpha = float(num6_txtbx.get())
            num_min = float(num7_txtbx.get())
            num_max = float(num8_txtbx.get())

            with open('random_nums.txt', 'w') as f:
                for _ in range(num_n):
                    # a = 24, c = 68, m = 37, x0 = 85, N = 40
                    rand_num = ((numA * num_x + numC) % numM)
                    num_x = rand_num
                    rand_num /= numM
                    f.write('{}\n'.format(rand_num))

            with open('random_nums.txt', 'r') as f:
                numbers = [float(i) for i in f.readlines()]

            with open('results.txt', 'w', encoding="utf-8") as f:
                prueba_rachas(numbers, num_n, f, num_alpha)
                kolmogorov_smirnov(numbers, num_n, f)
                #Prueba Chi-Cuadrada
                scale_to_interval(numbers, num_min, num_max)

            #answer_label.configure(text=answer)
            status_label.configure(text="Success")
        except ValueError:
            status_label.configure(text="invalid input, check your input types")
    else:
        status_label.configure(text="fill in all the required fields")


calculate_button = Button(root, text="calculate", command=addF)
calculate_button.grid(row=9, column=0, columnspan=2)

status_label = Label(root, height=5, width=25, bg="black", fg="#00FF00", text="---", wraplength=150)
status_label.grid(row=10, column=0, columnspan=2)

root.mainloop()
