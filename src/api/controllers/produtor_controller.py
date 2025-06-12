from flask import Blueprint, request, jsonify
from http import HTTPStatus
from src.application.services.logger_service import LoggerService
from src.application.usecases.produtor.buscar_produtor import BuscarProdutorUseCase
from src.infrastructure.db.repositories.produtor_repository import ProdutorRepository
from src.application.usecases.produtor.cadastrar_produtor import CadastrarProdutorUseCase
from src.application.usecases.produtor.listar_produtores import ListarProdutoresUseCase
from src.application.usecases.produtor.atualizar_produtor import AtualizarProdutorUseCase
from src.application.usecases.produtor.remover_produtor import RemoverProdutorUseCase


produtor_bp = Blueprint("produtores", __name__)
repository = ProdutorRepository()
logger = LoggerService(__name__)

@produtor_bp.route("/produtores", methods=["POST"])
def cadastrar_produtor():
    data = request.json
    usecase = CadastrarProdutorUseCase(repository)
    try:
        produtor = usecase.executar(
                nome=data["nome"],
                documento=data["documento"],
                propriedades=data["propriedades"]
                )
        return jsonify({
            "id": str(produtor.id),
            "nome": produtor.nome,
            "documento": produtor.documento
            }), HTTPStatus.CREATED
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@produtor_bp.route("/produtores", methods=["GET"])
def listar_produtores():
    usecase = ListarProdutoresUseCase(repository)
    try:
        produtores = usecase.executar()
        return jsonify({"produtores": produtores}), HTTPStatus.OK
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@produtor_bp.route("/produtor/<produtor_id>", methods=["GET"])
def buscar_produtor(produtor_id):
    usecase = BuscarProdutorUseCase(repository)
    try:
        produtor = usecase.executar(produtor_id)
        return jsonify({"produtor": produtor}), HTTPStatus.OK
    except Exception as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@produtor_bp.route("/produtor/<produtor_id>", methods=["PUT"])
def atualizar_produtor(produtor_id):
    data = request.json
    usecase = AtualizarProdutorUseCase(repository)
    try:
        produtor = usecase.executar(
                produtor_id=produtor_id,
                nome=data["nome"],
                documento=data["documento"],
                propriedades=data["propriedades"]
                )
        return jsonify({
            "nome": produtor.nome,
            "documento": produtor.documento,
            "propriedades": produtor.propriedades
            }), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@produtor_bp.route("/produtor/<produtor_id>", methods=["DELETE"])
def excluir_produtor(produtor_id):
    usecase = RemoverProdutorUseCase(repository)
    try:
        usecase.executar(produtor_id)
        return jsonify({"mensagem": "Produtor excluído com sucesso"}), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST
