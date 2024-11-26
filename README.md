a 4 layer test-board for the XC5VLX30T-1FF665I-ND using Kicad 8
<br><br>
This is a work in progress, i will update again after completing the bga reball work and confirming if the chips respond to jtag
<br><br>
This projects goal was to fan out as many I/O pins as possible on the Virtex-5 665 BGA , 1mm pitch footprint, using a standard PCB service without any special work. This means:
- 0.3 drill size vias
- 0.15mm track spacing & track width
- 4 layers
- NO microvia, blind via, buried via
- NO via-in-pad

With these constraints, I was able to pull 215 I/O pins on a standard 4-layer board.  
Warning: This design is on the extreme edge of "not following the manufacturers PCB design recommendations" with regards to the signal and power delivery
Im not certain if this will work for any practical design (VGA, Ethernet, DDR-SDRAM). However it should be acceptable for hobby work and experimenting. 
I initially planned to interface this Virtex-5 FPGA with some 3.3v cmos buffers and logic gates, high-speed wasn't a concern. 
If the scrap-recovered chips i have respond & work, this design could be easily converted to a 6-layer to improve power plane & signal 
<br><br>

For this 4-layer version, i had pcbway build it and i put together a youtube video of what it looks like here 
- Current board revision (Built by PCBWay) https://www.youtube.com/watch?v=_ErQVJeHTFE
- PCBWay by default offered 1oz copper on inner & outer layers, which gave more current carrying capability for VCCINT and VCCO
<br><br>
Next steps for testing:
- the next step is to reball these, solder them and test. 
  
<br><br>

Current Status:
- this is the basic idea of what i'm working with. a Xilinx programmer is $30+ and a raspi with [XC3SPROG](https://xc3sprog.sourceforge.net/hardware.php) is $5
- the raspi will have to live on this device and use the jtag header to program the virtex5 on each use or powerup.
- There is a lot of I/O, but theres nothing else. no ram, no EPROM, no flash. 
![rough_IDEA](https://github.com/user-attachments/assets/a32fb95d-40cd-4d11-b74d-ede6dcb3908c)

<br><br>

Power:  The virtex5 here needs 1.0V, 2.5V, and 3.3V 
- I'm starting off with the MP2307 buck converter, its an inexpensive (and discontinued) chip found in the mini360 modules 
- SMD version : https://github.com/xp5-org/Virtex5-XC5VLX30T-test-board/tree/main/XC5VLX30T_testboard/buck_converter_mp2307
- Through-hole version: https://github.com/xp5-org/Virtex5-XC5VLX30T-test-board/tree/main/XC5VLX30T_testboard/mp2307_tht


<br><br><br><br>
kicad screenshots of the various layers
<br><br>

<img width="895" alt="Screenshot 2024-10-20 at 9 57 44 PM" src="https://github.com/user-attachments/assets/5237cbdb-3e79-46d2-b88a-ed134af67141">
JTAG pins on the rear, clock and capacitors on the bottom GND plane side
headers for buck converters at the top of the board

<img width="994" alt="Screenshot 2024-10-20 at 9 58 12 PM" src="https://github.com/user-attachments/assets/7e23054e-d042-4f56-98db-b3151cc0618d">


Top Layer:

<img width="938" alt="Screenshot 2024-10-20 at 9 54 24 PM" src="https://github.com/user-attachments/assets/4c1df15d-8473-48cd-8a6b-9347bee68008">

2nd Layer:

<img width="765" alt="Screenshot 2024-10-20 at 9 54 59 PM" src="https://github.com/user-attachments/assets/004f34c5-8d35-4b16-a202-3fb5f1f38904">

3rd Layer:

<img width="761" alt="Screenshot 2024-10-20 at 9 55 11 PM" src="https://github.com/user-attachments/assets/262be93a-e25c-4354-8af1-6947c824e7b4">

4th Layer:

<img width="762" alt="Screenshot 2024-10-20 at 9 55 38 PM" src="https://github.com/user-attachments/assets/24cdeef5-b592-4144-9454-00349dcb80cf">
