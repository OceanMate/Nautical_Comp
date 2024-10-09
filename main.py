from Constants import Constants
from Subsystems.Modules.ApisqueenMotor import ApisqueenMotor
from Subsystems.MovementSubsystem import MovementSubsystem
from receive_commands import receive_commands


class main:
    def __init__(self):
        subsystems = {}
        subsystems["Movement"] = MovementSubsystem()
        commands = receive_commands()

        self.periodic()


    def periodic(self):

        while Shutdown == False:
            self.commands.requstCommands();
            Shutdown = self.commands.getShutdown();

            for subsystem in self.subsystems:
                subsystem.periodic()
        
    
    