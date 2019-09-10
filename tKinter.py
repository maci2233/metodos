from tkinter import *

def prueba_rachas(nums, n):
    high = 0
    low = 0
    R = 0
    last_change = ''
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            low += 1
            if last_change != '-':
                R += 1
                last_change = '-'
        elif nums[i] < nums[i+1]:
            high += 1
            if last_change != '+':
                R += 1
                last_change = '+'
    u = ((2 * high * low) / (high + low)) + 1
    o2 = ((2 * high * low) * ((2 * high * low) - high - low)) / ((high + low)**2 * (high + low - 1))
    o = o2**(1/2)
    ZR = (R-u) / o
    print(high, low, R, u, o2, o, ZR)



root = Tk()
root.title("Adding")

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

def addF():
    if (num1_txtbx.get() and num2_txtbx.get() and num3_txtbx.get() and num4_txtbx.get() and num5_txtbx.get() != ""):
        try:
            numA = int(num1_txtbx.get())
            numC = int(num2_txtbx.get())
            numM = int(num3_txtbx.get())
            num_x = int(num4_txtbx.get())
            num_n = int(num5_txtbx.get())

            with open('random_nums.txt', 'w') as f:
                for _ in range(num_n):
                    #a = 24c = 68m = 37x0 = 85N = 100
                    rand_num = ((numA * num_x + numC) % numM) / numM
                    f.write('{}\n'.format(rand_num))
                    num_x = rand_num

            with open('random_nums.txt') as f:
                numbers = f.readlines()
                prueba_rachas(numbers, num_n)


            answer_label.configure(text=answer)
            status_label.configure(text="Success")
        except:
            status_label.configure(text="invalid input, check your input types")
        else:
            status_label.configure(text="fill in all the required fields")


calculate_button = Button(root, text="calculate", command=addF)
calculate_button.grid(row=6, column=0, columnspan=2)

status_label = Label(root, height=5, width=25, bg="black", fg="#00FF00", text="---", wraplength=150)
status_label.grid(row=7, column=0, columnspan=2)

root.mainloop()
