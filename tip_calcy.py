import logging

logging.basicConfig(level=logging.INFO)

def tip_calculator(Bamount, rate=0.01):
    logging.info("Initializing the tip calculator")
    logging.info(f"Total Bill Amount is: {Bamount}")
    tip = Bamount * rate
    finalamount = Bamount + tip
    logging.info(f"Final amount for the order is {finalamount}")
    return tip, finalamount

def get_input():
    Bamount = float(input("Enter the total bill amount: "))
    return Bamount

Bamount = get_input()
tip, finalamount = tip_calculator(Bamount)
print(f"Tip: {tip}, Final Amount: {finalamount}")