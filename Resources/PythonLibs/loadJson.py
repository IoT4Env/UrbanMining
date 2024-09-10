import json, os


class LoadJson:
    #Get path of THIS file
    _current_file_path = os.path.dirname(os.path.abspath(__file__))
    
    def load(self, json_file:str):
        with open(os.path.join(self._current_file_path, f'../Json/{json_file}')) as f:
            return json.load(f)
    
