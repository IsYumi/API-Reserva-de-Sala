# 📅 API de Reserva de Salas

Sistema desenvolvido para gerenciamento de reservas de salas, integrando com um microsserviço de gestão escolar.

---

## 📅 Descrição da API

A API é composta por dois microsserviços principais:

* **Gestão Escolar**

  * Responsável pelo cadastro, listagem, edição e exclusão de turmas.
  * Expõe endpoints REST para acesso e manipulação das informações escolares.

* **API de Reservas de Salas**

  * Permite criar, consultar, editar e deletar reservas vinculadas a turmas.
  * Valida a existência da turma na Gestão Escolar antes de criar uma reserva.

---

## 📅 Instruções de Execução (com Docker)

### ✅ Requisitos

* Docker instalado: [https://www.docker.com/](https://www.docker.com/)

### ✅ Executando cada serviço manualmente

#### 1. Navegue até o diretório do projeto

```bash
cd /caminho/para/Reserva-de-salas-flask
```

#### 2. Crie a imagem Docker

```bash
docker build -t reserva-salas-api .
```

#### 3. Execute o container

```bash
docker run -p 5001:5001 reserva-salas-api
```

> Repita esse processo para a API de Gestão Escolar (em outro diretório, com outra imagem e porta como 5000).

---

## 🛠️ Arquitetura da Aplicação

```
reserva-de-salas-flask/
├── app.py               # Inicializa a aplicação Flask
├── reserva_model.py    # Modelo de dados da reserva (SQLAlchemy)
├── reserva_route.py    # Endpoints da API de reservas
├── database.py         # Configuração do banco de dados
├── config.py           # Parâmetros de ambiente (como URI do DB)
├── requirements.txt    # Dependências da aplicação
└── Dockerfile          # Instruções para montar o container Docker
```

---

## 🛂 Microsserviços e Integração

### 📆 Gestão Escolar (porta 5000)

* `GET /turma/<id>` → Buscar turma
* `POST /turma` → Criar nova turma
* `PUT /turma/<id>` → Atualizar turma
* `DELETE /turma/<id>` → Remover turma

### 📖 API de Reservas (porta 5001)

* `POST /reservas` → Criar nova reserva (valida com a Gestão Escolar)
* `GET /reservas` → Listar todas as reservas
* `GET /reservas/<id>` → Detalhar uma reserva
* `PUT /reservas/<id>` → Atualizar uma reserva
* `DELETE /reservas/<id>` → Deletar uma reserva
* `DELETE /reservas/limpar_orfaos` → Remove reservas sem turma válida

### 🛠️ Integração entre os Serviços

A API de Reservas realiza chamadas HTTP para a API de Gestão Escolar para:

* Validar existência de turmas ao criar/editar reservas
* Obter dados detalhados da turma para incluir na resposta
* Receber notificações de exclusão de turmas e remover reservas órfãs

Exemplo de integração:

```python
requests.get("http://127.0.0.1:5000/turma/1")
```

---

## 📈 Futuras melhorias

* Autenticação e permissões por usuário
* Integração com banco relacional externo
* Painel web para gerenciamento visual

---


