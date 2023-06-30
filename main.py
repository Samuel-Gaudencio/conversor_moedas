import customtkinter as ctk
import json
import requests


def cotacao():
    if opmoedas.get() == 'Dólar Americano':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-USD'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLUSD']['ask']
        return float(valor)

    elif opmoedas.get() == 'Euro':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-EUR'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLEUR']['ask']
        return float(valor)
    elif opmoedas.get() == 'Libra':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-GBP'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLGBP']['ask']
        return float(valor)
    elif opmoedas.get() == 'Pesos Argentino':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-ARS'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLARS']['ask']
        return float(valor)
    elif opmoedas.get() == 'Iene Japones':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-JPY'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLJPY']['ask']
        return float(valor)
    elif opmoedas.get() == 'Dólar Canadense':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-CAD'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLCAD']['ask']
        return float(valor)
    elif opmoedas.get() == 'Franco Suiço':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-CHF'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLCHF']['ask']
        return float(valor)
    elif opmoedas.get() == 'Dólar Australiano':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-AUD'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLAUD']['ask']
        return float(valor)
    elif opmoedas.get() == 'Yuan Chinês':
        url_api = f'https://economia.awesomeapi.com.br/last/BRL-CNY'
        req = requests.get(url_api)
        cota = json.loads(req.content)
        valor = cota['BRLCNY']['ask']
        return float(valor)


def converte():
    v_covertido.configure(text=f'{cotacao() * float(e_valor.get()):.2f}')


root = ctk.CTk()
root.geometry('400x400')
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

margin = ctk.CTkLabel(root, text=' ')
margin.pack(pady=5)

texto = ctk.CTkLabel(root, text='Selecione a moeda e faça a converção', font=('Montserrat', 20, 'bold'))
texto.pack()

opmoedas = ctk.CTkOptionMenu(root, values=['Dólar Americano', 'Euro', 'Libra', 'Pesos Argentino', 'Iene Japones', 'Dólar Canadense',
                                           'Franco Suiço', 'Dólar Australiano', 'Yuan Chinês'])
opmoedas.pack(pady=10)

e_valor = ctk.CTkEntry(root, placeholder_text='Informe o valor em real', font=('Montserrat', 10, 'bold'))
e_valor.pack()

b_converter = ctk.CTkButton(root, text='Converter', font=('Montserrat', 16, 'bold'), command=converte)
b_converter.pack(pady=10)

v_covertido = ctk.CTkLabel(root, text='', font=('Montserrat', 20, 'bold'))
v_covertido.pack()

root.mainloop()