class Message:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.body = ""
        
    def append(self, line):
        self.body += line + "\n"
        
    def toString(self):
        messageString = "From: {}\nTo: {}\n{}\n".format(self.sender, self.recipient, self.body)
        return messageString