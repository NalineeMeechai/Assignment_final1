from function import calculate

input_egg = input("กรอกจำนวนไข่ไก่ที่ลูกค้าต้องการ :")
try:
    try:
        input_egg = int(input_egg)
    except:
        input_egg = float(input_egg)
except:
    input_egg = str(input_egg)
result = calculate(input_egg)
print(result)



