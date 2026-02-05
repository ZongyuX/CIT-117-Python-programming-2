#1.Input the Earth Weight and Name
sName = input("What is your name")
nEarthWeight = float(input("What is your weight："))


#2.Plant and Surface Gravity Factor

MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066

#3.Calculate

nWeightMercury = nEarthWeight * MERCURY_GRAVITY
nWeightVenus = nEarthWeight * VENUS_GRAVITY
nWeightMoon = nEarthWeight * MOON_GRAVITY
nWeightMars = nEarthWeight * MARS_GRAVITY
nWeightJupiter = nEarthWeight * JUPITER_GRAVITY
nWeightSaturn = nEarthWeight * SATURN_GRAVITY
nWeightUranus = nEarthWeight * URANUS_GRAVITY
nWeightNeptune = nEarthWeight * NEPTUNE_GRAVITY
nWeightPluto = nEarthWeight * PLUTO_GRAVITY

#4.Output


print(f"{sName} here are your weights on our solar system's planets:")
print(f"Weight on Mercury: "  + format(nWeightMercury, '10.2f'))
print(f"Weight on Venus:   "  + format(nWeightVenus, '10.2f'))
print(f"Weight on our Moon:"  + format (nWeightMoon, '10.2f'))
print(f"Weight on Mars:    "  + format (nWeightMars,  '10.2f'))
print(f"Weight on Jupiter: "  + format (nWeightJupiter, '10.2f'))
print(f"Weight on Saturn:  "  + format (nWeightSaturn, '10.2f'))
print(f"Weight on Uranus:  "  + format (nWeightUranus, '10.2f'))
print(f"Weight on Neptune: "  + format (nWeightNeptune, '10.2f'))
print(f"Weight on Pluto:   "  + format (nWeightPluto,  '10.2f'))
