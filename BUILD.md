# Gerando o Executável

Este documento explica como gerar a versão executável da aplicação usando a ferramenta **PyInstaller**.

## Nota Importante: Sistema Operacional

Para gerar um arquivo `.exe` para **Windows**, você **obrigatoriamente** deve executar os comandos em um sistema operacional **Windows**.

Se você executar o PyInstaller no Linux ou macOS, ele criará um executável para essas plataformas, e não um `.exe` para Windows.

## Passos para Gerar o Executável

1.  **Prepare o Ambiente:**
    Certifique-se de que você tem o Python instalado e o ambiente virtual criado, conforme descrito no arquivo `RUN.md`.

2.  **Ative o Ambiente Virtual:**
    
    No Windows:
    ```bash
    .\venv\Scripts\activate
    ```
    No Linux ou macOS:
    ```bash
    source venv/bin/activate
    ```

3.  **Instale as Dependências de Geração:**
    Com o ambiente ativado, instale as bibliotecas necessárias para o projeto e também o `pyinstaller`.
    ```bash
    pip install -r requirements.txt
    pip install pyinstaller
    ```

4.  **Execute o PyInstaller:**
    Ainda no terminal, na pasta raiz do projeto, execute o seguinte comando:
    ```bash
    pyinstaller --onefile --windowed --name "pyYtbMp3" main.py
    ```
    *   `--onefile`: Agrupa todo o necessário em um único arquivo executável.
    *   `--windowed`: Impede que uma janela de console (terminal) seja aberta ao executar a aplicação.
    *   `--name "pyYtbMp3"`: Define o nome do arquivo de saída.

5.  **Encontre o Executável:**
    Após a finalização do processo, o arquivo `pyYtbMp3.exe` estará localizado dentro de uma nova pasta chamada `dist`.
