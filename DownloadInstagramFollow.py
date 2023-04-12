import instaloader
import xlsxwriter
from getpass import getpass
from datetime import datetime

now = datetime.now()


L = instaloader.Instaloader()

#Login or load session


print("Enter Login Usernmame: ")
loginUsername = input()
print("Enter Login Password: ")
loginPassword = getpass()
L.login(loginUsername, loginPassword)

print("Target UserName")
TargetUsername = input()
print("1. Followers \n2. Following")
followersOrFollowing = input()

profile = instaloader.Profile.from_username(L.context, TargetUsername)


row = 0


if followersOrFollowing == "1":
    i = 1
    time = now.strftime("%d_%m_%Y %H_%M_%S")
    workbook = xlsxwriter.Workbook(profile.full_name + " " + time + " followers.xlsx")
    worksheet = workbook.add_worksheet()
    for followers in profile.get_followers():
        numofFollowers = profile.followers
        username = followers.username
        Name = followers.full_name
        verified = followers.is_verified
        worksheet.write(row, 0 , username)
        worksheet.write(row, 1 , Name)
        worksheet.write(row, 2, verified)
        print("Downloading: " , row+1 , "/", numofFollowers)
        row=row+1 
    workbook.close()
elif followersOrFollowing == "2":
    time = now.strftime("%d_%m_%Y %H_%M_%S")
    workbook = xlsxwriter.Workbook(profile.full_name + " " + time + " following.xlsx")
    worksheet = workbook.add_worksheet()
    for followees in profile.get_followees():
        numOfFollowees = profile.followees
        username = followees.username
        Name = followees.full_name
        verified = followees.is_verified
        worksheet.write(row, 0, username)
        worksheet.write(row, 1 , Name)
        worksheet.write(row, 2, verified)
        print("Downloading: " , row+1 , "/" , numOfFollowees)
        row=row+1
    workbook.close()
else:
    print("Not valid input")


