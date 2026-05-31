import logging

logging.basicConfig(level=logging.INFO)
def tip_calculator(Bamount, rate=0.01):
    logging.info(f"Initializing the tip calulator")
    logging.info(f"Total Bill Amount is: {Bamount}")
    tip=Bamount*rate
    finalamount=Bamount+tip
    logging.info(f"Final amount for the order is {finalamount}")
    
Bamount=float(input(f"Emter the Bill Amount:"))
print(tip_calculator(Bamount))


