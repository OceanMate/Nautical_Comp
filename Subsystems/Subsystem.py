# Each subsytem should inherit from this class 
# So each subsystem can have a periodic method that is called in the main loop
class Subsystem:
    # Why does this exist? You are not using it and others are using supers to access it
    # Max you f*cking moron
    
    
    def __init__(self):
        return
    
    def periodic(self):
        raise NotImplementedError("Subclasses should implement this!")

    def end(self):
        raise NotImplementedError("Subclasses should implement this!")
