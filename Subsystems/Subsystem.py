class Subsystem:
    def __init__(self, name):
        self.name = name

    def onEnable(self):
        raise NotImplementedError("Subclasses should implement this!")
    
    def periodic(self):
        raise NotImplementedError("Subclasses should implement this!")
            
    def onDisable(self):
        raise NotImplementedError("Subclasses should implement this!")

