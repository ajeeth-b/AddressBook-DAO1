robot_x = 0
robot_y = 0
robot_facing = "NORTH"

def place(x,y,facing):
    global robot_x 
    robot_x = int(x)
    global robot_y
    robot_y = int(y)
    global robot_facing 
    robot_facing = facing    

def turnRight(facing):
    global robot_facing
    if(facing == "NORTH"):
        robot_facing = "EAST"
    if(facing == "WEST"):
        robot_facing = "NORTH"
    if(facing == "EAST"):
        robot_facing = "SOUTH"
    if(facing == "SOUTH"):
        robot_facing = "WEST"

def turnLeft(facing):
    global robot_facing
    if(facing == "NORTH"):
        robot_facing = "WEST"
    if(facing == "WEST"):
        robot_facing = "SOUTH"
    if(facing == "EAST"):
        robot_facing = "NORTH"
    if(facing == "SOUTH"):
        robot_facing = "EAST"

def move():
  if(robot_facing == "NORTH" and robot_y <3):
    robot_y += 1
  if(robot_facing == "SOUTH" and robot_y >0):
    robot_y -= 1
  if(robot_facing == "WEST" and robot_y > 0):
    robot_x -= 1
  if(robot_facing == "EAST" and robot_y <3):
    robot_x += 1
  return

global instruction
instruction = ""
while(instruction != "REPORT"):
    instruction 
    instruction = input()
    if("PLACE" in instruction):
        instruction = instruction[6:].split(",")
        place(instruction[0],instruction[1],instruction[2])
    elif(instruction.strip() == "LEFT"):
        turnLeft(robot_facing)
    elif(instruction.strip() == "RIGHT"):
        turnRight(robot_facing)
    else:
        move()   

print(robot_x)
print(robot_y)
print(robot_facing)
