# Como Executar o Projeto

Existem duas maneiras de executar esta aplicação:

## 1. A partir do Código-Fonte (Qualquer Sistema Operacional)

Este é o método recomendado para executar a aplicação em qualquer sistema operacional (Windows, macOS, Linux).

### Pré-requisitos

1.  **Python 3:** Tenha o Python 3.x instalado.
2.  **Ambiente Virtual:** Ative o ambiente virtual que foi criado.
    ```bash
    python3 -m venv venv && source venv/bin/activate
    ```
3.  **Instale as dependências:** Com o ambiente ativado, instale as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```
4.  **`ffmpeg`:** Esta ferramenta é necessária para a conversão de áudio e vídeo. Você deve instalá-la e garantir que ela esteja acessível no PATH do seu sistema.

### Executando a Aplicação

Após instalar os pré-requisitos, execute o script `main.py`:

```bash
python main.py
```

Isso iniciará a interface gráfica do usuário.

## 2. Usando o Executável (Apenas para Windows)

Um executável pré-empacotado está disponível para usuários do Windows.

### Executando a Aplicação

Simplesmente dê um duplo clique no arquivo `main.exe` ou execute-o a partir de um prompt de comando:

```bash
./main.exe
```
