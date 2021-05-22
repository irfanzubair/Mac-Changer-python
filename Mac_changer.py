# -----Created By Mr Irfan Zubair------
# Use This For Educational Purpose Only
# This is Mac Changer Program 
# ||==============||
# ||   *******    ||
# ||   Irfan      ||
# ||   Zubair     ||
# ||   *******    ||
# ||==============||
#/usr/bin/env python # Shabang
import subprocess #import module suprocess --> For execute commands
import optparse   #import module optparse  --> for getting arguments from user
import re         #import module re        --> regular expression 
def get_Arguments(): #define Function to get Argument From the user
    parser = optparse.OptionParser() #Option.Parser is a Class
    parser.add_option("-i","--interface",dest="interface",help="Change interface") # get First Argument
    parser.add_option("-m","--mac",dest="new_Mac",help="New Mac Address") #getting 2nd Argument
    (options,arguments)= parser.parse_args() # Store in Variables return Two Arguments Stored in Option which are entered By the User
    if not options.interface: # if User Could Not Give Interface after -i or --interface
        parser.error("[-] Please Specify an Interface") # gives error message
    if not options.new_Mac: # if user could not put mac address after -m or --mac
        parser.error("[-] Pleasse Specify a New Mac Address") # print error message
    return options # return options which have two arguments interface and mac
def change_Mac_Address(interface,new_Mac): # define function to execute commands (linux)
    print("[+] Changing Mac Address [+]")
    subprocess.call(["ifconfig",interface,"down"]) # ifconfig eth0,wlan0..etc down
    subprocess.call(["ifconfig",interface,"hw","ether",new_Mac]) #ifconfig eth0,wlan0..etc hw ether 00:00:00:00:00:00
    subprocess.call(["ifconfig",interface,"up"]) #ifconfig eth0,wlan0..etc up
    
def Check_Output(interface): # define function for Checking Output and reading
    ifconfig_result = subprocess.check_output(["ifconfig",interface]) # check output from command and stored in variable
    final_Result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result) # search from output with the pattern and stored in variable (pythex.org is a website for patterns)
    return final_Result.group(0) # return final result in group and (0) is the first similar group from pattern 
option = get_Arguments() # call arguments function
Check_Mac = Check_Output(option.interface) # getting mac address 
print("Current Mac Address :" + str(Check_Mac)) # print current mac address before changing
Mac = change_Mac_Address(option.interface,option.new_Mac) # changing mac address
New_mac = Check_Output(option.interface) # getting changed mac address
if New_mac == option.new_Mac: # mac address before changing and after changing , compare to each other
    print("[+] Mac Address Sucessfully Changed [+]") # if changed than print
    print("Current Mac Address :" + str(New_mac)) # prints mac address
else:  # if any error
    print("[-] Mac Address Could Not Changed Please Type Help [-]") # print this
