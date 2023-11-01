class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


final_emails = []
information = input()
while information != "Stop":
    sender, receiver, content = information.split()
    email_info = Email(sender, receiver, content)
    final_emails.append(email_info)

    information = input()

indexes = [int(index) for index in input().split(", ")]
for index in indexes:
    final_emails[index].send()
for email in final_emails:
    print(email.get_info())