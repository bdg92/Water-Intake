import math
def water_intake(name ="Akash",weight = 70,workout = 30):
    result = weight /30 + workout*0.0113
    print("%s \nAccording to your body weight =%d Kgs.\nAnd your work out of %s minutes every day \nYour water intake should be = %.2f Liters per day.\nWhich is = %.2f Glasses per day" % (name,weight,workout,result,round(result/0.2)))
    
water_intake("Sandhya",50,0)