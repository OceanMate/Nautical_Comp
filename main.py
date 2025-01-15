#from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.MovementSubsystem import MovementSubsystem
from server import ROVServer
from time import sleep
from pynput import keyboard
import sys


class main:
    def __init__(self):
        # Create dictornary of subsystems
        
        print("am here")
        
        
        self.subsystems = []
        self.subsystems.append(MovementSubsystem())
        
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()
        
        print("am here")

        # Create the server object
        self.server = ROVServer()
       
        self.loop()

    def loop(self):
        Shutdown = False
        
        while Shutdown == False:
            sleep(.001) 
            self.server.update()
            
            # Call the periodic method of each subsystem
            for subsystem in self.subsystems:
                subsystem.periodic()
                
    def shutdown(self):
        print("am here")
        for subsytem in self.subsystems:
            subsytem.end()
        sys.exit(0)
    
    def on_press(self,key):          
        if key == keyboard.Key.esc:
            self.shutdown()
            
    def on_release(self,key):
        pass
        

# Run the main class 
if __name__ == "__main__":
    main()
