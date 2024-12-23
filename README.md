# 4 layer test-board for the XC5VLX30T-1FF665I-ND
schematic & pcb designed in Kicad 8
>This is a work in progress, i will update again after completing the bga reball work and confirming if the chips respond to jtag
>- capcaitor footprints not finalized (may need more depending on what testing reveals)
<br><br>

This project's goal is to fan out as many I/O pins as possible on the Virtex-5 665 BGA , 1mm pitch footprint, using a standard PCB service without any special work. This means:
- 0.3 drill size vias
- 0.15mm track spacing & track width
- 0.2mm copper-to-hole clearance
- 4 layers, 1oz
- NO microvia, blind via, buried via
- NO via-in-pad

With these constraints, I was able to pull 215 I/O pins on a standard 4-layer board.  
Warning: This design is on the extreme edge of "not following the manufacturers PCB design recommendations" with regards to the signal and power delivery
I'm not certain if this will work for any practical design (VGA, Ethernet, DDR-SDRAM). However it should be acceptable for hobby work and experimenting.
I initially planned to interface this Virtex-5 FPGA with some 3.3v cmos buffers and logic gates, high-speed wasn't a concern.
If the scrap-recovered chips i have respond & work, this design could be easily converted to a 6-layer to improve power plane & signal
<br><br>

# pcb ordering & build
For this 4-layer version, i had [PCBWay](https://www.pcbway.com/) build it and i put together a youtube video of what it looks like
- Current pcbway board - https://www.youtube.com/watch?v=_ErQVJeHTFE , here I am showing some close up photos reviewing what was built and received. In this video i can confirm what pcbway's capabilities are on standard pcb service, specifically in this board design there is some critical areas around hole drill precision & plating for the vias. the precision by pcbway will allow to use 0.15mm copper clearance in this design and can see in this video link.
- PCBWay by default offered 1oz copper on inner & outer layers, which gave more current carrying capability for VCCINT and VCCO
- order sheet for PCBWay - https://github.com/xp5-org/Virtex5-XC5VLX30T-test-board/blob/main/pcbway_4layer_order.png , this is using default options for 4-layer with the exception of trace width & spacing has been specified to 5mil
<img width="500" alt="Screenshot 2024-12-02 at 1 48 46 AM" src="https://github.com/user-attachments/assets/aac8b5e0-8785-4a2b-a3d7-b07fbdbf5366">

 
<br><br>

# Current Status
- this is the basic idea of what i'm working with. a Xilinx programmer is $30+ and a raspi with [XC3SPROG](https://xc3sprog.sourceforge.net/hardware.php) is $5
- the raspi will have to live on this device and use the jtag header to program the virtex5 on each use or powerup.
- There is a lot of I/O, but there's nothing else. no ram, no EPROM, no flash.
![rough_IDEA](https://github.com/user-attachments/assets/a32fb95d-40cd-4d11-b74d-ede6dcb3908c)

<br><br>

Power:  The virtex5 here needs 1.0V, 2.5V, and 3.3V
- I'm starting off with the MP2307 buck converter, its an inexpensive (and discontinued) chip found in the mini360 modules
- SMD version : https://github.com/xp5-org/Virtex5-XC5VLX30T-test-board/tree/main/XC5VLX30T_testboard/buck_converter_mp2307
- Through-hole version: https://github.com/xp5-org/Virtex5-XC5VLX30T-test-board/tree/main/XC5VLX30T_testboard/mp2307_tht

<br><br>

Next steps for testing:
- build the MP2307 buck converters
- reball the virtex5's using 0.6mm lead balls
 
<br><br><br><br>
# kicad screenshots of each layer
<br><br>

<img width="895" alt="Screenshot 2024-10-20 at 9 57 44 PM" src="https://github.com/user-attachments/assets/5237cbdb-3e79-46d2-b88a-ed134af67141">
JTAG pins on the rear, clock and capacitors on the bottom GND plane side
headers for buck converters at the top of the board

<img width="994" alt="Screenshot 2024-10-20 at 9 58 12 PM" src="https://github.com/user-attachments/assets/7e23054e-d042-4f56-98db-b3151cc0618d">


Top Layer:

<img width="994" alt="Screenshot 2024-10-20 at 9 54 24 PM" src="https://github.com/user-attachments/assets/4c1df15d-8473-48cd-8a6b-9347bee68008">

2nd Layer:

<img width="994" alt="Screenshot 2024-10-20 at 9 54 59 PM" src="https://github.com/user-attachments/assets/004f34c5-8d35-4b16-a202-3fb5f1f38904">

3rd Layer:

<img width="994" alt="Screenshot 2024-10-20 at 9 55 11 PM" src="https://github.com/user-attachments/assets/262be93a-e25c-4354-8af1-6947c824e7b4">

4th Layer:

<img width="994" alt="Screenshot 2024-10-20 at 9 55 38 PM" src="https://github.com/user-attachments/assets/24cdeef5-b592-4144-9454-00349dcb80cf">





