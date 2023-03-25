# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_param_dict(self):
        return {'x': self.x, 'y': self.y, "z": self.z}


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        param = cube.get_param_dict()
        return param['x'] * param['y'] * param['z']
