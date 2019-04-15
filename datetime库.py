from datetime import datetime
birthday = datetime(1999, 4, 24, 0, 0, 0)
s1, s2, s3, s4, s5,s6 = birthday.year, birthday.month, birthday.day, birthday.hour, birthday.minute, birthday.second
print("生日是{}".format(birthday))
print("生日是{}-{}-{}-{}:{}:{}".format(s1, s2, s3, s4, s5, s6))
print("生日是{}".format(birthday.isoformat()))
print("生日是{}".format(birthday.strftime("%Y-%m-%d %H:%M:%S")))
