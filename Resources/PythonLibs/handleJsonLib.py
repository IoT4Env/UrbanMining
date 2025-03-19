import json, os


class HandleJsonLib:
    #Get path of THIS file
    #Private variable due to the '_' at the beginning of the variable
    _current_file_path = os.path.dirname(os.path.abspath(__file__))
    
    def load_json(self, json_file:str):
        with open(os.path.join(self._current_file_path, f'../Json/{json_file}')) as f:
            return json.load(f)
    
