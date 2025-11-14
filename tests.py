from pytest import approx

import src.calcs.ballistic.characteristic_velocity as cV
from src.DB.test_data import *

d = Data()
Fregat = d.payload.Fregat
true_d = TrueResult()

def test_char_velocity():

    V_char_ideal = cV.V_char_ideal(d.orbit.start)
    dV_1 = cV.dV_1(d.orbit.start, d.orbit.end)
    V_ideal_US = cV.V_ideal_i(Fregat.w, Fregat.m_start, Fregat.m_end)
    V_needed = (cV.V_needed(V_char_ideal, dV_1))

    assert V_char_ideal == approx(true_d.velocity.V_char_ideal, 0.005)
    assert dV_1 == approx(true_d.velocity.dV_1, 0.005)
    assert V_needed == approx(true_d.velocity.V_needed, 0.005)
    assert V_ideal_US >= dV_1