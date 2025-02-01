#from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.IMU import IMU
from Subsystems.MovementSubsystem import MovementSubsystem
from time import sleep
from pynput import keyboard
from transmission.ComsThread import ComsThread
import sys
from gpiozero import LED


class main:
    def __init__(self):
        imu = IMU()
        # Create dictornary of subsystems
        self.subsystems = dict(movement = MovementSubsystem(), imu = IMU())
        
        # Create the coms thread
        self.coms = ComsThread()
        self.coms.begin_thread()
        
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

        # Create the server object
        self.loop()

    def loop(self):
        Shutdown = False
    
        
        #try:
        while Shutdown == False:
            sleep(.001) 
            
            # Call the periodic method of each subsystem
            for subsystem in self.subsystems.values():
                subsystem.periodic()
        #finally:
            #self.shutdown()
                
    def shutdown(self):
        for subsytem in self.subsystems.values():
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
