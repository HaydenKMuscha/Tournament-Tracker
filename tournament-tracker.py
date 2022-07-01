#create start up
def start_up():
    title = str('Welcome to Tournaments R US')
    print(title)
    print('='*len(title))
    
    #get participant count
    global entries_count
    entries_count = int(input('Enter the number of participants: '))
    print(f"There are {entries_count} particapant slots ready for sing-ups.")

    #add to final_list
    global names_and_positions
    names_and_positions = []
    for n in range(entries_count):
        names_and_positions.append(None)

    # go to menu after getting entries
    menu()

def menu():
    title = str('Participant Menu')
    print(title)
    print('='*len(title)) 
    print('1. Sign Up')
    print('2. Cancel Sign Up')
    print('3. View Participants')
    print('4. Save Changes')
    print('5. Exit')

    menu_redirect = int(input('Enter the number (1-5) of where you would like to go: '))
    if menu_redirect ==1:
        sign_up()
    if menu_redirect ==2:
        cancel_sign_up()
    if menu_redirect ==3:
        view_participants()
    if menu_redirect ==4:
        save_changes()
    if menu_redirect ==5:
        exit()

#create sign_up
def sign_up():
    title = str('Participant Sign Up')
    print(title)
    print('='*len(title))
    
    #get name
    participant = str(input('Participant Name: '))
    
    #get desired position
    desired_position = int(input(f"Desired starting slot #[1-{entries_count}]: "))
    #checking spot availability
    if desired_position > entries_count or desired_position < 1:
        print('Error: ')
        print(f"That slot is not in the range of [1-{entries_count}]")
    elif names_and_positions[(desired_position-1)] is None:
        names_and_positions[(desired_position -1)] = str(desired_position) + ':' + participant
    else:
        print('Error: ')
        print(f"Slot #{desired_position} is filled. Please Try Again.")
    
    #asking for next action
    print('1. Enter another participant')
    print('2. Return to Participant Menu')
    sign_up_redirect = int(input('Make selection: '))
    if sign_up_redirect ==1:
        sign_up()
    elif sign_up_redirect ==2:
        menu()



#create cancel_sign_up
def cancel_sign_up():
    title = str('Participant Cancellation')
    print(title)
    print('='*len(title))

    desired_cancel_position = int(input(f"Starting slot #[1 - {entries_count}]: "))
    desired_cancel_participant = str(input('Participant Name: '))
    cancel_position_and_participant = names_and_positions[(desired_cancel_position-1)]
    participant = cancel_position_and_participant.split(':')[1]
    if participant == desired_cancel_participant:
        names_and_positions[(desired_cancel_position-1)] = None
        print('Success:')
        print(f"{desired_cancel_participant} has been cancelled from starting slot {desired_cancel_position}")
    else:
        print('Error: ')
        print(f"{desired_cancel_participant} is not in that starting slot.")
    print('1. Cancel another participant')
    print('2. Return to Participant Menu')
    cancel_sign_up_redirect = int(input('Make selection: '))
    if cancel_sign_up_redirect ==1:
        cancel_sign_up()
    elif cancel_sign_up_redirect ==2:
        menu()


#create view_participants
def view_participants():
    title = str('View Participants')
    print(title)
    print('='*len(title))
    view_position = int(input(f"Starting slot #[1-{entries_count}]: "))
    view_start = view_position - 5
    view_end = view_position + 5
    if view_start < 0:
        view_start = 0
    if view_end > entries_count:
        view_end = entries_count
    dislpay_participants = names_and_positions[view_start:view_end]
    for n in dislpay_participants:
        print(n)
    print('1. View another set of participants')
    print('2. Return to Participant Menu')
    view_participants_redirect = int(input('Make selection: '))
    if view_participants_redirect ==1:
        view_participants()
    elif view_participants_redirect ==2:
        menu()

#create save_changes
def save_changes():
    title = str('Save Changes')
    print(title)
    print('='*len(title))
    save_value = input('Save your changes to CSV? [y/n] ')
    if save_value == 'y':
        file = open('participant_list.csv', 'w')
        file.write(str(names_and_positions))
        file.close
        print('1. Save again?')
        print('2. Retutn to Participant Menu')
    else:
        print('1. Save file?')
        print('2. Retutn to Participant Menu')
    save_changes_redirect = int(input('Make selection: '))
    if save_changes_redirect ==1:
        save_changes()
    elif save_changes_redirect ==2:
        menu()

#create exit
def exit():
    title = str('Exit')
    print(title)
    print('='*len(title))
    print('Any unsaved changes will be lost.')
    exit_decision = input('Are you sure you want to exit? [y/n]: ')
    if exit_decision == 'y':
        print ('Goodbye!')
        exit
    else:
        menu()

start_up()