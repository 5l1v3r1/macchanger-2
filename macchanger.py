import subprocess
import optparse

print("""_   _      _ _       _ _
| | | | ___| | | ___ | | |
| |_| |/ _ \ | |/ _ \| | |
|  _  |  __/ | | (_) |_|_|
|_| |_|\___|_|_|\___/(_|_)""")

def user_get_inputs():
  parse_object = optparse.OptionParser()
  parse_object.add_option("-i","--interface",dest="interface",help="please enter interface name")
  parse_object.add_option("-m","--mac",dest="mac_address",help="please enter new mac address")

  (user_inputs,arguments) = parse_object.parse_args()

#print(user_inputs.interface)
#print(user_inputs.mac_address)

#user_interface = user_inputs.interface
#user_mac_address = user_inputs.mac_address

#print("Macchanger Started")

#interface = "eth0"
#mac_address = "00:11:22:33:55:77"

def change_mac_address(user_interface,user_mac_address)
  subprocess.call(["ifconfig",user_interface,"down"])
  subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
  subprocess.call(["ifconfig",user_interface,"up"])
