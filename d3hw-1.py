#Import module(library) 
import os

#Declare function name as clear_output to call in code using <clear_output()> with lamba perameters to support multiple operating systems
clear_output = lambda: os.system('cls' if os.name in ('nt') else 'clear')

#Function to add shopping list items and quantities into a library
def add_list_item(item, quantity):
    shopping_list[item] = quantity

#Start with an empty library for shopping list
shopping_list = {} 

#While loop to prompt user input for a task command
while True:
    
    task_prompt = input('SHOPPING LIST BUDDY Task Menu\nWhat would you like to do with your list?\nAdd/Show/Delete/Quit\n')
    
    #Add item prompt
    if task_prompt.lower() == 'add':
        clear_output()
        item_name_input = input('Add an item to your shopping list or type "back" to return to Task Menu\n')
        
        if item_name_input.lower() == 'back':
            clear_output()
            break
            
        if item_name_input.isdigit():
            print('Don\'t be silly, gorcery stores don\'t sell numbers!')
            continue
        else:    
            item_qt_input = input(f'How many units of {item_name_input} do you need?:\n')
        
        if item_qt_input.isdigit():
            print(f'Ok, let\'s add {item_qt_input} {item_name_input} to the shopping list...\n')
            add_list_item(item_name_input, item_qt_input)
        else:
            print(f'Please enter an integer for number of {item_name_input} you want to add')
        
        
    #Delete item prompt
    elif task_prompt.lower() == 'delete':
        clear_output()
        item_delete = input('What item would you like to remove?:\nType "back" to return to Task Menu\n')
        deleted_item =shopping_list.pop(item_delete)
              
        if item_delete.lower() == 'back':
            continue

    #Show current list prompt    
    elif task_prompt.lower() == 'show':
        clear_output()
        print('Current shopping list:\n')
        for k,v in shopping_list.items():
             print(f'{v} x {k}')
        print('-----')      

    #Close SHOPPING LIST BUDDY and clear shopping_list for next use prompt    
    elif task_prompt.lower() == 'quit':
        clear_output()
        print('Final shopping list:\n')
        for k,v in shopping_list.items():
             print(f'{v} x {k}')
        break

    #Invalid prompt user input echos user input with error message
    else:
        clear_output()
        print(f'-----\nI\'m sorry, "{task_prompt}" is not a valid command, please try again.\n-----')
    