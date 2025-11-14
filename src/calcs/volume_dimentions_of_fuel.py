from math import log

from scipy.optimize import *
import numpy as np

# s_i = [7.69, 12.33, 9.43, 9.43]
# w = [3000, 4500, 4500, 4500]
# Vx = 11260

s_i = [9, 12, 8, 8]
w = [3150, 3150, 3000, 3000]
Vx = 9529

# a = 833.85 / 2216.08  # Relations engine of rocket.
# a = 2216.08 / 833.85  # Relations engine of rocket.
a = 1  # Relations engine of rocket.


def Si(s):
    return s / (s - 1)


def sum_mass(s, x):
    sum = 0
    for i in range(len(x)):
        sum += s[i] * x[i]
    return sum


s = [Si(i) for i in s_i]


# Sequence block of rocket.
##############################
def f(x, start=0):
    res = [1]
    for i in range(len(x))[start:]:
        res.append(s[i] * x[i])

    return sum(res)


def c1(x):
    return f(x)


def c1_seq(x):
    return (c1(x) / (c1(x) - x[0]))


def c1_paral(x):
    return (c1(x) / (c1(x) - x[0] - a * w[0] * x[0] / w[1]))


def c1_paral_speed(x):
    c_local = c1_paral(x)
    return (w[0] * w[1] * (1 + a)) / (w[1] + a * w[0]) * log(c_local)


def c1_seq_speed(x):
    c_local = c1_seq(x)
    return w[0] * log(c_local)


def c2(x):
    return f(x, 1)


def c2_seq(x):
    return (c2(x) / (c2(x) - x[1]))


def c2_paral(x):
    return ((c2(x) - a * w[0] * x[0] / w[1]) / (c2(x) - x[1]))


def c3(x):
    return f(x, 2)


def c3_seq(x):
    return (c3(x) / (c3(x) - x[2]))


def c3_paral(x):
    res = (c3(x) / (c3(x) - x[2]))
    return res


def c4(x):
    return f(x, 3)


def c4_seq(x):
    return (c4(x) / (c4(x) - x[3]))


def c4_paral(x):
    return (c4(x) / (c4(x) - x[3]))


def c5(x):
    return f(x, 4)


def main_c_seq(x):
    return Vx - w[0] * log(c1_seq(x)) \
        - w[1] * log(c2_seq(x)) \
        - w[2] * log(c3_seq(x))


def main_c_seq_2(x):
    res = Vx - w[0] * log(c1_seq(x)) \
          - w[1] * log(c2_seq(x))
    return res


def main_c_seq_3(x):
    res = Vx - w[0] * log(c1_seq(x)) \
          - w[1] * log(c2_seq(x)) \
          - w[2] * log(c3_seq(x))
    return res


def main_c_seq_4(x):
    res = Vx - w[0] * log(c1_seq(x)) \
          - w[1] * log(c2_seq(x)) \
          - w[2] * log(c3_seq(x)) \
          - w[3] * log(c4_seq(x))
    return res


def main_c_paral_2(x):
    res = Vx - ((w[0] * w[1] * (1 + a)) / (w[1] + a * w[0])) * log(c1_paral(x)) \
          - w[1] * log(c2_paral(x))
    return res


def main_c_paral_3(x):
    res = Vx - ((w[0] * w[1] * (1 + a)) / (w[1] + a * w[0])) * log(c1_paral(x)) \
          - w[1] * log(c2_paral(x)) \
          - w[2] * log(c3_paral(x))

    return res


def main_c_paral_4(x):
    res = Vx - ((w[0] * w[1] * (1 + a)) / (w[1] + a * w[0])) * log(c1_paral(x)) \
          - w[1] * log(c2_paral(x)) \
          - w[2] * log(c3_paral(x)) \
          - w[3] * log(c4_paral(x))
    return res


##############################
##############################
def mass_fuel(x, m_pn):
    return x * m_pn


def mass_block(m_fuel):
    return np.multiply(m_fuel, s[:len(m_fuel)])


##############################
##############################


def calc_optim_weight_fuel(m_pn):
    nonLC_seq = [[
        NonlinearConstraint(c1_seq, 1, np.inf),
        NonlinearConstraint(c2_seq, 1, np.inf),
        # NonlinearConstraint(c1_seq_speed, 3000, np.inf),
        NonlinearConstraint(main_c_seq_2, -np.inf, 0)],
        [
            NonlinearConstraint(c1_seq, 1, np.inf),
            NonlinearConstraint(c2_seq, 1, np.inf),
            NonlinearConstraint(c3_seq, 1, np.inf),
            # NonlinearConstraint(c1_seq_speed, 3000, np.inf),
            NonlinearConstraint(main_c_seq_3, -np.inf, 0),
        ],
        [
            NonlinearConstraint(c1_seq, 1, np.inf),
            NonlinearConstraint(c2_seq, 1, np.inf),
            NonlinearConstraint(c3_seq, 1, np.inf),
            NonlinearConstraint(c4_seq, 1, np.inf),
            # NonlinearConstraint(c1_seq_speed, 3000, np.inf),
            NonlinearConstraint(main_c_seq_4, -np.inf, 0),
        ],
    ]

    nonLC_paral = [[
        NonlinearConstraint(c1_paral, 1, np.inf),
        NonlinearConstraint(c2_paral, 1, np.inf),
        # NonlinearConstraint(c1_paral_speed, 3000, np.inf),
        NonlinearConstraint(main_c_paral_2, -np.inf, 0)],
        [
            NonlinearConstraint(c1_paral, 1, np.inf),
            NonlinearConstraint(c2_paral, 1, np.inf),
            NonlinearConstraint(c3_paral, 1, np.inf),
            # NonlinearConstraint(c1_paral_speed, 3000, np.inf),
            NonlinearConstraint(main_c_paral_3, -np.inf, 0),
        ],
        [
            NonlinearConstraint(c1_paral, 1, np.inf),
            NonlinearConstraint(c2_paral, 1, np.inf),
            NonlinearConstraint(c3_paral, 1, np.inf),
            NonlinearConstraint(c4_paral, 1, np.inf),
            # NonlinearConstraint(c1_paral_speed, 3000, np.inf),
            NonlinearConstraint(main_c_paral_4, -np.inf, 0),
        ],
    ]

    # Start x.
    x_fix = np.array([15, 23, 3, 3, 3])

    # Solver.
    for i in range(5)[2:]:
        x = x_fix[:i]
        bounds = [(1, 100) for i in range(len(x))]

        # TOOO: WHY THIS FUNCTON INCORRECT WORK AFTER 4th step of rocket?

        res_paral = minimize(f, x, method='slsqp', bounds=bounds, constraints=nonLC_paral[i - 2])
        res_seq = minimize(f, x, method='slsqp', bounds=bounds, constraints=nonLC_seq[i - 2])
        print("PARAL: ", res_paral.x, f(res_paral.x))
        print("SEQ: ", res_seq.x, f(res_seq.x))

        m_fuel = mass_fuel(res_paral.x, m_pn)
        m_block = mass_block(m_fuel)

        # print("Mass fuel: ", m_fuel)
        # print("Masses of blocks: ", m_block)
        print("Sum: ", sum(m_block), '\n\n')


if __name__ == "__main__":
    m_pn = 8.885
    calc_optim_weight_fuel(m_pn)
