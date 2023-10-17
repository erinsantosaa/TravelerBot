import discord
import requests
from discord.ext import commands
from translate import Translator

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, traveler!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello, {message.author.mention}!')


# Testing currency conversion using Open Exchange Rates API
def convert_currency(api_key, from_currency, to_currency, amount):
    base_url = "https://open.er-api.com/v6/latest/"
    url = f"{base_url}/{from_currency}"
    params = {"apikey": api_key}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            raise Exception("Error fetching exchange rates")

        if to_currency not in data["rates"]:
            raise Exception("Invalid currency code")

        conversion_rate = data["rates"][to_currency]
        converted_amount = amount * conversion_rate

        return converted_amount

    except Exception as e:
        return f"Error: {str(e)}"

api_key = "INSERT_API_KEY"
from_currency = "USD"
to_currency = "EUR"
amount = 50

converted_amount = convert_currency(api_key, from_currency, to_currency, amount)
if isinstance(converted_amount, float):
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
else:
    print(converted_amount)


# Testing getting weather data using Open Weather Map API
def getWeatherData(api_key, city_name):
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    current_weather_params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    forecast_params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        current_weather_response = requests.get(current_weather_url, params=current_weather_params)

        if current_weather_response.status_code == 200:
            current_weather_data = current_weather_response.json()

            forecast_response = requests.get(forecast_url, params=forecast_params)

            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()

                return {
                    "current_weather": current_weather_data,
                    "forecast": forecast_data
                }
            else:
                print(f"Error: Unable to fetch forecast data. Status Code: {forecast_response.status_code}")
        else:
            print(f"Error: Unable to fetch current weather data. Status Code: {current_weather_response.status_code}")

        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

api_key = "INSERT_API_KEY"
city_name = "New York"

weather_data = getWeatherData(api_key, city_name)

if weather_data:
    current_weather = weather_data["current_weather"]
    forecast = weather_data["forecast"]

    print("Current Weather Description:", current_weather["weather"][0]["description"])
    print("Current Temperature (°C):", current_weather["main"]["temp"])
    print("Current Humidity:", current_weather["main"]["humidity"], "%")

# Testing language translation with translator library
def translate_text(text, target_language):
    try:
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return str(e)

text_to_translate = "Hello, how are you?"
target_language = "es"  # Spanish
translated_text = translate_text(text_to_translate, target_language)
print(translated_text)


# Run the bot
bot.run('INSERT_API_KEY')