import os
import re

class Util:
    
    def __init__(self) -> None:
        self._img_ext = ['jpg', 'jpeg', 'png']
        self._current_dir = os.getcwd()
        
    def get_list_files(self, path, extension):
        self._extension = extension
        if (path is not None):
            self._working_path = os.path.join(self._current_dir, path)
        else:
            self._working_path = self._current_dir
            
        _list_files = os.listdir(self._working_path)
        return self._check_format(_list_files)
    
    def _check_format(self, data):
        print('---> check format > files found: ', data)
        _out = []
        if (self._extension is not None):
            if (len(data) > 0):
                for i in data:
                    j = i.split('.')
                    if j[-1] == self._extension:
                        _full_path = os.path.join(self._working_path, i)
                        _out.append(_full_path)
        else:
            if (len(data) > 0):
                for i in data:
                    j = i.split('.')
                    if any(re.findall('|'.join(self._img_ext), j[-1])):
                        _full_path = os.path.join(self._working_path, i)
                        _out.append(_full_path)
        return _out

