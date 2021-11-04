from models.order import *
import datetime

order1 = Order("John", datetime.date(2021, 4, 23), 3472, 2)
order2 = Order("Steven", datetime.date(2021, 2, 3), 3473, 4)

orders = [order1, order2]
