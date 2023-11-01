# Conversor de Moeda

Este é um simples conversor de moeda desenvolvido em Python usando a biblioteca CustomTkinter. O programa permite converter o valor em real brasileiro para outras moedas estrangeiras, incluindo Dólar Americano, Euro, Libra, Pesos Argentinos, Iene Japonês, Dólar Canadense, Franco Suíço, Dólar Australiano e Yuan Chinês.

## Requisitos

- Python 3.x
- Biblioteca CustomTkinter
- Biblioteca requests
- Conexão à Internet

## Como Usar

1. **Executar o Programa**: Execute o script Python em um ambiente que tenha acesso à internet.

2. **Selecione a Moeda**: Escolha a moeda para a qual deseja converter o valor em reais no menu suspenso.

3. **Informe o Valor em Real**: Digite o valor em reais no campo de entrada correspondente.

4. **Converter**: Clique no botão "Converter" para calcular o valor convertido na moeda escolhida.

5. **Resultado**: O valor convertido será exibido abaixo do botão de conversão.

## Moedas Disponíveis para Conversão

- Dólar Americano (USD)
- Euro (EUR)
- Libra (GBP)
- Pesos Argentinos (ARS)
- Iene Japonês (JPY)
- Dólar Canadense (CAD)
- Franco Suíço (CHF)
- Dólar Australiano (AUD)
- Yuan Chinês (CNY)

## Como Funciona

O programa faz uso da API da [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para obter as últimas taxas de câmbio entre o real brasileiro (BRL) e outras moedas. Após escolher a moeda e informar o valor em reais, o programa realiza a conversão usando a taxa de câmbio atual.

---

**Nota**: Certifique-se de ter uma conexão à internet ativa ao executar o programa para obter as taxas de câmbio mais recentes.

Para mais detalhes sobre como usar o CustomTkinter, consulte a documentação [aqui](https://github.com/d-rez/customtkinter).


