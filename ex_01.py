"""{
y=0.5x+0.5
y=-x+2}"""

import matplotlib.pyplot as plt


def resolve(x):
    y1 = 0.5 * x + 0.5
    y2 = x * -1 + 2
    return y1,y2
    
def cria_vetores(max_X):
    vals_x = []
    vals_y1 = []
    vals_y2 = []
    for i in range(max_X):
        y1, y2 = resolve(i)
        vals_y1.append(y1)
        vals_y2.append(y2)
        vals_x.append(i)
        if y1 == y2:
            plt.scatter(i,y1, color="black", label="interseção")
            print(f"o resultado do sistema de equações é: x = {i} e por consequencia y= {y1}")
    return vals_x, vals_y1, vals_y2
    
def des_linha(vals_x, vals_y1, vals_y2):
    plt.plot(vals_x, vals_y1, color='blue', label='equação 1')
    plt.plot(vals_x, vals_y2, color='red', label='equação 2')
    plt.legend()
    plt.show()
    
while True:
    max_X = int(input("diga o valor maximo de X: "))
    vals_x, vals_y1, vals_y2 = cria_vetores(max_X)      
    des_linha(vals_x, vals_y1, vals_y2)