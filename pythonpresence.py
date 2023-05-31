from pypresence import Presence
import time

client_id = 'Your client_id ' #Yo client id jesse
RPC = Presence(client_id) # This is basic project 
RPC.connect() 

print(RPC.update(state="STATE", details="DETAILS", large_image="IMAGE-LARGE", small_image="SMAL-IMAGE", large_text="LARGE-IMAGE-TEXT", start=time.time())

while True: 
    time.sleep(15) 
