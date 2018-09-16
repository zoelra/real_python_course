def fahrenheit(celsius, conversion_rate, base_temperature):
    fahrenheit_conversion = celsius * conversion_rate + base_temperature
    return fahrenheit_conversion


def get_user_input():
    try:
        celsius_input = float(input("Enter Degrees Celsius: "))
        conversion_rate = 9 / 5
        base_temperature = float(32)
        return [celsius_input, conversion_rate, base_temperature]
    except ValueError:
        print("Oops! Please enter a valid number.")
        exit()


user_inputs = get_user_input()

print(fahrenheit(user_inputs[0], user_inputs[1], user_inputs[2]))
