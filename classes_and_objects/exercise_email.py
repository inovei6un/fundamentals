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


emails = list()
line = input().split(' ')
while True:
    if line[0] == "Stop":
        break
    sender = line[0]
    receiver = line[1]
    content = line[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input().split(' ')

send_email = [emails[int(x)].send() for x in input().split(', ')]

for email in emails:
    print(email.get_info())
