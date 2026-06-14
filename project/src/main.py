from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from services.task_service import TaskService

app = FastAPI(
    title="API Frigobé",
    description="Sistema de gerenciamento de pedidos",
    version="1.0.0"
)

service = TaskService()


@app.get("/")
def home():
    return {"message": "API Frigobé rodando"}


# ==========================
# LOGIN
# ==========================

@app.get("/login", response_class=HTMLResponse)
def login():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>
        <meta charset="UTF-8">
        <title>Frigobé Premium</title>

        <style>

            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, sans-serif;
            }

            body{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;

                background:
                linear-gradient(
                    135deg,
                    #000000,
                    #180000,
                    #3d0000,
                    #000000
                );

                overflow:hidden;
            }

            .box{

                width:450px;

                background:#080808;

                border:2px solid #a00000;

                border-radius:25px;

                padding:50px;

                box-shadow:
                    0 0 25px rgba(255,0,0,0.4),
                    0 0 50px rgba(255,0,0,0.2);

            }

            .logo{
                text-align:center;
                font-size:65px;
                margin-bottom:10px;
            }

            h1{
                text-align:center;
                color:white;
                font-size:48px;
                margin-bottom:10px;
                letter-spacing:2px;
            }

            .subtitle{
                text-align:center;
                color:#bdbdbd;
                margin-bottom:35px;
                font-size:16px;
            }

            input{

                width:100%;
                padding:16px;

                margin-bottom:18px;

                border:1px solid #b30000;

                border-radius:12px;

                background:#111111;

                color:white;

                font-size:15px;
            }

            input:focus{
                outline:none;
                border-color:#ff0000;
            }

            button{

                width:100%;

                padding:16px;

                border:none;

                border-radius:12px;

                background:
                linear-gradient(
                    #ff1a1a,
                    #b30000
                );

                color:white;

                font-size:18px;

                font-weight:bold;

                cursor:pointer;

                transition:0.3s;
            }

            button:hover{
                transform:scale(1.02);
                box-shadow:0 0 20px rgba(255,0,0,0.5);
            }

            .footer{
                text-align:center;
                margin-top:25px;
                color:#888;
                font-size:13px;
            }

        </style>

    </head>

    <body>

        <div class="box">

            <div class="logo">
                🐂
            </div>

            <h1>FRIGOBÉ</h1>

            <p class="subtitle">
                Sistema de Gestão Comercial
            </p>

            <form method="post" action="/login">

                <input
                    type="text"
                    name="usuario"
                    placeholder="Usuário"
                    required
                >

                <input
                    type="password"
                    name="senha"
                    placeholder="Senha"
                    required
                >

                <button type="submit">
                    Entrar
                </button>

            </form>

            <div class="footer">
                Distribuição de Carnes e Produtos Bovinos
            </div>

        </div>

    </body>

    </html>
    """


@app.post("/login")
def validar_login(
    usuario: str = Form(...),
    senha: str = Form(...)
):
    if usuario == "admin" and senha == "1234":
        return RedirectResponse(
            url="/dashboard",
            status_code=302
        )

    return HTMLResponse("""
    <h2>Usuário ou senha inválidos.</h2>
    <a href="/login">Voltar</a>
    """)


# ==========================
# DASHBOARD
# ==========================

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    total = len(service.list_orders())

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>

        <meta charset="UTF-8">

        <title>Dashboard Frigobé Premium</title>

        <style>

            *{{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial,sans-serif;
            }}

            body{{
                background:
                linear-gradient(
                    135deg,
                    #000000,
                    #180000,
                    #3d0000,
                    #000000
                );

                color:white;
                min-height:100vh;
            }}

            .header{{
                background:#080808;
                padding:30px;
                text-align:center;
                border-bottom:2px solid #b30000;
                box-shadow:0 0 20px rgba(255,0,0,0.3);
            }}

            .header h1{{
                font-size:42px;
                margin-top:10px;
                margin-bottom:10px;
            }}

            .header p{{
                color:#d1d5db;
            }}

            .container{{
                max-width:1200px;
                margin:auto;
                padding:50px 20px;
            }}

            .cards{{
                display:grid;
                grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
                gap:25px;
            }}

            .card{{
                background:#0b0b0b;
                padding:30px;
                border-radius:20px;
                text-align:center;
                border:1px solid #b30000;
                box-shadow:0 0 20px rgba(255,0,0,0.25);
            }}

            .card h2{{
                margin-bottom:15px;
                color:white;
            }}

            .card h1{{
                font-size:50px;
                color:#ff4d4d;
                margin-bottom:10px;
            }}

            .card p{{
                color:#d1d5db;
            }}

            .btn{{
                display:inline-block;
                margin-top:15px;
                padding:12px 22px;
                border-radius:10px;
                text-decoration:none;
                color:white;
                font-weight:bold;

                background:
                linear-gradient(
                    #ff1a1a,
                    #b30000
                );
            }}

            .btn:hover{{
                transform:scale(1.05);
            }}

            footer{{
                text-align:center;
                padding:40px;
                color:#d1d5db;
            }}

        </style>

    </head>

    <body>

        <div class="header">

            <p>
                Carnes selecionadas • Qualidade garantida • Entrega rápida
            </p>

            <h1>🐂 FRIGOBÉ PREMIUM</h1>

            <p>
                Distribuição de Carnes e Produtos Bovinos
            </p>

        </div>

        <div class="container">

            <div class="cards">

                <div class="card">

                    <h2>🥩 Pedidos</h2>

                    <h1>{total}</h1>

                    <p>
                        Total de pedidos cadastrados
                    </p>

                </div>

                <div class="card">

                    <h2>📄 API</h2>

                    <p>
                        Documentação completa da API
                    </p>

                    <a class="btn" href="/docs">
                        Abrir
                    </a>

                </div>

                <div class="card">

                    <h2>📦 Gerenciar Pedidos</h2>

                    <p>
                        Cadastro, edição e controle
                    </p>

                    <a class="btn" href="/pedidos">
                        Gerenciar
                    </a>

                </div>

                <div class="card">

                    <h2>🚪 Sair</h2>

                    <p>
                        Retornar ao login
                    </p>

                    <a class="btn" href="/login">
                        Sair
                    </a>

                </div>

            </div>

        </div>

        <footer>
            © 2026 FRIGOBÉ PREMIUM | Sistema de Gestão Comercial
        </footer>

    </body>

    </html>
    """


