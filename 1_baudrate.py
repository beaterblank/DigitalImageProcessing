from math import log2,ceil
print()
b = int(input("Baud rate (b) = "))
w = int(input("Width (w) = "))
h = int(input("Height(h) = "))
l = int(input("Intensity levels (l) =  "))
#default transmission is assumed as 1 start bit 8 data bits 1 end bit
end =2
p = w*h
print(f"\nnumber of pixels (p) = w*h = {w}*{h} = {p}")
bits_per_pixel = ceil(log2(l))*(1+2/8)
print(f"\nbits per pixel = ceil(log2(l))+{end} ({int(end/2)} start and {int(end/2)} stop bit) = {bits_per_pixel}")
data = p*bits_per_pixel
print(f"\ntotal data = number of pixels * bits per pixel = {data}")
time_sec =  data/b
print(f"\nhence time taken = data/baudrate = {time_sec:.3f} s",end = " = ")
time_min = time_sec/60
print(f"{time_min:.3f} min")
input("\npress enter to exit...")