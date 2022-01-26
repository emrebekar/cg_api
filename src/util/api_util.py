from typing import Dict, Tuple 
import requests

class ApiUtil:

    @staticmethod
    def send_request(scheme: str, host:str, base_path:str,  method: str, path: str, path_vars: Dict, query_params: Dict) -> Tuple:

        header = {
            "Content-Type": "application/json"
        }

        formatted_path = path.format(**path_vars)

        args = {
            "method": method,
            "url": f"{scheme}://{host}{base_path}{formatted_path}",
            "headers": header,
            "params": {k: v for k, v in query_params.items() if v is not None}
        }

        response = requests.request(**args)
        if response.ok:
            return response.headers, response.json()

        raise Exception(response.content)