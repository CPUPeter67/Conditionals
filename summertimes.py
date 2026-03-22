temperature = float(input("What is the temperature in your area in Celsius? "))

if temperature >= 30:
    print("It's a pretty hot day. You are recommended to drink lots of water and wear loose clothing.")

if temperature >= 20 and temperature < 30:    
    print("It's a nice day. You can go outside and enjoy the weather. You can wear normal, comfortable clothes.")

if temperature >= 10 and temperature < 20:
    print("It's a bit chilly. You can wear a light jacket or sweater.")    

if temperature < 10:
    print("Brrr, it's cold! You should wear heavy, warm clothing and even a hat or gloves as it might be snowing.")    