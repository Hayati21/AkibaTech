destination = input("Enter your destination: ")
distance = float(input("Enter the distance in kilometer: "))
speed = float(input("Enter the average speed in kilometer per hour: "))

time = distance / speed

print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speed} km/h")

print(f"Estimated Travel Time: {time: .2f}hours")
