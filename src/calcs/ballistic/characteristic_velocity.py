from math import *

# Constant values.
R_Earth = 6371
mu = 3.986 * pow(10, 5)

V1 = 7.91  # km/c -> first cosmic =)

def V_char_ideal(h_orbit):
    """
    Calculate of ideal character velocity.
    """

    r_orbit = h_orbit + R_Earth
    res = sqrt(
        (mu / r_orbit) * (2 * r_orbit / R_Earth - 1))
    return res


def V_needed(V_char_ideal, sum_dV_i):
    """
    Calculate of nedded character velocity for Rocket (sum nedded velocity + maneuvers.
    """
    sum_dV_interference = -1.650  # km/s -> sum of interference: dV_G (gravitation, dV_A (aerodynamic)
    # dV_P (P of nozzle), dV_management.

    V_needed = V_char_ideal + sum_dV_i + sum_dV_interference
    return V_needed


def V_perigee(r_p, r_a):
    """
    Calculate of velocity in perigee of ellipse orbit -> target point (target orbit).
    """

    a = (r_a + r_p) / 2

    V_p = V1 * sqrt(
        R_Earth * ((2 / r_p) - (1 / a)))
    return V_p


def Voo(r_oo):
    """
    Calculate of velocity Space Machine on cycle orbit.
    """

    V_oo = V1 * sqrt(
        R_Earth / r_oo)
    return V_oo


def dV_1(r_p, r_a):

    r_p = r_p + R_Earth
    # r_a = r_a + R_Earth

    res = V_perigee(r_p, r_a) - Voo(r_p)
    return res

def V_ideal_i(w_n, m_start, m_end):
    """
    Max dV, what upper stage can be add to payload.
    """
    z_i = m_start / m_end
    V_id = w_n * log(z_i)
    return V_id


#
# def name():
#     """
#
#     """
#
#     pass

# def d_speed_cyrcle_to_ellipse(, V)
