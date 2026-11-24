# Stanford Research System SR245
The board has two LEDs and ten BNC connectors, eight analog and two digital.
It is a Computer Interface Module for the SR200 series NIM (Nuclear Instrumentation Module)

## Documentation
- [thinksrs.com](https//thinksrs.com)

## Features
- RS-232 110-19200 bps
- IEEE-488
- 8 BNC analog ADC or DAC
- 2 TTL I/O or trigger (?)
- +12V/-12V, +24V/-24V


## ICs
- Mostek MK3880-4 (Z80 CPU)
- Intel 8251A (USART)
- NEC D8253C-2 (Programmable Interval Timer: Intel 8253)
- AMD2764ADC (8kB EPROM)
- Sony CXK5864PN-12L (8kB SRAM)
- Motorola MC68488P (IEEE-488 controller)

## U2
SR245 firmware v3.6, Copyright 1985 by Stanford Research. Checksum `96B0`
- [AM2764A@DIP28.BIN](./AM2764A@DIP28.BIN)

## Memory map
TBD

## Commands
See manual: [SR245c.pdf](./docs/SR245c.pdf)

# Baud rates
Prelimenary (may be wrong) SW2 settings. Note `1` on the switch block is BIT0.

| BIT | Function      |
| :-: | :------------ |
|  0  | baudrate      |
|  1  | baudrate      |
|  2  | baudrate      |
|  3  | even parity   |
|  4  | parity enable |
|  5  | stop bits     |
|  6  | IEEE-488?     |
|  7  | IEEE-488?     |

| BIT2-0 | Baud rate |
| :----: | --------: |
|   000  |       110 |
|   001  |       300 |
|   010  |       600 |
|   011  |      1200 |
|   100  |      2400 |
|   101  |      4800 |
|   110  |      9600 |
|   111  |     19200 |





