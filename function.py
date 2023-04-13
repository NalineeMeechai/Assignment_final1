def calculate(input_egg):
    sum=0
    amount=0
    amount_=0
    price=0
    if type(input_egg) == int:
        if input_egg != 0:
            if input_egg < 60:
                amount = input_egg % 12
                amount_ = input_egg - amount
                sum = amount_ * 3
                price = (amount * 4) + sum
                return (price)
            elif input_egg >= 60:
                amount = input_egg % 12
                amount_ = input_egg - amount
                sum = (input_egg // 12) *35
                price = (amount * 4) + sum
                return (price)
        else:
            return "กรุณากรอกตั้งแต่ 1 ฟองขึ้นไป"
    elif type(input_egg) == str:
        return "กรุณากรอกเป็นตัวเลข"
    elif type(input_egg) == float :
        return "กรุณากรอกเป็นจำนวนเต็มบวก"




 