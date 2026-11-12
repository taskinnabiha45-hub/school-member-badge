member_name = input("Enter your name : ")
club_name = input("Enter your club name : ")

member_number = 8
points = 9.5
is_active = True 

print("Member Number : ", member_name, "--> type : ", type(member_name))
print("Points : ", points, "--> type : ", type(points))
print("Active : ", is_active, "--> type : ", type(is_active))

badge_code = member_name[0:3] + club_name[-1:] + str(member_number)

print("Badge Code : ", badge_code)

print(" ")
print("===== CLUB BADGE =====")
print("Member : " + member_name)
print("Club : " + club_name)
print("Code : " + badge_code)
print("Points : " + str(points) + " | Active : " + str(is_active))