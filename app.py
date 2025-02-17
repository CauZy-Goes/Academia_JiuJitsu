import flet as ft
import requests

# URL base da API – ajuste conforme necessário
API_BASE_URL = "http://127.0.0.1:8000/api"

def main(page: ft.Page):
    page.title = "Exemplo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #Criar Aluno

    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")
    create_result = ft.Text()


    def criar_aluno_click(e):
        payload = {
            "nome": nome_field.value,
            "email": email_field.value,
            "faixa": faixa_field.value,
            "data_nascimento": data_nascimento_field.value,
        }
        try:
            response = requests.post(API_BASE_URL + "/", json=payload)
            if response.status_code == 200:
                aluno = response.json()
                create_result.value = f"Aluno criado: {aluno}"
            else:
                create_result.value = f"Erro: {response.text}"
        except Exception as ex:
            create_result.value = f"Exceção: {ex}"
        page.update()
    

    create_button = ft.ElevatedButton(text="Criar Aluno", on_click=criar_aluno_click)

    #Listar alunos

    criar_aluno_tab = ft.Column(
        [
            nome_field,
            email_field,
            faixa_field,
            data_nascimento_field,
            create_result,
            create_button
        ],
        scroll=True
    )

    students_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Email")),
            ft.DataColumn(ft.Text("Faixa")),
            ft.DataColumn(ft.Text("Data Nascimento")),
        ],
        rows=[],
    )
    list_result = ft.Text()

    def listar_alunos_click(e):
        try:
            response = requests.get(API_BASE_URL + "/alunos/")
            if response.status_code == 200:
                alunos = response.json()

                # Limpa as linhas anteriores
                students_table.rows.clear()

                for aluno in alunos:
                    row = ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(aluno.get("nome", ""))),
                            ft.DataCell(ft.Text(aluno.get("email", ""))),
                            ft.DataCell(ft.Text(aluno.get("faixa", ""))),
                            ft.DataCell(ft.Text(aluno.get("data_nascimento", ""))),
                        ]
                    )
                    students_table.rows.append(row)
                list_result.value = f"{len(alunos)} alunos encontrados."
            else:
                list_result.value = f"Erro: {response.text}"
        except Exception as ex:
            list_result.value = f"Exceção: {ex}"
        page.update()

    list_button = ft.ElevatedButton(text="Listar Alunos", on_click=listar_alunos_click)

    listar_alunos_tab = ft.Column([list_button, students_table, list_result], scroll=True)



    #adicionar aulas

    email_aula_field = ft.TextField(label="Email do Aluno")
    qtd_field = ft.TextField(label="Quantidade de Aulas", value="1")
    aula_result = ft.Text()

    def marcar_aula_click(e):
        try:
            qtd = int(qtd_field.value)
            payload = {
                "qtd": qtd,
                "email_aluno": email_aula_field.value,
            }

            response = requests.post(API_BASE_URL + "/aula_realizada/", json=payload)

            if response.status_code == 200:
                # A API retorna uma mensagem de sucesso
                mensagem = response.json()  # pode ser uma string ou objeto
                aula_result.value = f"Sucesso: {mensagem}"
            else:
                aula_result.value = f"Erro: {response.text}"
        except Exception as ex:
            aula_result.value = f"Exceção: {ex}"

        page.update()

    aula_button = ft.ElevatedButton(text="Marcar Aula Realizada", on_click=marcar_aula_click)
    aula_tab = ft.Column([email_aula_field, qtd_field, aula_button, aula_result], scroll=True)

    ##Progresso do aluno

    email_progress_field = ft.TextField(label="Email do Aluno")
    progress_result = ft.Text()

    def consultar_progresso_click(e):
        try:
            email = email_progress_field.value
            response = requests.get(
                API_BASE_URL + "/progresso_aluno/", params={"email_aluno": email}
            )
            if response.status_code == 200:
                progress = response.json()
                progress_result.value = (
                    f"Nome: {progress.get('nome', '')}\n"
                    f"Email: {progress.get('email', '')}\n"
                    f"Faixa Atual: {progress.get('faixa', '')}\n"
                    f"Aulas Totais: {progress.get('total_aulas', 0)}\n"
                    f"Aulas necessárias para a próxima faixa: {progress.get('aulas_necessarias_para_proxima_faixa', 0)}"
                )
            else:
                progress_result.value = f"Erro: {response.text}"
        except Exception as ex:
            progress_result.value = f"Exceção: {ex}"
        page.update()

    progress_button = ft.ElevatedButton(text="Consultar Progresso", on_click=consultar_progresso_click)
    progresso_tab = ft.Column([email_progress_field, progress_button, progress_result], scroll=True)


    ## tabs

    tabs = ft.Tabs (
        selected_index=0,
        tabs=[
            ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
            ft.Tab(text="Listar Aluno", content=listar_alunos_tab),
            ft.Tab(text="Aula realizada", content=aula_tab),
            ft.Tab(text="Progresso Do Aluno", content=progresso_tab),

        ]
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
