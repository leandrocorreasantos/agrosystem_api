from flask import Blueprint, request, jsonify
from http import HTTPStatus
from src.application.services.logger_service import LoggerService
from src.infrastructure.db.repositories.propriedade_repository import PropriedadeRepository
from src.application.usecases.propriedade.cadastrar_propriedade import CadastrarPropriedadeUseCase
from src.application.usecases.propriedade.listar_propriedades import ListarPropriedadeUseCase
from src.application.usecases.propriedade.atualizar_propriedade import AtualizarPropriedadeUseCase
from src.application.usecases.propriedade.remover_propriedade import RemoverPropriedadeUseCase


propriedade_bp = Blueprint("propriedades", __name__)
repository = PropriedadeRepository()
logger = LoggerService(__name__)

@propriedade_bp.route("/propriedades", methods=["GET"])
def listar_propriedades():
    usecase = ListarPropriedadeUseCase(repository)
    try:
        propriedades = usecase.executar()
        return jsonify({"propriedades": propriedades}), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@propriedade_bp.route("/propriedades", methods=["POST"])
def cadastrar_propriedade():
    data = request.json
    usecase = CadastrarPropriedadeUseCase(repository)
    try:
        propriedade = usecase.executar(
                nome=data["nome"],
                cidade=data["cidade"],
                estado=data["estado"],
                area_total=data["area_total"],
                area_agricultavel=data["area_agricultavel"],
                area_vegetacao=data["area_vegetacao"],
        safras=data["safras"]
                )
        return jsonify({
            "id": str(propriedade.id),
            "nome": propriedade.cidade,
            "cidade": propriedade.estado,
            "area_total": propriedade.area_total,
            "area_vegetacao": propriedade.area_vegetacao,
            "area_agricultavel": propriedade.area_agricultavel,
            "safras": propriedade.safras
            }), HTTPStatus.CREATED
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@propriedade_bp.route("/propriedade/<propriedade_id>", methods=["PUT"])
def atualizar_propriedade(propriedade_id):
    data = request.json
    usecase = AtualizarPropriedadeUseCase(repository)
    try:
        propriedade = usecase.executar(
                propriedade_id=propriedade_id,
                nome=data["nome"],
                cidade=data["cidade"],
                estado=data["estado"],
                area_total=data["area_total"],
                area_agricultavel=data["area_agricultavel"],
                area_vegetacao=data["area_vegetacao"],
                safras=data["safras"]
                )
        return jsonify({
            "nome": propriedade.nome,
            "cidade": propriedade.cidade,
            "estado": propriedade_id.estado,
            "area_total": propriedade.area_total,
            "area_vegetacao": propriedade.area_vegetacao,
            "area_agricultavel": propriedade.area_agricultavel,
            "safras": propriedade.safras
            }), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

@propriedade_bp.route("/propriedade/<propriedade_id>", methods=["DELETE"])
def excluir_propriedade(propriedade_id):
    usecase = RemoverPropriedadeUseCase(repository)
    try:
        usecase.executar(propriedade_id)
        return jsonify({"mensagem": "Propriedade excluída com sucesso"}), HTTPStatus.OK
    except ValueError as e:
        logger.error(str(e))
        return jsonify({"erro": str(e)}), HTTPStatus.BAD_REQUEST

