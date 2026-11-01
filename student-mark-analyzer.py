s1_name = input("Enter student 1 name")
s2_name = input("Enter student 2 name")
s3_name = input("Enter student 3 name")

sub1 = 'Telugu'
sub2 = 'Hindi'
sub3 = 'English'
sub4 = 'Maths'
sub5 = 'science'

print(f"\n--- Enter Marks for {s1_name} ---")
s1_t = int(input(f"Enter {sub1} marks: "))
s1_h = int(input(f"Enter {sub2} marks: "))
s1_e = int(input(f"Enter {sub3} marks: "))
s1_m = int(input(f"Enter {sub4} marks: "))
s1_s = int(input(f"Enter {sub5} marks: "))

print(f"\n--- Enter Marks for {s2_name} ---")
s2_t = int(input(f"Enter {sub1} marks: "))
s2_h = int(input(f"Enter {sub2} marks: "))
s2_e = int(input(f"Enter {sub3} marks: "))
s2_m = int(input(f"Enter {sub4} marks: "))
s2_s = int(input(f"Enter {sub5} marks: "))

print(f"\n--- Enter Marks for {s3_name} ---")
s3_t = int(input(f"Enter {sub1} marks: "))
s3_h = int(input(f"Enter {sub2} marks: "))
s3_e = int(input(f"Enter {sub3} marks: "))
s3_m = int(input(f"Enter {sub4} marks: "))
s3_s = int(input(f"Enter {sub5} marks: "))

s1_total = s1_t + s1_h + s1_e + s1_m + s1_s
s2_total = s2_t + s2_h + s2_e + s2_m + s2_s
s3_total = s3_t + s3_h + s3_e + s3_m + s3_s

if s1_t >= 35 and s1_h >= 35 and s1_e >= 35 and s1_m >= 35 and s1_s >= 35:
    s1_status = "PASS"
else:
    s1_status = "FAIL"

if s2_t >= 35 and s2_h >= 35 and s2_e >= 35 and s2_m >= 35 and s2_s >= 35:
    s2_status = "PASS"
else:
    s2_status = "FAIL"

if s3_t >= 35 and s3_h >= 35 and s3_e >= 35 and s3_m >= 35 and s3_s >= 35:
    s3_status = "PASS"
else:
    s3_status = "FAIL"
  
print("\n==============================")
print("          REPORT CARD         ")
print("==============================")
print(f"1. {s1_name} -> Total Marks: {s1_total}/500 | Status: {s1_status}")
print(f"2. {s2_name} -> Total Marks: {s2_total}/500 | Status: {s2_status}")
print(f"3. {s3_name} -> Total Marks: {s3_total}/500 | Status: {s3_status}")
print("==============================")

if s1_total >= s2_total and s1_total >= s3_total:
    print(f"🏆 First Rank: {s1_name} ({s1_total} Marks)")
elif s2_total >= s1_total and s2_total >= s3_total:
    print(f"🏆 First Rank: {s2_name} ({s2_total} Marks)")
else:
    print(f"🏆 First Rank: {s3_name} ({s3_total} Marks)")
print("==============================")