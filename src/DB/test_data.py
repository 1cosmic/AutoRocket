class Data():
    class orbit():
        start = 200  # km
        end = 384400  # km

    class payload():
        mass = 8.885  # ton.
        class Fregat():
            w = 3269  # m/s (удельный импульс)
            m_start = 6235  # kg
            m_end = 945  # kg

        mass_KA = 2250  # kg


class TrueResult():
    class velocity():
        V_char_ideal = 8.029  # km/s
        dV_1 = 3.133  # km/s
        V_needed = 9.529  # km/s

        V_id_Fregat = 3.193  # km/s