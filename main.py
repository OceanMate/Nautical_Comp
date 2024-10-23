from Constants import Constants
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.MovementSubsystem import MovementSubsystem
from receive_commands import receive_commands
import RPi.GPIO as GPIO
from time import sleep


class main:
    def __init__(self):
        sleep(10)
        # Create dictornary of subsystems
        GPIO.setmode(GPIO.BCM)
        
        
        subsystems = {}
        subsystems["Movement"] = MovementSubsystem()
        
        
        #self.commands = receive_commands()

        #self.loop()


    def loop(self):
        Shutdown = False
        
        while Shutdown == False:
            self.commands.requstCommands();
            Shutdown = self.commands.shutdown;

            # Call the periodic method of each subsystem
            for subsystem in self.subsystems:
                subsystem.periodic()
        

# Run the main class 
if __name__ == "__main__":
    main()
