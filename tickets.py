#Name:George ibarra
#Date: 12/12/24

#Initialize
import turtle
t = turtle.Turtle()

#Functions

#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    t.penup()
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")

#Mainticket = 100
price=100
#draw_ticket(str("george"),int(10),str("monday"),int(55))
#Introduce the customer to your app:
print("welcome to dinosaur musuem ticket generator app")
#Collect the pertinet information Name,age,day of the week,coupon code
name = input("Enter Firstname: ")
age = int(input("Enter your age: "))
day = input("Please tell what day of week you're going: ")
coupon = input("Enter a coupon code if you have one please: ")
#3.Algorith for setting the price
if age <= 3:
    price = 0 #baby price
if age >= 4 and age <= 17 and day == "Monday"or day == "tuseday" or day == "wenesday" or day == "thursday" or day =="friday":
    price = 50
else:
    price = 100
if age >= 17:
    price= 100
if age >= 4 and age <= 17 and day == "friday" and coupon == "FREEFRIDAY":
    price=0
if age >= 4 and age <= 17 and day == "Sunday" and coupon == "SUNDAY10":
    price=90

print(price)

draw_ticket(str(name),int(price),str(day),int(0))
