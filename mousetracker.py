import pygame, time, math

# We will make a window with pygame to simulate a browser window
# Pygame setup
pygame.init()
size = width, height = 300, 300
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

# Amount of time between start and end coordinates are logged
waitingTime = 2

# List to store mouse speed values for calculation of average speed
mouseLog = []

def Average(lst): 
    return sum(lst) / len(lst) 

def mouseSpeed():
    # Get start position
    data = pygame.mouse.get_pos()
    print("Start position: {0}".format(data))
    x1 = data[0] 
    y1 = data[1] 
    z1 = time.time()

    time.sleep(waitingTime)

    # Clear pygame event data to store new value
    for event in pygame.event.get():
        pass     

    # Get end position 
    data = pygame.mouse.get_pos()
    print("End position: {0}".format(data))
    x2 = data[0]
    y2 = data[1] 
    z2 = time.time()

    # Determine distance traveled
    deltaX = x2 - x1
    deltaY = y2 - y1
    distance = math.sqrt( math.pow(deltaX, 2) + math.pow(deltaY, 2) ) # Distance between 2 points

    # Get the change in time 
    # the variable waitingTime would serve the same purpose, 
    # but chose to leave deltaZ in, in case I want to reuse the algorithm later
    # (Plus, there is a small, albeit insignificant, difference in milliseconds)
    deltaZ = z2 - z1

    # Get distance/time (pixels/seconds)
    mouseSpeedUnits = math.ceil(distance/deltaZ)
    mouseLog.append(mouseSpeedUnits)
    # Print out the speed
    print ("I've traveled {0} Mouse Speed Units in the last {1} seconds".format(mouseSpeedUnits, waitingTime))
    average = Average(mouseLog)
    print("Current Average Speed:{0}".format(average))
    print(" ")
    
    # Clear pygame event data to store new value
    for event in pygame.event.get():
        pass            

#Infamous infinite loop
while True:
    mouseSpeed()
