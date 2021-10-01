import serial, sys

ser=serial.Serial(sys.argv[1],sys.argv[2])
print("connected to: " + ser.portstr)
while True:
  try:
    line = ser.readline()
    print(line)
  except KeyboardInterrupt:
    print("KeyboardInterrupt")
    break
ser.close()
exit()