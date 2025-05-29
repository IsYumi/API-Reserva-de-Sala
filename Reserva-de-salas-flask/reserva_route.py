from flask import Blueprint, request, jsonify
from reserva_model import Reserva
from database import db
import requests

routes = Blueprint("routes", __name__)

def obter_dados_turma(turma_id):
    try:
        resp = requests.get(f"http://127.0.0.1:5000/api/turma/{turma_id}")  
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        print("Erro ao obter turma:", e)
    return None



def validar_turma(turma_id):
    resp = requests.get(f"http://localhost:5000/api/turmas/{turma_id}")
    return resp.status_code == 200

@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json
    turma_id = dados.get("turma_id")

    if not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva = Reserva(
        turma_id=turma_id,
        sala=dados.get("sala"),
        data=dados.get("data"),
        hora_inicio=dados.get("hora_inicio"),
        hora_fim=dados.get("hora_fim")
    )

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"mensagem": "Reserva criada com sucesso"}), 201

@routes.route("/reservas", methods=["GET"])
def listar_reservas():
    reservas = Reserva.query.all()
    resultado = []
    for r in reservas:
        turma_info = obter_dados_turma(r.turma_id)
        print(f"Turma ID: {r.turma_id} -> turma_info: {turma_info}")  # DEBUG
        resultado.append({
            "id": r.id,
            "turma_id": r.turma_id,
            "turma": turma_info,  
            "sala": r.sala,
            "data": r.data,
            "hora_inicio": r.hora_inicio,
            "hora_fim": r.hora_fim
        })
    return jsonify(resultado)


@routes.route("/reservas/<int:id>", methods=["GET"])
def detalhar_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    return jsonify(reserva.to_dict(turma=obter_dados_turma(reserva.turma_id)))

@routes.route("/reservas/<int:id>", methods=["PUT"])
def atualizar_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    dados = request.json
    turma_id = dados.get("turma_id")

    if turma_id and not validar_turma(turma_id):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva.turma_id = turma_id or reserva.turma_id
    reserva.sala = dados.get("sala", reserva.sala)
    reserva.data = dados.get("data", reserva.data)
    reserva.hora_inicio = dados.get("hora_inicio", reserva.hora_inicio)
    reserva.hora_fim = dados.get("hora_fim", reserva.hora_fim)

    db.session.commit()

    return jsonify({"mensagem": "Reserva atualizada com sucesso"})


@routes.route("/reservas/<int:id>", methods=["DELETE"])
def deletar_reserva(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        return jsonify({"erro": "Reserva não encontrada"}), 404

    db.session.delete(reserva)
    db.session.commit()
@routes.route("/teste-turma/<int:turma_id>", methods=["GET"])
def teste_turma(turma_id):
    turma = obter_dados_turma(turma_id)
    return jsonify(turma)
