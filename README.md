# 🥋 DashBoard Jiu Jitsu 🥋

Este é um sistema simples para gerenciar alunos e aulas de Jiu Jitsu, desenvolvido com [Flet](https://flet.dev/) e consumindo minha api(https://github.com/CauZy-Goes/Academia_JiuJitsu_API) API via `requests`.

## 📌 Funcionalidades

- **Cadastro de alunos**: Nome, Email, Faixa e Data de Nascimento.
- **Listagem de alunos**: Visualização de todos os alunos cadastrados.
- **Registro de aulas realizadas**: Adiciona aulas ao histórico do aluno.
- **Consulta de progresso**: Verifica o número total de aulas e quantas são necessárias para a próxima faixa.
- **Atualização de dados do aluno**: Permite alterar nome, email, faixa e data de nascimento.

## 📸 Imagens do Projeto

### Cadastro de Aluno
![Tela Cadastro](https://github.com/CauZy-Goes/Academia_JiuJitsu/blob/main/JiuJitsu_imgs/cadastro.png)


### Listar Alunos
![Tela Lista](https://github.com/CauZy-Goes/Academia_JiuJitsu/blob/main/JiuJitsu_imgs/Listar%20aluno.png)


### Adicionar Aulas
![Tela Aulas](https://github.com/CauZy-Goes/Academia_JiuJitsu/blob/main/JiuJitsu_imgs/aula_realizada.png)

## Ver Progresso Do Aluno
![Tela Progresso](https://github.com/CauZy-Goes/Academia_JiuJitsu/blob/main/JiuJitsu_imgs/Progresso%20do%20aluno.png)

## Fazer update no aluno
![Tela update](https://github.com/CauZy-Goes/Academia_JiuJitsu/blob/main/JiuJitsu_imgs/Atualizar%20aluno.png)


## 🛠️ Tecnologias Utilizadas

- **Python**
- **Flet**
- **Requests**
- **API REST**

## 🚀 Melhorias Futuras

- Validação de dados no frontend.
- Melhor experiência de usuário com feedbacks visuais.
- Implementação de autenticação para segurança.
- Deploy da API e do frontend para acesso online.


## 🛠️ Instalação e Execução

1. Clone este repositório:

   ```sh
   git clone https://github.com/seu-usuario/dashboard-jiujitsu.git
   cd dashboard-jiujitsu
   ```

2. Crie um ambiente virtual e ative-o:

   ```sh
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No macOS/Linux:
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Configure a URL da API no código: Abra o arquivo `main.py` e edite a variável `API_BASE_URL`, substituindo pelo endereço correto da API:

   ```python
   API_BASE_URL = "SUA_URL_DA_API_AQUI"
   ```

   **URL da API utilizada:** [https://github.com/CauZy-Goes/Academia_JiuJitsu_API]

5. Execute o aplicativo:

   ```sh
   python main.py
   ```
