from app.facade.juscaba import API
import json


class JuscabaController:
    @staticmethod
    def get_first(identificador: str):

        filter = {
            'filter': json.dumps({'identificador': identificador}),
            'tipoBusqueda': 'CAU',
            'page': 0,
            'size': 10
        }

        data = API.get_list(filter)
        exp_id = data['content'][0]['expId']
        details = API.get_record_details(exp_id)

        return JuscabaController.curate_data(exp_id, details)

    def curate_data(id, data: dict):
        return {
            'id': id,
            'fecha': data['fechaInicio'],
            'caratula': data['caratula'],
            'materia': data['objetosJuicio'][0]['materia'],
            'objeto': data['objetosJuicio'][0]['objetoJuicio']
        }
