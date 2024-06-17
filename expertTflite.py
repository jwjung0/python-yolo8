from ultralytics import YOLO
from utils import Util

class ExpertTflite:
    
    def __init__(self) -> None:
        print('---> expert tflite > init')
        self._get_files()
    
    def _get_files(self):
        _util = Util()
        self.models = _util.get_list_files(None, extension='pt')
        print('---> models: ', self.models)
    
    def excute(self):
        if self.models is not None:
            for model in self.models:
                model = YOLO(model=model)
                model.export(format='tflite')

if __name__ == '__main__':
    app = ExpertTflite()
    app.excute()
