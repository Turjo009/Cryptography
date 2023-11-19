'''
Identifying Vulnerabilities in an Application

Problem 2


RULE: A strong password requires

1) a minimum of 8 Characters
2) at least one UpperCase Letter
3) at least one LowerCase Letter
4) at least one Number
5) at least one Special Character
6) no sequence of 3 or more repeating characters

'''
MIN_PW = 8

'''
Simple function to validate the password meets the 
specified criteria
'''

def ValidateStrongPassword(password):
    
    # Assume required characters not found
    upp = False
    low = False
    num = False
    spc = False
    cnt = False

    # Assume three repeating characters not found
    noRpt = True
    
    # Validate all conditions

    pwLen = len(password)
    if pwLen >= MIN_PW:
        cnt = True
        
    for eachChar in password:
        if eachChar in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upp = True
        elif eachChar in "abcdefghijklmnopqrstuvwxyz":
            low = True
        elif eachChar in "0123456789":
            num = True
        elif eachChar in "!@#$%^&*()_-=+/\';><,.>":
            spc = True
        else:
            continue
        '''
        check for triple repeats
        '''
    pos = 0
    for eachChar in password:
        if pos < pwLen - 2:
            if eachChar == password[pos+1] and eachChar == password[pos+2]:
                noRpt = False
            else:
                pos += 1
    
    if upp and low and num and spc and cnt and noRpt:
        return True
    else:
        return False
    
# Main Program Starts Here
#===================================

if __name__ == '__main__':
    
    '''
    Your next activity is as follows:
    1) Create a unit test for the above function and
       validate all conditions
    2) Identify and correct vulnerabilities
       and logic issues that are identified
    '''
    
    if ValidateStrongPassword("A11aBC!!11"):
        print("Strong")
    else:
        print("Weak")
        
    
