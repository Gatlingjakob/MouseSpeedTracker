import pygame, time, math

#Pygame setup
pygame.init()
size = width, height = 1000, 1000
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)

#Amount of time between start and end coordinates are logged
waitingTime = 5
mouseLog = []

def Average(lst): 
    return sum(lst) / len(lst) 

def mouseSpeed():

    # Start
    data = pygame.mouse.get_pos()
    print("Start position: {0}".format(data))
    x1 = data[0] 
    y1 = data[1] 
    z1 = time.time()

    time.sleep(waitingTime)

    # Clear pygame event data
    for event in pygame.event.get():
        pass     

    # End
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
    deltaZ = z2 - z1

    # Get distance/change in time
    mouseSpeedUnits = math.ceil(distance/deltaZ)
    mouseLog.append(mouseSpeedUnits)
    # Print out the speed
    print ("I've traveled {0} Mouse Speed Units in the last {1} seconds".format(mouseSpeedUnits, waitingTime))
    average = Average(mouseLog)
    print("Current Average Speed:{0}".format(average))

    print(" ")
    
    # Clear pygame event data
    for event in pygame.event.get():
        pass            

#Infamous infinite loop
while True:
    mouseSpeed()
