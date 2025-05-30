from database import db
import requests

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    hora_inicio = db.Column(db.String(10), nullable=False)
    hora_fim = db.Column(db.String(10), nullable=False)

    def to_dict(self, turma=None):
        if turma is None:
            try:
                response = requests.get(f"http://127.0.0.1:5000/api/turma/{self.turma_id}")
                if response.status_code == 200:
                    turma = response.json()
            except Exception:
                turma = None

        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "turma": turma,
            "sala": self.sala,
            "data": self.data,
            "hora_inicio": self.hora_inicio,
            "hora_fim": self.hora_fim
        }
