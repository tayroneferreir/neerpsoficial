from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from flask_mail import Mail, Message

app = Flask(__name__)




@app.route('/')
def Login():
    return render_template('login.html')
    

@app.route('/home')
def Home():
    return render_template('index.html')


@app.route('/dados')
def Dados():
    data = {
        'Ano': [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1],
        'Ingressos': [30, 27, 31, 28, 30, 34, 33, 39, 34, 33, 26]
    }
    df = pd.DataFrame(data)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.plot(df['Ano'], df['Ingressos'], marker='o')  # Plota o gráfico de linha
    plt.title('Ingressos no curso Noturno')  # Define o título do gráfico
    plt.xlabel('Ano')  # Define o rótulo do eixo x
    plt.ylabel('Ingressos')  # Define o rótulo do eixo y
    plt.grid(True)  # Adiciona uma grade ao gráfico


    # Salva o gráfico em um objeto BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_b64 = base64.b64encode(img.getvalue()).decode()

    #Ingresso curso DIURNO

    data = {
        'Ano': [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1],
        'Ingressos': [33, 24, 31, 20, 22, 33, 32, 33, 33, 25, 20]
    }
    df = pd.DataFrame(data)

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.plot(df['Ano'], df['Ingressos'], marker='o')  # Plota o gráfico de linha
    plt.title('Ingressos no curso Diurno')  # Define o título do gráfico
    plt.xlabel('Ano')  # Define o rótulo do eixo x
    plt.ylabel('Ingressos')  # Define o rótulo do eixo y
    plt.grid(True)  # Adiciona uma grade ao gráfico


    # Salva o gráfico em um objeto BytesIO
    img2 = io.BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    img_b64_g2 = base64.b64encode(img2.getvalue()).decode()



    

   
    
    

     ##################Trancamentos NOTURNO#########################
    # Criando o gráfico de barras Cancelamento de Matrícula
    fig, ax = plt.subplots(figsize=(20, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    tresreprovacoes = [4, 4, 4, 3, 6, 2, 3, 0, 1, 3, 0]
    ingressonomesmocurso = [6, 2, 5, 4, 4, 5, 3, 1, 1, 0, 0]
    ingressooutrocurso = [2, 1, 0, 0, 2, 1, 2, 1, 0, 0, 0]
    reprovouporfalta = [15, 11, 13, 10, 9, 4, 5, 8, 0, 2, 0]  
    x = range(len(categorias))
    largura = 0.20

    ax.bar([p - 1.5*largura for p in x], tresreprovacoes, largura, label='Três Reprovações', color='lightblue')
    ax.bar([p - 0.5*largura for p in x], ingressonomesmocurso, largura, label='Ingresso no Mesmo Curso', color='green')
    ax.bar([p + 0.5*largura for p in x], ingressooutrocurso, largura, label='Ingresso em Outro Curso', color='yellow')
    ax.bar([p + 1.5*largura for p in x], reprovouporfalta, largura, label='Reprovado por Falta', color='purple')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Trancamentos Noturno')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64trancamentonoturno = base64.b64encode(output.getvalue()).decode('utf-8')


    ##################Trancamentos DIURNO#########################
    # Criando o gráfico de barras Cancelamento de Matrícula
    fig, ax = plt.subplots(figsize=(20, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    tresreprovacoes = [3, 6, 0, 2, 4, 2, 3, 2, 2, 0, 7]
    ingressonomesmocurso = [3, 3, 7, 4, 1, 3, 2, 1, 0, 1, 0]
    ingressooutrocurso = [6, 0, 2, 2, 2, 4, 1, 4, 1, 1, 0]
    reprovouporfalta = [10, 8, 12, 2, 2, 3, 7, 4, 1, 6, 0]  
    x = range(len(categorias))
    largura = 0.20

    ax.bar([p - 1.5*largura for p in x], tresreprovacoes, largura, label='Três Reprovações', color='lightblue')
    ax.bar([p - 0.5*largura for p in x], ingressonomesmocurso, largura, label='Ingresso no Mesmo Curso', color='green')
    ax.bar([p + 0.5*largura for p in x], ingressooutrocurso, largura, label='Ingresso em Outro Curso', color='yellow')
    ax.bar([p + 1.5*largura for p in x], reprovouporfalta, largura, label='Reprovado por Falta', color='purple')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Trancamentos Diurno')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64trancamentodiurno = base64.b64encode(output.getvalue()).decode('utf-8')

   




    ###################
    

    #Gráfico para homem e mulher Diurno

    fig, ax = plt.subplots(figsize=(10, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    homens = [22, 10, 21, 16, 16, 23, 19, 24, 19, 16, 9]
    mulheres = [11, 14, 10, 4, 6, 10, 13, 9, 14, 9, 11]
    x = range(len(categorias))
    largura = 0.30

    ax.bar([p - largura/2 for p in x], homens, largura, label='Homens', color='lightblue')
    ax.bar([p + largura/2 for p in x], mulheres, largura, label='Mulheres', color='green')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Ingresso Homens e Mulheres Diurno ')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()   
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64 = base64.b64encode(output.getvalue()).decode('utf-8')

     #Gráfico para homem e mulher Noturno

    fig, ax = plt.subplots(figsize=(10, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    homens = [22, 10, 21, 16, 16, 23, 19, 24, 19, 16, 9]
    mulheres = [10, 10, 7, 8, 7, 11, 11, 9, 12, 18, 10]
    x = range(len(categorias))
    largura = 0.30

    ax.bar([p - largura/2 for p in x], homens, largura, label='Homens', color='lightblue')
    ax.bar([p + largura/2 for p in x], mulheres, largura, label='Mulheres', color='green')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Ingresso Homens e Mulheres Noturno ')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()   
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64_g2 = base64.b64encode(output.getvalue()).decode('utf-8')

    #############Tipos de Escola Noturno##############
    fig, ax = plt.subplots(figsize=(10, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    publica_e_privada = [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
    escola_privada = [0, 0, 1, 1, 1, 1, 3, 1, 1, 1, 0]
    escola_publica = [28, 27, 29, 27, 28, 33, 29, 38, 32, 32, 26]
    x = range(len(categorias))
    largura = 0.30

    ax.bar([p - largura for p in x], publica_e_privada, largura, label='Pública e Privada', color='lightblue')
    ax.bar(x, escola_privada, largura, label='Escola Privada', color='green')
    ax.bar([p + largura for p in x], escola_publica, largura, label='Escola Pública', color='yellow')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Escolas de Ingresso Noturno')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64escolas = base64.b64encode(output.getvalue()).decode('utf-8')

    ############Tipos de Escola DIURNO####################

    fig, ax = plt.subplots(figsize=(10, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    publica_e_privada = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    escola_privada = [4, 4, 2, 5, 3, 5, 6, 3, 2, 1, 0]
    escola_publica = [28, 19, 28, 15, 18, 28, 26, 29, 30, 23, 20]
    x = range(len(categorias))
    largura = 0.30

    ax.bar([p - largura for p in x], publica_e_privada, largura, label='Pública e Privada', color='lightblue')
    ax.bar(x, escola_privada, largura, label='Escola Privada', color='green')
    ax.bar([p + largura for p in x], escola_publica, largura, label='Escola Pública', color='yellow')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Escolas de Ingresso Diurno')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64escolasdiurno = base64.b64encode(output.getvalue()).decode('utf-8')

    ###########################################

    ############Estado Civil NOTURNO##############

    fig, ax = plt.subplots(figsize=(14, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    casado = [5, 5, 2, 2, 3, 3, 2, 5, 1, 2, 2]
    solteiro = [25, 22, 28, 21, 26, 30, 31, 33, 32, 29, 24]
    divorciado = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    nao_declarado = [0, 0, 0, 5, 1, 1, 0, 1, 1, 2, 0]  
    x = range(len(categorias))
    largura = 0.30

    ax.bar([p - 1.5*largura for p in x], casado, largura, label='Casado', color='lightblue')
    ax.bar([p - 0.5*largura for p in x], solteiro, largura, label='Solteiro', color='green')
    ax.bar([p + 0.5*largura for p in x], divorciado, largura, label='Divorciado', color='yellow')
    ax.bar([p + 1.5*largura for p in x], nao_declarado, largura, label='Não Declarado', color='purple')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Estado Civil Noturno')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64estadocivil = base64.b64encode(output.getvalue()).decode('utf-8')

    ############Estado Civil DIURNO##############

    fig, ax = plt.subplots(figsize=(14, 6))
    categorias = [2012.1, 2013.1, 2014.1, 2015.1, 2016.1, 2017.1, 2018.1, 2019.1, 2020.1, 2021.1, 2022.1]
    casado = [5, 1, 3, 2, 0, 2, 0, 0, 1, 0, 0]
    solteiro = [28, 23, 28, 18, 22, 31, 32, 33, 32, 23, 19]
    divorciado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nao_declarado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1]  
    x = range(len(categorias))
    largura = 0.30

    ax.bar([p - 1.5*largura for p in x], casado, largura, label='Casado', color='lightblue')
    ax.bar([p - 0.5*largura for p in x], solteiro, largura, label='Solteiro', color='green')
    ax.bar([p + 0.5*largura for p in x], divorciado, largura, label='Divorciado', color='yellow')
    ax.bar([p + 1.5*largura for p in x], nao_declarado, largura, label='Não Declarado', color='purple')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Estado Civil Diurno')
    ax.set_xticks(x)
    ax.set_xticklabels(categorias)
    ax.legend()

    # Converter o gráfico para base64
    output = io.BytesIO()
    plt.savefig(output, format='png')
    plt.close(fig)
    output.seek(0)
    img_hm_b64estadocivildiurno = base64.b64encode(output.getvalue()).decode('utf-8')

    # Renderiza o template HTML
    return render_template('dados.html', img_data=img_b64, img_hm_b64=img_hm_b64, img_b64_g2=img_b64_g2, img_hm_b64_g2=img_hm_b64_g2, img_hm_b64escolas=img_hm_b64escolas, img_hm_b64estadocivil=img_hm_b64estadocivil, img_hm_b64estadocivildiurno=img_hm_b64estadocivildiurno, img_hm_b64trancamentodiurno=img_hm_b64trancamentodiurno, img_hm_b64trancamentonoturno =img_hm_b64trancamentonoturno, img_hm_b64escolasdiurno=img_hm_b64escolasdiurno)

@app.route('/contatos')
def Contatos():
    return render_template('contatos.html')


    
    

if __name__ == "__main__":
    app.run(debug=True)