# ==========================
# TELA DE PEDIDOS
# ==========================

@app.get("/pedidos", response_class=HTMLResponse)
def tela_pedidos():

    pedidos = service.list_orders()

    linhas = ""

    for pedido in pedidos:

       linhas += f"""
<tr>
    <td>{pedido.id}</td>
    <td>{pedido.customer}</td>
    <td>{pedido.product}</td>
    <td>{pedido.status}</td>

    <td>

        <form action="/pedidos/concluir/{pedido.id}" method="post" style="display:inline;">
            <button type="submit">
                ✅ Concluir
            </button>
        </form>

        <form action="/pedidos/excluir/{pedido.id}" method="post" style="display:inline;">
            <button type="submit">
                ❌ Excluir
            </button>
        </form>

    </td>

</tr>
"""

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>

        <meta charset="UTF-8">

        <title>Pedidos - Frigobé</title>

        <style>

            body{{
               background:#2b0f0f;
                color:white;
                font-family:Arial;
                padding:30px;
            }}

            .box{{
                background:#4a1d1d;
                padding:30px;
                border-radius:15px;
            }}

            h1{{
                margin-bottom:20px;
            }}

            table{{
                width:100%;
                border-collapse:collapse;
                margin-top:20px;
            }}

            th,td{{
                border:1px solid #334155;
                padding:12px;
                text-align:center;
            }}

            th{{
                background:#111827;
            }}

            a{{
                color:white;
                text-decoration:none;
            }}

        </style>

    </head>

    <body>

        <div class="box">

            <h1> Pedidos Cadastrados</h1>

            <form action="/pedidos/criar" method="post">

    <input
        type="text"
        name="customer"
        placeholder="Nome do Cliente"
        required
    >

    <input
        type="text"
        name="product"
        placeholder="Produto"
        required
    >

    <button type="submit">
        Cadastrar Pedido
    </button>

</form>

<br>

          <table>

    <tr>
        <th>ID</th>
        <th>Cliente</th>
        <th>Produto</th>
        <th>Status</th>
        <th>Ações</th>
    </tr>

    {linhas}

</table>

            <br>

            <a href="/dashboard">
                ← Voltar ao Dashboard
            </a>

        </div>

    </body>

    </html>
    """
@app.post("/pedidos/criar")
def criar_pedido(
    customer: str = Form(...),
    product: str = Form(...)
):

    service.create_order(customer, product)

    return RedirectResponse(
        url="/pedidos",
        status_code=302
    )

@app.post("/pedidos/concluir/{order_id}")
def concluir_pedido(order_id: int):

    service.complete_order(order_id)

    return RedirectResponse(
        url="/pedidos",
        status_code=302
    )


@app.post("/pedidos/excluir/{order_id}")
def excluir_pedido(order_id: int):

    service.delete_order(order_id)

    return RedirectResponse(
        url="/pedidos",
        status_code=302
    )



@app.post("/orders")
def create_order(customer: str, product: str):

    order = service.create_order(customer, product)

    return {
        "id": order.id,
        "customer": order.customer,
        "product": order.product,
        "status": order.status
    }


@app.get("/orders")
def get_orders():

    return [
        {
            "id": order.id,
            "customer": order.customer,
            "product": order.product,
            "status": order.status
        }
        for order in service.list_orders()
    ]


@app.put("/orders/{order_id}/complete")
def complete_order(order_id: int):

    order = service.complete_order(order_id)

    if order:
        return {
            "id": order.id,
            "customer": order.customer,
            "product": order.product,
            "status": order.status
        }

    return {"erro": "Pedido não encontrado"}


@app.delete("/orders/{order_id}")
def delete_order(order_id: int):

    return {
        "deleted": service.delete_order(order_id)
    }