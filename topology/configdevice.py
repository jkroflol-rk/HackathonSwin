# This is a sample Python script.
import serial
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def connectSerial():
    # creating your serial object
    ser = serial.Serial(
        port='COM7',  # COM is on windows, linux is different
        baudrate=9600,  # many different baudrates are available
        parity='N',  # no idea
        stopbits=1,
        bytesize=8,
        timeout=8  # 8 seconds seems to be a good timeout, may need to be increased
    )

    # open your serial object
    ser.isOpen()
    # in this case it returns str COM3
    print(ser.name)
    # first command (hitting enter)
    command = "\r\n"
    # convert str to binary (commands sent to switch must be binary)
    command = str.encode(command)
    # send the command to the switch
    ser.write(command)
    # wait a sec
    time.sleep(0.5)
    ser.inWaiting()
    # get the response from the switch
    input_data = ser.read(225)  # (how many bytes to limit to read)
    input_data = input_data.decode("utf-8", "ignore")
    # print response
    print(input_data)
    # create a loop
    while 1:
        command = input('')
        command = str.encode(command+'\r\n')
        ser.write(command)
        time.sleep(0.5)
        ser.inWaiting()
        output = ser.read(225)
        output = output.decode("utf-8","ignore")
        print(output)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    connectSerial()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
