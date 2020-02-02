import numpy as np
import pye57


class E57toPCD:
    def __init__(self,file):
        self.e57 = E57(file)
    def toPCD(self):
        # read scan at index 0
        data = self.e57.read_scan(0)
        instance(data["colorRed"], np.ndarray)
        instance(data["colorGreen"], np.ndarray)
        instance(data["colorBlue"], np.ndarray)

        # other attributes can be read using:
        data = self.e57.read_scan(0, intensity=True, colors=True, row_column=True)



