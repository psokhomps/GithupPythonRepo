from datetime import datetime
current_hour=datetime.now().hour
if 8 <= current_hour < 17:
	print("store is open")
else:
	print("store is close")
