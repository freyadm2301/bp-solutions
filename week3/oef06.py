# Print alle getallen tussen 200 en 308 (grenzen inclusief) die deelbaar door 7 maar geen veelvoud van 5 zijn.
for getallen in range(200,309):
    if getallen%7 == 0 and getallen%5 != 0:
        print(getallen)