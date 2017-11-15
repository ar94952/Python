##
#  Anthony Rivera
#  CIS 117 OL
#
from AnthonyRiveraLab7 import Message

# Create the message.
wishList = Message("Anthony", "Santa")
wishList.append("For Christmas, I would like:")
wishList.append("Video games")
wishList.append("World peace")

# Display its contents.
print(wishList.toString())
