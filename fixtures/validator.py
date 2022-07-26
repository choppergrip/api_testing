import cattr
from requests import Response


class Validator:
    def structure_response(self, response: Response, response_data_model) -> Response:
        """
        Convert unstructured response data to structured
        :param response: response
        :param response_data_model: response data model
        :return structured response
        """
        if response_data_model:
            try:
                response.data = cattr.structure(response.json(), response_data_model)
            except Exception as e:
                raise e

        return response
