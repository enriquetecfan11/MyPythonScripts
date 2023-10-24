import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
  # Pasamos de formato bytes a string para poder manipular mejor los datos
  data = ser.readline().decode("utf-8")
  temp = len(data)
  data01 = data[:temp - 12]
  print(data01)
