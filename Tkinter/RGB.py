import tkinter as tk
import serial

# Connect to the Arduino serial port
ser = serial.Serial('COM2', 9600)  # Replace 'COM3' with the appropriate port and baud rate

# Define the GUI window
window = tk.Tk()
window.title("RGB LED Control")

# Function to send RGB values to Arduino
def send_rgb(value):
    # Get the RGB values from the sliders
    red_value = red_slider.get()
    green_value = green_slider.get()
    blue_value = blue_slider.get()

    # Create the RGB string to send to Arduino
    rgb_string = str(red_value) + ',' + str(green_value) + ',' + str(blue_value)

    # Send the RGB string to Arduino
    ser.write(rgb_string.encode())

# Create the red slider
red_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Red",
                      length=200, command=send_rgb)
red_slider.pack()

# Create the green slider
green_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Green",
                        length=200, command=send_rgb)
green_slider.pack()

# Create the blue slider
blue_slider = tk.Scale(window, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue",
                       length=200, command=send_rgb)
blue_slider.pack()

# Start the Tkinter event loop
window.mainloop()
