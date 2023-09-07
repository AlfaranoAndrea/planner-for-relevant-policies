import sys

#this function reads the plan and returns a list of actions
def plan_reader(path):
    with open(path, 'r') as p: 
        lines = p.readlines()
        lines = [elem.strip().strip('()').split(' ') for elem in lines]
        #['move agent p0 task', 'restroom agent vis1', 'assist_visitor_DETDUP_0 agent vis1 task']
        return lines
    
#this dictionary contains the mapping from each action to the corresponding script path
action_to_script = {
   'move' : "scripts/choice_room.py",
   'restroom' : "scripts/pipi.py",
   'assist_visitor_DETDUP_0' : ["scripts/presentazione_pictures.py", 'p 1_1'], 
   'assist_visitor_DETDUP_1' : ["scripts/presentazione_pictures.py", 'p 1_2'],
   'assist_visitor_DETDUP_2' : ["scripts/presentazione_pictures.py", 'p 1_3'],
   'assist_visitor_DETDUP_3' : ["scripts/presentazione_pictures.py", 'p 1_4'],
   'assist_visitor_DETDUP_4' : ["scripts/presentazione_pictures.py", 'p 2_1'],
   'assist_visitor_DETDUP_5' : ["scripts/presentazione_pictures.py", 'p 2_2'],
   'assist_visitor_DETDUP_6' : ["scripts/presentazione_pictures.py", 'p 2_3'],
   'assist_visitor_DETDUP_7' : ["scripts/presentazione_pictures.py", 'p 2_4'],
   'assist_visitor_DETDUP_8' : "scripts/museum_history.py",

}

#this function executes a single action
def execute_single_action(action):
    act = action[0]
    if (act == 'move'):
        place1 = action[2]
        place2 = action[3]
        sys.argv = [place1,place2]
        exec(open(action_to_script[act]).read())
 
        #os.system('python3' + ' ' + action_to_script[act] + ' ' + place)
        #exec(open(action_to_script[act]).read(),)
        
    elif( act == 'restroom'):
        exec(open(action_to_script[act]).read())

    elif( act == 'assist_visitor_DETDUP_8'):
        exec(open(action_to_script[act]).read())
    
    #pictures
    else:
        sys.argv = action_to_script[act][1]
        exec(open(action_to_script[act][0]).read())

    
        

    
    #print(action_to_script[act])
    #exec(open(action_to_script[act]).read())
    return 0


    
    



def main():
    #reading the plan
    lines= plan_reader('sas_plan') #TODO: insert path of the file 'sas_plan'
    #executing the actions in the plan
    for action in lines:
        execute_single_action(action)





main()







