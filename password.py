# importing sleep from time module
from time import sleep

# Let's set a unique password
password = "Susheel@123"

# initial number of trials = 5
trials = 5

# Let's loop it 
while True:

    # Let's take input from the user for password
    user_password = input('please enter your password: ')

    # Let's compare both the password
    if password != user_password:
        
        # reduce the value by 1
        trials = trials - 1
        print('wrong password', trials, "trials left")
        
        if trials == 0:
            # print counting for 30 seconds
            # the phone has to remain locked for 30 seconds
            counting = 30
            while counting > 0:    
                print('Phone locked. Try again in', counting,'seconds.')
                counting = counting - 1
                sleep(1)
            
            trials = 5
        
    else:
        print('Welcome Susheel!')
        break
