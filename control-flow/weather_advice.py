weatherToday = input("What's the weather today? (sunny/rainy/cold): ")

if weatherToday == "sunny":
    print(f"Wear a t-shirt and sunglasses.")
elif weatherToday == "rainy":
    print(f"Don't forget your umbrella and a raincoat.")
elif weatherToday == "cold":
    print(f"Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.")