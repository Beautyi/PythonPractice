favourite_places = {
    'jen': ['beijing', 'tianjin'],
    'sarah': ['hangzhou'],
    'edward': ['beijing', 'paris'],
    'phil': ['tongliao', 'hangzhou']

    }
for name, places in favourite_places.items():
    print("\n" + name.title() + "'s favourite places are:")
    for place in places:
        print("\t" + place.title())
        