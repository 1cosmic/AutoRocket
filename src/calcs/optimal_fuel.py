from src.DB.data_storage import fuels

def get_optimal_fuel(fuels, criterion=None):
    """Return max efficiency fuel."""

    criterion = [True for i in range(7)]

    last_max_fuel = None
    last_max_score = None

    for fuel in fuels:
        score = fuel.effiency_p * fuel.sum_W(criterion)
        # print(f"Fuel: {fuel.name}\tMax score: {score}")

        if last_max_score == None or last_max_score > score:
            last_max_score = score
            last_max_fuel = fuel

    return last_max_fuel


print(get_optimal_fuel(fuels).name)