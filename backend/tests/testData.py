"""
Файл с тестовыми данными для моделирования процесса нагревания продукта в духовке
"""

import numpy as np


class SensorData:
    """
    Класс для моделирования процесса нагревания нагревания корки продукта, внетреннего наргева и потери влаги
    """
    def __init__(self, t: np.array,
                 t_start: float = 22.0,
                 t_end: float = 200.0,
                 a: float = 23e-6,
                 x: float = 0.21,
                 y: float = 0.11,
                 z: float = 0.06):
        self.t = t
        self.t_start = t_start
        self.t_end = t_end
        self.a = a
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def _calc_rT(F: float, n: int = 50) -> float:
        """
        Метод для подсчета относительной температуры по числу Фурье в соответствиии с формулой для пластины

        :param F: float, число Фурье
        :param n: int, параметр приближения
        :return: float, относительная темпаратура
        """
        return (4 / np.pi) * np.sum(
            np.array(
                [
                    (1 / (2 * i - 1) * ((-1) ** (i + 1)) * np.exp(-(2 * i - 1) ** 2 * np.pi ** 2 / 4 * F))
                    for i in range(1, n + 1)
                ]
            )
        )

    def _calc_F(self, index: int, dim: float) -> float:
        """
        Функция для расчета числа Фурье

        :param index: int, индекс элемента в массиве времени
        :param dim: float, линейный размер продука
        :return: float, число Фурье
        """
        return (self.t[index] * self.a) / (dim ** 2)

    def inner_heat(self):
        pass

    def outer_heat(self, index: int):
        """
        Функция для рассчета температуры на поверхности продукта

        :param index: int, временная ответка
        :return: температура через промежуток времени
        """
        F_x, F_y, F_z = self._calc_F(index, self.x), self._calc_F(index, self.y), self._calc_F(index, self.z)
        O_x, O_y, O_z = self._calc_rT(F_x), self._calc_rT(F_y), self._calc_rT(F_z)
        O_total = O_x * O_y * O_z
        return self.t_end + 273 - O_total * (self.t_end + 273 - self.t_start + 273) - 273

    def mass_loss(self):
        pass
