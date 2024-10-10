from Constants import Constants
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.MovementSubsystem import MovementSubsystem
from receive_commands import receive_commands


class main:
    def __init__(self):
        # Create dictornary of subsystems
        subsystems = {}
        subsystems["Movement"] = MovementSubsystem()
        
        self.commands = receive_commands()

        self.loop()


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