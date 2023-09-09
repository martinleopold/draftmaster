# HP Draftmaster I (HP7595A)

Paper Notes:
* Longer Axis is always X.
* Landscape: P1 bottom-left, P2 top-right, non-printable border at the bottom
* Portrait:  P1 top-left, P2 bottom-right, non-printable border at the bottom

Paper loading:
| Paper Size | Dimensions    | Loading Direction |
| ---------- | ------------- | ----------------- |
| A4         | 210 × 297 mm  | either            |
| ANSI A     | 216 × 279 mm  | either            |
| –          |               |                   |
| A3         | 297 × 420 mm  | portrait          |
| ANSI B     | 279 × 432 mm  | portrait          |
| –          |               |                   |
| A2         | 420 × 594 mm  | landscape         |
| ANSI C     | 432 × 559 mm  | landscape         |
| Arch C     | 457 × 610 mm  | landscape         |
| –          |               |                   |
| A1         | 594 × 841 mm  | either            |
| ANSI D     | 559 × 864 mm  | either            |
| Arch D     | 610 × 914 mm  | either            |
| –          |               |                   |
| A0         | 841 × 1189 mm | portrait          |
| ANSI E     | 864 × 1118 mm | portrait          |
| Arch E     | 914 × 1219 mm | portrait          |

Additional formats:
| Paper Size | Dimensions    | Loading Direction |
| ---------- | ------------- | ----------------- |
| 24 x 34    | 240 × 340 mm  | either            | * 
| 44 x 63    | 440 × 630 mm  | landscape         | *  todo: test portrait
| 50 x 65    | 500 × 650 mm  | landscape         | *  todo: test portrait
| 50 x 70    | 500 × 700 mm  | landscape         | *
| A1U        | 625 × 880 mm  | portrait          | *

(* ... tested)

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

