import sqlalchemy


# def create_DB(name):
#
#
#     pass


class Fuel():
    def __init__(self, name, ro, w, effiency_p, W_i):
        self.name = name
        self.ro = ro
        self.w = w
        self.effiency_p = effiency_p
        self.W_i = W_i
        self.k_i = [0.2, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1]


    def sum_W(self, W_criterion):

        sum = 0
        i = 0
        for criterion in W_criterion:
            if criterion:
                sum = sum + self.W_i[i] * self.k_i[i]
            i = i + 1


        return sum


# Efficiency data of fuels.
fuels = [
    Fuel("KEROSIN+LIQUID_O", 1000, 3475, 2.408,
         [1, 1, 0.1, 0.5, 0.6, 0.1, 0.3]),
    Fuel("LIQUID_H+LIQUID_O", 200, 4500, 2.018,
         [0.7, 0.9, 0.8, 0.7, 0.8, 0.7, 0.8]),
    Fuel("SPG+LIQUID_O", 820, 3740, 2.266,
         [0.5, 0.2, 1, 1, 0.4, 0.2, 0.2]),
    Fuel("NDMG+4NO2", 1280, 2795, 2.979,
         [0.8, 0.9, 0.7, 0.7, 0.9, 0.8, 0.9]),
]
