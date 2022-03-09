from datetime import datetime
import pytz

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de Mexico: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))