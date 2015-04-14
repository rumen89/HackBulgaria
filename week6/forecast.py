#forecast.py

def forecast(days):
    days_weather = {
        "rain": 0,
        "snow": 0,
        "sunshine": 0
    }

    for day in days:
        if day in days_weather:
            days_weather[day] += 1

    if days_weather["rain"] == days_weather["snow"] == days_weather["sunshine"]:
        return days[len(days) - 1]

    if days_weather["rain"] == days_weather["sunshine"]:
        return "snow"
    elif days_weather["rain"] == days_weather["snow"]:
        return "sunshine"
    elif days_weather["sunshine"] == days_weather["snow"]:
        return "rain"

    current_weather = days_weather["rain"]

    for weather in days_weather:
        if days_weather[weather] > current_weather:
            current_weather = days_weather[weather]
            result = weather

    return result

# a = forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"])
# print("The weather today is:")
# print(a)