#from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.IMU import IMU
from Subsystems.MovementSubsystem import MovementSubsystem
from time import sleep
from transmission.ComsThread import ComsThread
from gpiozero import LED


class main:
    def __init__(self):
        imu = IMU()
        # Create dictornary of subsystems
        self.subsystems = dict(movement = MovementSubsystem(), imu = IMU())
        
        # Create the coms thread
        self.coms = ComsThread()
        self.coms.begin_thread()
        

        # Create the server object
        self.loop()

    def loop(self):
        Shutdown = False
    
        
        try:
            while Shutdown == False:
                sleep(.001) 
                
                # Call the periodic method of each subsystem
                for subsystem in self.subsystems.values():
                    subsystem.periodic()
        except KeyboardInterrupt:
            self.shutdown()
                
    def shutdown(self):
        for subsytem in self.subsystems.values():
            subsytem.end()
        print("am here")
    
        

# Run the main class 
if __name__ == "__main__":
    main()
