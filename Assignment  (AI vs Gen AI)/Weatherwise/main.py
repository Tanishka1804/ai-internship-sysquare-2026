from weather_service import get_weather
from weather_utils import (
    calculate_travel_score,
    weather_mood,
    smart_advice
)
from ai_summary import generate_summary


def display_weather(weather):

    score = calculate_travel_score(
        weather["temperature"],
        weather["humidity"]
    )

    mood = weather_mood(
        weather["temperature"],
        weather["condition"]
    )

    advice = smart_advice(
        weather["temperature"],
        weather["humidity"]
    )

    summary = generate_summary(weather)

    print("\n" + "=" * 50)

    print(f"📍 City: {weather['city']}")
    print(f"🌡 Temperature: {weather['temperature']}°C")
    print(f"🤗 Feels Like: {weather['feels_like']}°C")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"☁ Condition: {weather['condition']}")

    print("\n🚗 Travel Comfort Score:")
    print(f"{score}/10")

    print("\n🌈 Weather Mood:")
    print(mood)

    print("\n💡 Smart Advice:")
    print(advice)

    print("\n🤖 AI Summary:")
    print(summary)

    print("=" * 50)


def run_agent():

    print("""
========================================================
                🌤 WeatherWise AI
========================================================

Hello! 👋

I'm WeatherWise.

Want to know how the weather looks in a city?
Just enter the city name and I'll take care of the rest.

Type 'exit' anytime to quit.

========================================================
""")

    while True:

        city = input("\n📍 Enter city name: ").strip()

        if city.lower() == "exit":

            print(
                "\n👋 Thanks for using WeatherWise."
                "\nHave a great day!"
            )

            break

        weather = get_weather(city)

        if not weather:

            print(
                "\n❌ Sorry, I couldn't find weather information "
                "for that city."
                "\nPlease check the city name and try again."
            )

            continue

        print(
            "\n🤖 Analyzing weather conditions "
            "and generating insights..."
        )

        display_weather(weather)


if __name__ == "__main__":
    run_agent()