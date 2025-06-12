from flask import Blueprint, request, jsonify
from http import HTTPStatus
from src.application.services.logger_service import LoggerService
from src.infrastructure.db.repositories.cultura_repository import CulturaRepository
from src.application.usecases.cultura.listar_culturas import ListarCulturaUseCase
from src.application.usecases.cultura.cadastrar_cultura import CadastrarCulturaUseCase
from src.application.usecases.cultura.atualizar_cultura import AtualizarCulturaUseCase
from src.application.usecases.cultura.buscar_cultura import BuscarCulturaUseCase
from src.application.usecases.cultura.remover_cultura import RemoverCulturaUseCase


cultura_bp = Blueprint("culturas", __name__)
repository = CulturaRepository()
logger = LoggerService(__name__)

@cultura_bp.route("/culturas", methods=["GET"])
def listar_culturas():
    usecase = ListarCulturaUseCase(repository)
    try:
        culturas = usecase.executar()
        return jsonify({"culturas": culturas}), HTTPStatus.OK
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@cultura_bp.route("/cultura/<cultura_id>", methods=["GET"])
def buscar_cultura(cultura_id):
    usecase = BuscarCulturaUseCase(repository)
    try:
        cultura = usecase.executar(cultura_id)
        return jsonify({"cultura": cultura}), HTTPStatus.OK
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@cultura_bp.route("/culturas", methods=["POST"])
def cadastrar_cultura():
    data = request.json
    usecase = CadastrarCulturaUseCase(repository)
    try:
        cultura = usecase.executar(
                nome=data["nome"],
                area_utilizada=data["area_utilizada"]
                )
        return jsonify({
            "id": str(cultura.id),
            "nome": cultura.nome,
            "area_utilizada": cultura.area_utilizada
            }), HTTPStatus.CREATED
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@cultura_bp.route("/cultura/<cultura_id>", methods=["PUT"])
def atualizar_cultura(cultura_id):
    data = request.json
    usecase = AtualizarCulturaUseCase(repository)
    try:
        cultura = usecase.executar(
                cultura_id=cultura_id,
                nome=data["nome"],
                area_utilizada=data["area_utilizada"]
                )
        return jsonify({
            "nome": cultura.nome,
            "area_utilizada": cultura.area_utilizada,
            }), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@cultura_bp.route("/cultura/<cultura_id>", methods=["DELETE"])
def excluir_cultura(cultura_id):
    usecase = RemoverCulturaUseCase(repository)
    try:
        usecase.executar(cultura_id)
        return jsonify({"mensagem": "Cultura excluída com sucesso"}), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

