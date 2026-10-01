"""Give simple gardening advice for a selected season and plant type."""

SEASON_ADVICE = {
    "spring": "Prepare the soil and begin sowing frost-tolerant seeds.",
    "summer": "Water your plants regularly and provide some shade.",
    "autumn": "Collect fallen leaves for compost and protect tender plants.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Harvest little and often to encourage fresh growth.",
}


def get_gardening_advice(season, plant_type):
    """Return combined advice for a season and type of plant."""
    season_tip = SEASON_ADVICE.get(season, "No advice for this season.")
    plant_tip = PLANT_ADVICE.get(plant_type, "No advice for this type of plant.")
    return f"{season_tip}\n{plant_tip}"


def main():
    """Ask the user about their garden and display suitable advice."""
    season = input("Enter the current season: ").strip().lower()
    plant_type = input("Enter the plant type: ").strip().lower()
    print(get_gardening_advice(season, plant_type))


if __name__ == "__main__":
    main()
