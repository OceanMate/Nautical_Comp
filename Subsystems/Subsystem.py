# Each subsytem should inherit from this class 
# So each subsystem can have a periodic method that is called in the main loop
class Subsystem:
    def __init__(self):
        return
    
    def periodic(self):
        raise NotImplementedError("Subclasses should implement this!")

