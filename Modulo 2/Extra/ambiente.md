# Passo a passo - Criar ambiente de desenvolvimento

## Criar ambiente virtual

    1. Criar uma pasta
    2. entrar na pasta e como o botão direito do mouse "Abrir no terminal"
    3. Criar um venv(ambiente virtual)
        python -m venv nomedovenv
    4. Ativar o venv
        .\nomedovenv\Scripts\activate
    5. Instalar bibliotecas para a aula do dia  
        Aula de hoje "PyAutoGui"   
            pip intall pyautogui

    6. Abrir o vscode
        code .

## Observações

1. Caso Não tenha o vscode intalado:

[site oficial do visual studio code](https://code.visualstudio.com/)

1.1 Após instalar o vscode, istalar as extenções:

    Python
    Jupyter
    Material Icon
    Rainbown CSV
    Dracula
    Html CSS Support

2. Caso ao ativar o venv apresentae uma mensagem de erro:

    rodar o comando

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Curr

## Criar arquivo Jupyter

    1. Criar arquivo do Jupyter notebook

        nome.ipynb

    2. Clicar em "Select Kernel", "python eviroments" e selecionar o seu venv (ele vai te recomendar )


    3. Rodar um print qualquer ex. print('oi')
        o visual code vai pra intalar um kerel. clicar em intalar   