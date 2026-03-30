# 🥩 Sistema Frigobé - API de Gestão

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de ajudar um pequeno negócio local, a **Frigobé – Casa de Carnes e Conveniência**, a melhorar sua organização e controle das operações do dia a dia.

Atualmente, muitos processos são feitos de forma manual, como anotações em papel e controle informal de pedidos. Isso acaba gerando erros, perda de informações e dificuldade no crescimento do negócio.

A proposta dessa API é centralizar essas informações em um sistema simples, prático e funcional.

---

## 🎯 Objetivo

Criar uma API que permita:

* Cadastro de pedidos
* Organização das vendas
* Controle básico de informações
* Estrutura inicial para evolução do sistema

---

## ⚙️ Tecnologias utilizadas

* **Python**
* **FastAPI**
* **Uvicorn**

---

## 🧠 Paradigmas de Programação

Este projeto utiliza diferentes paradigmas:

### 🔹 Orientado a Objetos (POO)

Utilizado para representar entidades do sistema, como pedidos.

### 🔹 Estruturado

Aplicado no fluxo lógico das operações, como criação e listagem.

### 🔹 Funcional (parcial)

Usado em funções simples de processamento de dados.

---

## 📁 Estrutura do Projeto

```
src/
 ├── models/
 ├── services/
 ├── utils/
 └── main.py
```

* **models** → representa os dados (ex: pedido)
* **services** → regras de negócio
* **utils** → funções auxiliares
* **main.py** → ponto de entrada da aplicação

---

## 🚀 Como executar o projeto

1. Instalar dependências:

```
python -m pip install -r requirements.txt
```

2. Rodar a API:

```
python -m uvicorn main:app --reload
```

3. Acessar no navegador:

```
http://127.0.0.1:8000/docs
```

---

## 📊 Funcionalidades atuais (MVP)

* Criar pedidos
* Listar pedidos
* Marcar como concluído
* Remover pedidos

---

## 🔮 Possíveis melhorias futuras

* Cadastro de clientes
* Controle de estoque
* Relatórios de vendas
* Integração com banco de dados

---

## 👨‍💻 Autor

Projeto desenvolvido como atividade acadêmica (TED 2)
Curso de Sistemas de Informação

---

## 📌 Observação

Este sistema representa um **MVP (Produto Mínimo Viável)**, focado em resolver problemas reais de forma simples e eficiente.
