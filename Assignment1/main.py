from uuid import uuid4

from datetime import datetime

n=input()
unique_id = str(uuid4())
# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Name:",n)
print("unique_id:",unique_id)
print("date and time:", dt_string)	
