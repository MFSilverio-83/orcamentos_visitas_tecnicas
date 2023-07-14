'''
Código para calcular o valor de uma visita técnica. Informando a Cidade, a distância da sede até esta cidade
e o valor do serviço a ser cobrado.
'''

import tkinter as tk
import pyperclip as pc

def calcular():
    cidade = informarCidade.get()
    km = float(informarKM.get())
    servico = float(informarvalorServico.get())
    # o valor do Km é relacionado a ida e volta, multiplicado pelo valor do custo por Km (1.50)
    valor_km = (km * 2) * 1.5
    valor_visita["text"] = f'''
Visita técnica em {cidade} para manutenção em equipamento Dimep.
R$ {str(f'{valor_km:.2f}'.replace('.', ','))}

Serviço de manutenção em equipamento Dimep.
R$ {str(f'{servico:.2f}'.replace('.', ','))} (Valor por equipamento / não incluso peças)

Pagamento
= 28 DDF'''
    valor_visita["font"] = ('Arial', '9')
    # Usado para copiar o retorno para uma área de transferência - e-mail.
    pc.copy(valor_visita["text"])


janela = tk.Tk()
janela.title('ORÇAMENTO PARA VISITAS TÉCNICAS')
janela.configure(bg='#32CD32')
janela.geometry("600x500")

cidade = tk.Label(text="CIDADE ", font='bold', fg='green', borderwidth=1, relief='solid', anchor='w')
cidade.grid(row=0, column=0, padx=15, pady=15, sticky='nswe', columnspan=2)

informarCidade = tk.Entry(fg='green', font='bold', borderwidth=1, relief='solid')
informarCidade.grid(row=0, column=2, padx=15, pady=15, sticky='nsew', columnspan=5)

km = tk.Label(text="KM", font='bold', fg='green', borderwidth=1, relief='solid', anchor='w')
km.grid(row=1, column=0, padx=15, pady=15, sticky='nswe', columnspan=2)

informarKM = tk.Entry(fg='green', font='bold', borderwidth=1, relief='solid')
informarKM.grid(row=1, column=2, padx=15, pady=15, sticky='nsew', columnspan=5)

valor_servico = tk.Label(text="VALOR DO SERVIÇO", font='bold', fg='green', borderwidth=1, relief='solid', anchor='w')
valor_servico.grid(row=2, column=0, padx=15, pady=15, sticky='nswe', columnspan=2)

informarvalorServico = tk.Entry(fg='green', font='bold', borderwidth=1, relief='solid')
informarvalorServico.grid(row=2, column=2, padx=15, pady=15, sticky='nsew', columnspan=5)

botao_calcular = tk.Button(text="CALCULAR", font='bold', fg='green', borderwidth=1, relief='solid', command=calcular)
botao_calcular.grid(row=3, column=0, padx=15, pady=15, sticky='nsew')

valor_visita = valor_visita = tk.Label(width=80, height=10, borderwidth=1, relief='solid', anchor='w', justify='left')
valor_visita.grid(row=4, column=0, columnspan=7, padx=15, pady=15, sticky='nsew')

botao_fechar = tk.Button(text='Fechar', borderwidth=1, relief='solid', command=janela.quit)
botao_fechar.grid(row=5, column=6, padx=15, pady=15, sticky='nsew')

janela.mainloop()
