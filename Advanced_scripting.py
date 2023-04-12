'''Case: We have an admission counsellor who wants to deliver a bulk message.

To the corresponding students with similar context, the admission counsellor asked a team of developers in EN2004 to help them creating a mechanism to deliver the same with an application that has a form like structure wherein
The counsellor can update the asked fields and messages will be processed.


names = # get and process input for a list of names
Admission_ID = # get and process input for a list of the number of admission ID
 CAP_Rank = # get and process input rank of the student in CAP # Information to be sent to be used for each student
# HINT: use .format() with this string in your for loop
'''

message = "Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship. \n\n" # write a for loop that iterates through each set of names, Admission_ID, and CAP ranks to print each student's message.

names = list(input().split(","))
ID = list(input().split(","))
CAP_Rank = list(input().split(","))
print("\n")
message = "Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit your academic credential including primary and secondary certificates. Your admission ID is {} and will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents on time and process university might offer you a scholarship. \n\n" # write a for loop that iterates through each set of names, Admission_ID, and CAP ranks to print each student's message.
for i in range(len(names)):
    a = names[i]
    b = ID[i]
    c = CAP_Rank[i]
    print(message.format(a,a,b,c))