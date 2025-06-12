from flask import Blueprint, request, jsonify
from http import HTTPStatus
from src.application.services.logger_service import LoggerService
from src.infrastructure.db.repositories.safra_repository import SafraRepository
from src.application.usecases.safra.listar_safras import ListarSafraUseCase
from src.application.usecases.safra.cadastrar_safra import CadastrarSafraUseCase
from src.application.usecases.safra.atualizar_safra import AtualizarSafraUseCase
from src.application.usecases.safra.buscar_safra import BuscarSafraUseCase
from src.application.usecases.safra.remover_safra import RemoverSafraUseCase


safra_bp = Blueprint("safras", __name__)
repository = SafraRepository()
logger = LoggerService(__name__)

@safra_bp.route("/safras", methods=["GET"])
def listar_safras():
    usecase = ListarSafraUseCase(repository)
    try:
        safras = usecase.executar()
        return jsonify({"safras": safras}), HTTPStatus.OK
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@safra_bp.route("/safra/<safra_id>", methods=["GET"])
def buscar_safra(safra_id):
    usecase = BuscarSafraUseCase(repository)
    try:
        safra = usecase.executar(safra_id)
        return jsonify({"safra": safra}), HTTPStatus.OK
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@safra_bp.route("/safras", methods=["POST"])
def cadastrar_safra():
    data = request.json
    usecase = CadastrarSafraUseCase(repository)
    try:
        safra = usecase.executar(
                ano=data["ano"],
                culturas=data["culturas"]
                )
        return jsonify({
            "id": str(safra.id),
            "ano": safra.ano,
            "culturas": safra.culturas
            }), HTTPStatus.CREATED
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@safra_bp.route("/safra/<safra_id>", methods=["PUT"])
def atualizar_safra(safra_id):
    data = request.json
    usecase = AtualizarSafraUseCase(repository)
    try:
        safra = usecase.executar(
                safra_id=safra_id,
                ano=data["ano"],
                culturas=data["culturas"]
                )
        return jsonify({
            "ano": safra.ano,
            "culturas": safra.culturas
            }), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@safra_bp.route("/safra/<safra_id>")
def excluir_safra(safra_id):
    usecase = RemoverSafraUseCase(repository)
    try:
        usecase.executar(safra_id)
        return jsonify({"mensagem": "Safra excluída com sucesso"}), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST
