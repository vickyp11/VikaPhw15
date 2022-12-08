"""
Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.


 class TVController:
pass
 controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"

"""


CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    current_channel = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        print('First channel:', self.channels[0])
        TVController.current_channel = 0

    def last_channel(self):
        print('Last channel:', self.channels[-1])
        TVController.current_channel = len(CHANNELS)

    def turn_channel(self, n):
        print('Turned channel:', self.channels[n-1])
        TVController.current_channel = n-1

    def next_channel(self):
        if TVController.current_channel < len(CHANNELS)-1:
            print('Next channel:', self.channels[TVController.current_channel + 1])
            TVController.current_channel +=  1
        else:
            print('Selected channel is out of the range, first channel:', self.channels[0])
            TVController.current_channel = 0

    def previous_channel(self):
        if len(CHANNELS)-1 > TVController.current_channel > 0:
            print('Previous channel:', self.channels[TVController.current_channel - 1])
            TVController.current_channel -= 1
        else:
            print('Selected channel is out of the range, last channel:', self.channels[-1])
            TVController.current_channel = len(CHANNELS)

    def current_channell(self):
        print('Current channel:', self.channels[TVController.current_channel])

    def is_exist(self, var):
        if type(var) == int:
            if len(self.channels) > int(var) >= 0:
                print('Yes!')
            else:
                print('No!')
        if type(var) == str:
            for names in self.channels:
                if var == names:
                    print('Yes!')
                    break
            else:
                print('No!')


contorller = TVController(CHANNELS)

contorller.first_channel()
contorller.last_channel()
contorller.turn_channel(1)
contorller.next_channel()
contorller.previous_channel()
contorller.current_channell()
contorller.is_exist(4)
contorller.is_exist('BBC')