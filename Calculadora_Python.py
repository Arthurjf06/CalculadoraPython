import tkinter as tk

calculation = ''

def add_a_calculation(simbolo):
    global calculation
    calculation += str(simbolo)
    resultado_de_texto.delete(1.0, "end")
    resultado_de_texto.insert(1.0, calculation)
def valor_do_calculo():
    global calculation
    try: 
        result = str(eval(calculation))
        calculation = ""
        resultado_de_texto.delete(1.0,"end") 
        resultado_de_texto.insert(1.0, result) 
    except:
        limpar_a_calculadora()
        resultado_de_texto.insert(1.0,"Error")
            

def limpar_a_calculadora():
    global calculation
    result = str(eval(calculation))
    calculation = ""
    resultado_de_texto.delete(1.0,"end")

root= tk.Tk()
root.geometry("300x275")
resultado_de_texto = tk.Text(root,height=2, width=16, font=("Arial",24))
resultado_de_texto.grid(columnspan=5)



botao_1=tk.Button(root, text="1", command=lambda:add_a_calculation(1), width=5, font=("Arial", 14))
botao_1.grid(row=2, column=1)
botao_2=tk.Button(root, text="2", command=lambda:add_a_calculation(2), width=5, font=("Arial", 14))
botao_2.grid(row=2, column=2)
botao_3=tk.Button(root, text="3", command=lambda:add_a_calculation(3), width=5, font=("Arial", 14))
botao_3.grid(row=2, column=3)
botao_4=tk.Button(root, text="4", command=lambda:add_a_calculation(4), width=5, font=("Arial", 14))
botao_4.grid(row=3, column=1)
botao_5=tk.Button(root, text="5", command=lambda:add_a_calculation(5), width=5, font=("Arial", 14))
botao_5.grid(row=3, column=2)
botao_6=tk.Button(root, text="6", command=lambda:add_a_calculation(6), width=5, font=("Arial", 14))
botao_6.grid(row=3, column=3)
botao_7=tk.Button(root, text="7", command=lambda:add_a_calculation(7), width=5, font=("Arial", 14))
botao_7.grid(row=4, column=1)
botao_8=tk.Button(root, text="8", command=lambda:add_a_calculation(8), width=5, font=("Arial", 14))
botao_8.grid(row=4, column=2)
botao_9=tk.Button(root, text="9", command=lambda:add_a_calculation(9), width=5, font=("Arial", 14))
botao_9.grid(row=4, column=3)
botao_0=tk.Button(root, text="0", command=lambda:add_a_calculation(0), width=5, font=("Arial", 14))
botao_0.grid(row=5, column=2)
botao_mais=tk.Button(root, text="+", command=lambda:add_a_calculation("+"), width=5, font=("Arial", 14))
botao_mais.grid(row=2, column=4)
botao_menos=tk.Button(root, text="-", command=lambda:add_a_calculation("-"), width=5, font=("Arial", 14))
botao_menos.grid(row=3, column=4)
botao_mult=tk.Button(root, text="*", command=lambda:add_a_calculation("*"), width=5, font=("Arial", 14))
botao_mult.grid(row=4, column=4)
botao_divi=tk.Button(root, text="/", command=lambda:add_a_calculation("/"), width=5, font=("Arial", 14))
botao_divi.grid(row=5, column=4)
botao_abre=tk.Button(root, text="(", command=lambda:add_a_calculation("("), width=5, font=("Arial", 14))
botao_abre.grid(row=5, column=1)
botao_fecha=tk.Button(root, text=")", command=lambda:add_a_calculation(")"), width=5, font=("Arial", 14))
botao_fecha.grid(row=5, column=3)
botao_limpar=tk.Button(root, text="C", command=limpar_a_calculadora, width=11, font=("Arial", 14))
botao_limpar.grid(row=6, column=1, columnspan=2)
botao_igual=tk.Button(root, text="=", command=valor_do_calculo, width=11, font=("Arial", 14))
botao_igual.grid(row=6, column=3, columnspan=2)



root.mainloop()