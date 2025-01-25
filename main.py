#from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems import IMU
from Subsystems.MovementSubsystem import MovementSubsystem
from server import ROVServer
from time import sleep
from pynput import keyboard
import sys
from gpiozero import LED


class main:
    def __init__(self):
        
        # Create dictornary of subsystems
        self.subsystems = []
        self.subsystems.append(MovementSubsystem())
        #self.subsystems.append(IMU())
        
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()
        

        # Create the server object
        self.server = ROVServer()
       
        self.loop()

    def loop(self):
        Shutdown = False
    
        
        #try:
        while Shutdown == False:
            sleep(.001) 
            self.server.update()
            
            # Call the periodic method of each subsystem
            for subsystem in self.subsystems:
                subsystem.periodic()
        #finally:
            #self.shutdown()
                
    def shutdown(self):
        
        for subsytem in self.subsystems:
            subsytem.end()
        print("am here")
        sys.exit()
    
    def on_press(self,key):          
        if key == keyboard.Key.esc:
            self.shutdown()
            
    def on_release(self,key):
        pass
        

# Run the main class 
if __name__ == "__main__":
    main()
