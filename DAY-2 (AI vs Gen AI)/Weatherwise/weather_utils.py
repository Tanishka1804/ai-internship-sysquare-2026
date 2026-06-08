def calculate_travel_score(temp, humidity):
    score = 10

    if temp > 40:
        score -= 3

    elif temp > 35:
        score -= 2

    if humidity > 80:
        score -= 2

    elif humidity > 60:
        score -= 1

    return max(score, 1)


def weather_mood(temp, condition):

    condition = condition.lower()

    if "rain" in condition:
        return "A calm rainy day 🌧"

    elif temp > 35:
        return "A hot energetic summer day 🔥"

    elif temp < 15:
        return "A cool and peaceful day ❄"

    else:
        return "A pleasant day to be outdoors 🌤"


def smart_advice(temp, humidity):

    if temp > 38:
        return (
            "Stay hydrated and avoid direct sunlight "
            "during afternoon hours."
        )

    if humidity > 80:
        return (
            "High humidity may feel uncomfortable. "
            "Plan outdoor activities carefully."
        )

    return (
        "Weather conditions look comfortable "
        "for most outdoor activities."
    )