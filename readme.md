# HP Draftmaster I (HP7595A)

Paper Notes:
* Longer Axis is always X.
* Landscape: P1 bottom-left, P2 top-right, non-printable border at the bottom
* Portrait:  P1 top-left, P2 bottom-right, non-printable border at the bottom

Paper loading:
* A4: landscape
* A3: portrait
* A2: landscape
* A1: ?
* A0: ?

Serial cable requirements:
* Plotter port (labeled "Computer/Modem"): Female DB-25, RS232-C/CCITT V.24 
* Computer side (Serial to USB Adapter): Male DB-9

Cable (Null Modem)
Sender DB-9 female  -> Receiver DB25 male

|     | DB25 | DE9 | –> | DB25 | DE9 |     |
| --- | ---- | --- | -- | ---- | --- | --- |
| GND |  7   |  5  |    |  7   |  5  | GND |
| TX  |  2   |  3  |    |  3   |  2  | RX  |
| RX  |  3   |  2  |    |  2   |  3  | TX  |
| –   |      |     |    |      |     |     |
| RTS |  4   |  7  |    |  5   |  8  | CTS |
| CTS |  5   |  8  |    |  4   |  7  | RTS |
| –   |      |     |    |      |     |     |
| DTR |  20  |  4  |    |  6   |  6  | DSR |
| DSR |  6   |  6  |    |  20  |  4  | DTR |

-> Crossed RX/TX, RTS/CTS, DTR/DSR

DB25 5+6 are connected (comp side)

Plotter supports DTR/DSR hardwire handshake:
* Plotter sets DTR high to signal the computer to send data
* Plotter sets DTR low when buffer reaches a threshold level

pyserial: can set RTS and DTR line

does pyserial really set: RTS and DTR?
* RTS: on 10V, off -9.6V
* DTR: on 10V, off -9.6V  
-> YES

does pyserial really receive: CTS and DSR?
* CTS receives 10V, -9.V (from RTS)
* DSR: receives 10V, -9.6V (from RTS)  
-> YES

does pyserial stop sending, when CTS / DSR is going low?
* CTS: 
* DSR:  
-> test with loopback cable (RX + TX, RTS + CTS, DSR + DTR)

