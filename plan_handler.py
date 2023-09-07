import sys

#this function reads the plan and returns a list of actions
def plan_reader(path):
    with open(path, 'r') as p: 
        lines = p.readlines()
        lines = [elem.strip().strip('()').split(' ') for elem in lines]
        return lines
    
#this dictionary contains the mapping from each action to the corresponding script path.
#when handling the pictures, we also pass the specific picture the robot should present
action_to_script = {
   'move' : "scripts/choice_room.py",
   'restroom' : "scripts/pipi.py",
   'assist_visitor_DETDUP_0' : ["scripts/presentazione_pictures.py", 'p 11'], 
   'assist_visitor_DETDUP_1' : ["scripts/presentazione_pictures.py", 'p 21'],
   'assist_visitor_DETDUP_2' : ["scripts/presentazione_pictures.py", 'p 31'],
   'assist_visitor_DETDUP_3' : ["scripts/presentazione_pictures.py", 'p 41'],
   'assist_visitor_DETDUP_4' : ["scripts/presentazione_pictures.py", 'p 12'],
   'assist_visitor_DETDUP_5' : ["scripts/presentazione_pictures.py", 'p 22'],
   'assist_visitor_DETDUP_6' : ["scripts/presentazione_pictures.py", 'p 32'],
   'assist_visitor_DETDUP_7' : ["scripts/presentazione_pictures.py", 'p 42'],
   'assist_visitor_DETDUP_8' : "scripts/museum_history.py",

}

#this function executes a single action
def execute_single_action(action):
    act = action[0]
    #move
    if (act == 'move'):
        place1 = action[2]
        place2 = action[3]
        sys.argv = [place1,place2]
        exec(open(action_to_script[act]).read())

    #restroom  
    elif( act == 'restroom'):
        exec(open(action_to_script[act]).read())
    #museum history
    elif( act == 'assist_visitor_DETDUP_8'):
        exec(open(action_to_script[act]).read())
    
    #pictures
    else:
        sys.argv = action_to_script[act][1]
        exec(open(action_to_script[act][0]).read())

    
        
    return 0


    
    


def main():
    lines= plan_reader('sas_plan') 
    for action in lines:
        execute_single_action(action)





main()







