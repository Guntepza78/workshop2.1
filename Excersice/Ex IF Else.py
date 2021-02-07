# ข้อที่1 จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้

# คะแนน 80 - 100 ได้ A
# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F

# และให้แสดงผลตามตัวอย่างด้านล่าง

# Enter your score: 49
# grade:  F

x = int(input("Enter You Score:"))

if x < 0:
    print("error")
elif x <= 49:
    print("grade: F")
elif x >= 50 and x < 55:
    print("grade: D")
elif x >= 55 and x < 60:
    print("grade: D+")
elif x >= 60 and x < 65:
    print("grade: C")
elif x >= 65 and x < 70:
    print("grade: C+")
elif x >= 70 and x < 75:
    print("grade: ")
elif x >= 75 and x < 80:
    print("grade: B+")
elif x >= 80 and x <= 100:
    print("grade: A")