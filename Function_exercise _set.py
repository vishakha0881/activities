'''
Problem 2:

Chit Chat Application - Function:

(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.


(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words.
'''

def check_message_length(message):
    if len(message) <= 200:
        return message
    else:
        return message[:200]

message = "Hello, how are you? This is a message that is longer than 200 characters. I hope this function works correctly."
new_message = check_message_length(message)
print(new_message)




