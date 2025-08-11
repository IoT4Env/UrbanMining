import json, os


class JsonHelperLib:
    #Get path of THIS file
    _current_file_path = os.path.dirname(os.path.abspath(__file__))
    

    def load_address_translation(self):
        self._address_translation = 'addressTranslation.json'
        try:
            with open(os.path.join(self._current_file_path, f'../Json/{self._address_translation}')) as json_file:
                json_data = json.load(json_file)
                json_file.close()
            
            return json_data
        except FileNotFoundError as file_error:
            print(f'File not found: {self._address_translation}')
    
    
    def load_enumerables(self):
        self._enamerables = 'enumerables.json'

        try:    
            with open(os.path.join(self._current_file_path, f'../Json/{self._enamerables}')) as json_file:
                json_data = json.load(json_file)
                json_file.close()
        
            return json_data
        except FileNotFoundError as file_error:
            print(f'File not found: {self._enamerables}')
