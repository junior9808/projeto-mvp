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
        <title>Login Frigobé</title>

        <style>
            body{
                background:#111827;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                font-family:Arial;
            }

            .box{
                background:#1f2937;
                padding:40px;
                border-radius:15px;
                width:350px;
                box-shadow:0 0 20px rgba(0,0,0,0.5);
            }

            h1{
                color:white;
                text-align:center;
                margin-bottom:30px;
            }

            input{
                width:100%;
                padding:12px;
                margin-bottom:15px;
                border:none;
                border-radius:8px;
                box-sizing:border-box;
            }

            button{
                width:100%;
                padding:12px;
                border:none;
                border-radius:8px;
                background:#22c55e;
                color:white;
                font-size:16px;
                cursor:pointer;
            }

            button:hover{
                background:#16a34a;
            }

            p{
                color:#cbd5e1;
                text-align:center;
                margin-top:15px;
            }
        </style>

    </head>

    <body>

        <div class="box">

            <h1>🥩 Frigobé</h1>

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

            <p>Sistema de Gerenciamento de Pedidos</p>

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
        <title>Dashboard Frigobé</title>

        <style>

            *{{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, sans-serif;
            }}

            body{{
                background:#0f172a;
                color:white;
            }}

            .header{{
                background:#111827;
                padding:25px;
                text-align:center;
            }}

            .header h1{{
                font-size:32px;
            }}

            .header p{{
                color:#94a3b8;
                margin-top:8px;
            }}

            .container{{
                max-width:1200px;
                margin:auto;
                padding:40px;
            }}

            .cards{{
                display:grid;
                grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
                gap:20px;
            }}

            .card{{
                background:#1e293b;
                padding:30px;
                border-radius:15px;
                text-align:center;
            }}

            .card h2{{
                margin-bottom:15px;
            }}

            .btn{{
                display:inline-block;
                margin-top:15px;
                padding:12px 20px;
                background:#22c55e;
                color:white;
                text-decoration:none;
                border-radius:8px;
            }}

            .btn:hover{{
                background:#16a34a;
            }}

            footer{{
                text-align:center;
                padding:30px;
                color:#94a3b8;
            }}
        </style>

    </head>

    <body>

        <div class="header">
            <h1>🥩 Frigobé</h1>
            <p>Sistema de Gerenciamento de Pedidos</p>
        </div>

        <div class="container">

            <div class="cards">

                <div class="card">
                    <h2>📦 Pedidos</h2>
                    <h1>{total}</h1>
                    <p>Total de pedidos cadastrados</p>
                </div>

                <div class="card">
                    <h2>📄 API</h2>
                    <p>Documentação completa da API</p>
                    <a class="btn" href="/docs">
                        Abrir
                    </a>
                </div>

                <div class="card">
                    <h2>📋 Pedidos</h2>
                    <p>Visualizar pedidos cadastrados</p>
                    <a class="btn" href="/orders">
                        Ver Pedidos
                    </a>
                </div>

                <div class="card">
                    <h2>🚪 Sair</h2>
                    <p>Retornar ao login</p>
                    <a class="btn" href="/login">
                        Sair
                    </a>
                </div>

            </div>

        </div>

        <footer>
            Desenvolvido por Dhonantan dos Santos e Arthur Cirqueira
        </footer>

    </body>
    </html>
    """


# ==========================
# PEDIDOS
# ==========================

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