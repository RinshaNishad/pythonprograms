users=["sachin","kohli","sehwang","rahul","dhoni","raina"]
sachin_followers=["kohli","sehwang","rahul"]
new_frnds=[]
for user in users:
    sachin_followers.append(user) if user in sachin_followers else new_frnds.append(user)
print("possible frnd rqsts :",new_frnds)


