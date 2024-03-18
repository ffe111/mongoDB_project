#! /usr/bin/env python3
"""
u1.py is mean UI
ui for main_menu 
use to get input and call func
"""
import sys
import re

def case1(*,client,session,db):
    print('Case1')
    return 

def case2(*,client,session,db):
    print('Case1')
    return 

def get_string(*,minlength,maxlength,pattern,prompt):
    import re
    while True:
        try:
            inval = input(prompt)
            slen = len(inval)
        except EOFError:                        # if they hit EOF key
            print()                             # set slen to 0
            slen = 0                            # to force a retry
        slen = len(inval)
        if (slen < minlength) or (slen > maxlength):
            print("Invalid num lenght input!")
            continue
        try:
            if pattern != None:
                if not re.match(pattern, inval):
                    print("Invalid pattern input!")
                    continue
        except Exception as e:
            print(f"Invalid regex :\n{e}")
            continue
        return inval

def get_choice(*, choicedata):
    base, groupsize, totalsize = 0, 10, len(choicedata["pairs"])
    while True:
        print(f"{choicedata['title']:^78s}\n")
        if base>0:                                # if we are not on first page of data
            print(f"{base: 3d}.  Previous page")  # create synthetic prevous page entry
        # show groupsize entries, starting at index base
        for i,pair in enumerate(choicedata["pairs"][base:base+groupsize], start=base+1):
            print(f"{i: 3d}.  {pair[0]:s}")
        if base+groupsize < totalsize:          # if we are not on last page of data
            i += 1
            print(f"{i: 3d}.  Next page")       # create synthetic next page entry
        i += 1
        print(f"{i: 3d}.  Exit\n")              # create synthetic exit entry
        try:
            inval = input(choicedata["prompt"]) # try to get user input
        except EOFError:                        # if they hit EOF key
            print()                             # set inval to None
            inval = None                        # which will cause a retry
        try:                                      
            choice = int(inval)                 # try to convert to an integer
        except (TypeError,ValueError) as xcpn:  # if it fails, then
            choice = -1                         # set to -1 which is never valid
        if not (base <= choice <= i):           # if not in the range of choices then
            print(f"Invalid choice '{inval}'!") # display error and try again
            continue
        if ((base > 0) and (choice == base)):   # if not first page but first choice on page
            base -= groupsize                   # then goto previous page
            continue
        if ((base+groupsize < totalsize) and    # if not last page but second-to-last choice on page
            (choice == i-1)):                   # then goto next page
            base += groupsize
            continue
        if choice == i:                         # if last choice on page
            return None                         # then return None
        # Ok, it is an actual choice, return the _id
        return choicedata["pairs"][choice-1][1]

def main_menu(*, mdata, client, session, db):
    while True:
        print("\n\n")
        print("="*70)
        print(f"\n{'Main Menu':^70s}\n")
        print("*"*70)
        for index, entry in enumerate(mdata,start=1):
            print(f"{index:d}.  {entry[0]:s}")
        print(f"{index+1:d}.  Exit\n")
        try:
            print("="*70)
            inval = input(f"Enter choice: ")
            print("\n\n")
        except EOFError:
            print()
            inval = None
        try:
            choice = int(inval)
        except (TypeError,ValueError) as xcpn:
            choice = 0        # 0 is never valid
        if not (1 <= choice <= (index+1)):
            print(f"Invalid choice '{inval}'!")
            continue
        if choice == index+1: # synthetic exit choice
            return EXIT_SUCCESS
        mdata[choice-1][1](client=client,session=session,db=db)  # call function associated with choice

def main():
    try:
        return main_menu(mdata=[("Dump Categories", case1),
                                ("Dump Locations", case2)],
                         client=None,session=None,db=None)
    except KeyboardInterrupt:
        # they hit ctl-c
        print("\nProgram Exit by user request ctl-c!")
        return EXIT_FAILURE
    
EXIT_SUCCESS=0 
EXIT_FAILURE=1
    
if __name__ == "__main__":
    raise SystemExit(main())