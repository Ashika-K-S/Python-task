from abc import ABC,abstractmethod
class notification(ABC):
    @abstractmethod
    def send(self,message):
        pass
class Email(notification):
    def send(self,message):
        print(f"Email:{message}")
class SMS(notification):
    def send(self,message):
        print(f"SMS:{message}")
        
n=SMS()
n.send("Helooo")