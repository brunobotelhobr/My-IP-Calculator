# My-IP-Calculator 

![Icon](https://brunobotelhobr.github.io/My-IP-Calculator/0.1.0/assets/logo.png)

![GitHub Action CI](https://github.com/brunobotelhobr/My-IP-Calculator/actions/workflows/ci.yml/badge.svg?branch=main)
![GitHub Action CodeQL](https://github.com/brunobotelhobr/My-IP-Calculator/actions/workflows/codeql.yml/badge.svg?branch=main)
![GitHub Action Trivy](https://github.com/brunobotelhobr/My-IP-Calculator/actions/workflows/trivy.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/brunobotelhobr/My-IP-Calculator/branch/main/graph/badge.svg?token=58zkdUzWkh)](https://codecov.io/gh/brunobotelhobr/My-IP-Calculator)

**This an IP address calculator.**

I'm a savy CyberSecurity professional, and the propose of this code is provide and an example and also incentivate my graduation students to develop tools and scripts in python to do defensive or ofensive security tasks.

Features:

 - Works with IPv6 and IPv4.
 - Convert address to decimal, hexadecimal and bnary form.
 - Valdiate addresses
 - Calculate nets (Broadcast, Network ID and avaliable host address)
 - Calculate Subnets

## Demo
[![asciicast](https://asciinema.org/a/585954.svg)](https://asciinema.org/a/585954)

## Install
You can use this tool in many ways:

### Install from Repository
With this command:
````
pip install my-ip-calculator
````

[![asciicast](https://asciinema.org/a/585935.svg)](https://asciinema.org/a/585935)

### Run in Container
With this commands:
````
docker push brunobotelhobr/my-ip-calulator:latest
docker run --rm brunobotelhobr/my-ip-calulator:latest
````

[![asciicast](https://asciinema.org/a/585942.svg)](https://asciinema.org/a/585942)

### Build from Source Code
You mus have python installed.

````
pip install poetry

git clone https://github.com/brunobotelhobr/My-IP-Calculator.git
cd My-IP-Calculator
poetry shell
poetry install

# Testing
task test

# Run
python src/app/cmd.py
````

[![asciicast](https://asciinema.org/a/585958.svg)](https://asciinema.org/a/585958)

## How to use
General:

Usage: `my-ip-calculator [OPTIONS] COMMAND [ARGS]...`

Options:

    --install-completion          Install completion for the current shell.
    --show-completion             Show completion for the current shell, to copy it or customize the installation.
    --help                        Show this message and exit.

Commands:

    net        Calculate the network address from an IP address and a subnet mask, output the address in the desired format.
    subnet     Split an IP address into network and host parts, output the address in the desired format.
    val        Validate an IPv4 ou IPv6 address, output the address in the desired format.
    version    Show version.

### Version
Show the software version:
`````
my-ip-calculator version
0.0.2
`````

### Validate (Val)
Usage: `my-ip-calculator [OPTIONS] ADDRESS`

Validate an IPv4 ou IPv6 address, output the address in the desired format.    

Arguments

    *    address      TEXT  IP address, it supports IPv4 and IPv6 [default: None] [required]

Options

    --output  -o      [bin|hex|dec]  Output format for the network address details of an IP address, it supports bin, hex, dec. [default: None]
    --help                           Show this message and exit.

Examples

`````
my-ip-calculator val 10.10.10.10
               Address                
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item    ┃ Value           ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version │ 4               │ ✅ OK  │
│ Address │ 010.010.010.010 │ ✅ OK  │
└─────────┴─────────────────┴────────┘

my-ip-calculator val 10.10.10.10 -o bin
                         Address                          
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item    ┃ Value                               ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version │ 4                                   │ ✅ OK  │
│ Address │ 00001010.00001010.00001010.00001010 │ ✅ OK  │
└─────────┴─────────────────────────────────────┴────────┘

my-ip-calculator val 10.10.10.10 -o hex
             Address              
┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item    ┃ Value       ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version │ 4           │ ✅ OK  │
│ Address │ 0A.0A.0A.0A │ ✅ OK  │
└─────────┴─────────────┴────────┘

my-ip-calculator val 1:2:3:4:5:6:7:8
                           Address                            
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item    ┃ Value                                   ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version │ 6                                       │ ✅ OK  │
│ Address │ 0001:0002:0003:0004:0005:0006:0007:0008 │ ✅ OK  │
└─────────┴─────────────────────────────────────────┴────────┘
my-ip-calculator  val 1:2:3::
                           Address                            
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item    ┃ Value                                   ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version │ 6                                       │ ✅ OK  │
│ Address │ 0001:0002:0003:0000:0000:0000:0000:0000 │ ✅ OK  │
└─────────┴─────────────────────────────────────────┴────────┘

my-ip-calculator val A -o hex
                      Errors                      
┏━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Item    ┃ Value ┃ Message         ┃ Status     ┃
┡━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ address │ A     │ Invalid address │ ⛔ Invalid │
└─────────┴───────┴─────────────────┴────────────┘
`````

### Network (Net)
Usage: `my-ip-calculator net [OPTIONS] ADDRESS [MASK]`
Calculate the network address from an IP address and a subnet mask, output the address in the desired format.
if a mask isn't provided:

- For IPv4 it will provide a mask based on the adress class: A, B,C,D and E
- For IPv6 a standart /64 will be provided.

Arguments

    *   address      TEXT    IP address, it supports IPv4 and IPv6. [default: None] [required]
        mask         [MASK]  IP address mask, if not provided an auto generated one will be assigned. [default:None]

Options

    --output  -o      [bin|hex|dec]  Output format for the network address details of an IP address, it supports bin, hex, dec. [default:None]
    --help                           Show this message and exit.

Examples
````
my-ip-calculator net 192.168.0.1
                 Network                  
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item        ┃ Value           ┃ Status ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version     │ 4               │ ✅ OK  │
│ Address     │ 192.168.000.001 │ ✅ OK  │
│ Mask        │ 255.255.255.000 │ ✅ OK  │
│ Network     │ 192.168.000.000 │ ✅ OK  │
│ Broadcast   │ 192.168.000.255 │ ✅ OK  │
│ Hosts (dec) │ 254             │ ✅ OK  │
└─────────────┴─────────────────┴────────┘

my-ip-calculator net 192.168.0.1 16
                 Network                  
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item        ┃ Value           ┃ Status ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version     │ 4               │ ✅ OK  │
│ Address     │ 192.168.000.001 │ ✅ OK  │
│ Mask        │ 255.255.000.000 │ ✅ OK  │
│ Network     │ 192.168.000.000 │ ✅ OK  │
│ Broadcast   │ 192.168.255.255 │ ✅ OK  │
│ Hosts (dec) │ 65534           │ ✅ OK  │
└─────────────┴─────────────────┴────────┘

my-ip-calculator net 192.168.0.1 16 -o hex
               Network                
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item        ┃ Value       ┃ Status ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version     │ 4           │ ✅ OK  │
│ Address     │ C0.A8.00.01 │ ✅ OK  │
│ Mask        │ FF.FF.00.00 │ ✅ OK  │
│ Network     │ C0.A8.00.00 │ ✅ OK  │
│ Broadcast   │ C0.A8.FF.FF │ ✅ OK  │
│ Hosts (dec) │ 65534       │ ✅ OK  │
└─────────────┴─────────────┴────────┘

my-ip-calculator net 192.168.0.1 16 -o bin
                           Network                            
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item        ┃ Value                               ┃ Status ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version     │ 4                                   │ ✅ OK  │
│ Address     │ 11000000.10101000.00000000.00000001 │ ✅ OK  │
│ Mask        │ 11111111.11111111.00000000.00000000 │ ✅ OK  │
│ Network     │ 11000000.10101000.00000000.00000000 │ ✅ OK  │
│ Broadcast   │ 11000000.10101000.11111111.11111111 │ ✅ OK  │
│ Hosts (dec) │ 65534                               │ ✅ OK  │
└─────────────┴─────────────────────────────────────┴────────┘

my-ip-calculator  net 1:2:3:4:5:6:A:B -o hex
                             Network                              
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item        ┃ Value                                   ┃ Status ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version     │ 6                                       │ ✅ OK  │
│ Address     │ 0001:0002:0003:0004:0005:0006:000A:000B │ ✅ OK  │
│ Mask        │ FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000 │ ✅ OK  │
│ Network     │ 0001:0002:0003:0004:0000:0000:0000:0000 │ ✅ OK  │
│ Broadcast   │ 0001:0002:0003:0004:FFFF:FFFF:FFFF:FFFF │ ✅ OK  │
│ Hosts (dec) │ 18446744073709551614                    │ ✅ OK  │
└─────────────┴─────────────────────────────────────────┴────────┘

my-ip-calculator net 1:2:3:4:5:6:A:B 96 -o hex
                             Network                              
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Item        ┃ Value                                   ┃ Status ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ Version     │ 6                                       │ ✅ OK  │
│ Address     │ 0001:0002:0003:0004:0005:0006:000A:000B │ ✅ OK  │
│ Mask        │ FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:0000:0000 │ ✅ OK  │
│ Network     │ 0001:0002:0003:0004:0005:0006:0000:0000 │ ✅ OK  │
│ Broadcast   │ 0001:0002:0003:0004:0005:0006:FFFF:FFFF │ ✅ OK  │
│ Hosts (dec) │ 4294967294                              │ ✅ OK  │
└─────────────┴─────────────────────────────────────────┴────────┘

my-ip-calculator net 12:A:Z:: -o hex  
                                       Errors                                       
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Item    ┃ Value                                   ┃ Message         ┃ Status     ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ address │ 0012:000A:000Z:0000:0000:0000:0000:0000 │ Invalid address │ ⛔ Invalid │
└─────────┴─────────────────────────────────────────┴─────────────────┴────────────┘

my-ip-calculator net Z -o hex  
                      Errors                      
┏━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Item    ┃ Value ┃ Message         ┃ Status     ┃
┡━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ address │ A     │ Invalid address │ ⛔ Invalid │
└─────────┴───────┴─────────────────┴────────────┘
````

### Subnet
Usage: `cmd.py subnet [OPTIONS] ADDRESS MASK PARTS`

Split an IP address into network and host parts, output the address in the desired format.

Arguments 

    *    address      TEXT     IP address, it supports IPv4 and IPv6. [default: None][required]
    *    mask         TEXT     IP address mask. [default: None] [required]│
    *    parts        INTEGER  Split the netork into this parts. [default: None] [required]│

Options

    --output  -o      TEXT  Output format for the network address details of an IP address, it supports bin, hex, dec. [default: None]
    --help                  Show this message and

Examples
````
my-ip-calculator  subnet 192.168.0.1 8 8
                                        Networks
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Version ┃ Network         ┃ Mask            ┃ Broadcast       ┃ Hosts (dec) ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━┩
│ 4       │ 192.168.000.000 │ 255.255.000.000 │ 192.168.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.169.000.000 │ 255.255.000.000 │ 192.169.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.170.000.000 │ 255.255.000.000 │ 192.170.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.171.000.000 │ 255.255.000.000 │ 192.171.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.172.000.000 │ 255.255.000.000 │ 192.172.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.173.000.000 │ 255.255.000.000 │ 192.173.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.174.000.000 │ 255.255.000.000 │ 192.174.255.255 │ 65534       │ ✅ OK  │
│ 4       │ 192.175.000.000 │ 255.255.000.000 │ 192.175.255.255 │ 65534       │ ✅ OK  │
└─────────┴─────────────────┴─────────────────┴─────────────────┴─────────────┴────────┘

my-ip-calculator subnet 192.168.0.1 8 8 -o hex
                                  Networks
┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Version ┃ Network     ┃ Mask        ┃ Broadcast   ┃ Hosts (dec) ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━┩
│ 4       │ C0.A8.00.00 │ FF.FF.00.00 │ C0.A8.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.A9.00.00 │ FF.FF.00.00 │ C0.A9.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.AA.00.00 │ FF.FF.00.00 │ C0.AA.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.AB.00.00 │ FF.FF.00.00 │ C0.AB.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.AC.00.00 │ FF.FF.00.00 │ C0.AC.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.AD.00.00 │ FF.FF.00.00 │ C0.AD.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.AE.00.00 │ FF.FF.00.00 │ C0.AE.FF.FF │ 65534       │ ✅ OK  │
│ 4       │ C0.AF.00.00 │ FF.FF.00.00 │ C0.AF.FF.FF │ 65534       │ ✅ OK  │
└─────────┴─────────────┴─────────────┴─────────────┴─────────────┴────────┘

my-ip-calculator subnet A:B:C:D:E:: 96 16 -o dec
                                                                                        Networks                                                                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Version ┃ Network                                         ┃ Mask                                            ┃ Broadcast                                       ┃ Hosts (dec) ┃ Status ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━┩
│ 6       │ 00010:00011:00012:00013:00014:00000:00000:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00000:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00001:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00001:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00002:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00002:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00003:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00003:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00004:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00004:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00005:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00005:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00006:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00006:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00007:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00007:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00008:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00008:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00009:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00009:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00010:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00010:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00011:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00011:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00012:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00012:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00013:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00013:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00014:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00014:65535 │ 65534       │ ✅ OK  │
│ 6       │ 00010:00011:00012:00013:00014:00000:00015:00000 │ 65535:65535:65535:65535:65535:65535:65535:00000 │ 00010:00011:00012:00013:00014:00000:00015:65535 │ 65534       │ ✅ OK  │
└─────────┴─────────────────────────────────────────────────┴─────────────────────────────────────────────────┴─────────────────────────────────────────────────┴─────────────┴────────┘
````

## About this code
It uses Poetry for dependency management and includes pre-configured tools such as black, flake8, mypy, pylint, pytest, and others, for formatting, linting, testing, and documentation management. 
The project also includes security tools like trivy and bandit. 

The pyproject.toml file contains various configurations like project metadata, dependencies, build system, and commands for release and documentation management.

To have more details, check the [Documentation](https://brunobotelhobr.github.io/My-IP-Calculator/)

## Features
- Project Management
    - ✅ [Poetry](https://python-poetry.org/docs/)
    - ✅ Script to manage project metadata (Name, Version, Description, etc)
    - ✅ Script to Upgrade all dependencies
    - ✅ Script to clean all temporary files
- Code Formatting
    - ✅ [Black](https://github.com/psf/black)
    - ✅ [isort](https://pycqa.github.io/isort/)
    - ✅ [autoflake](https://github.com/myint/autoflake)  
- Code Linting
    - ✅ [Pylint](https://www.pylint.org/)
    - ✅ [Flake8](https://flake8.pycqa.org/en/latest/)
    - ✅ [Mypy](https://mypy.readthedocs.io/en/stable/)
- Testing
    - ✅ [Pytest](https://docs.pytest.org/en/stable/)
    - ✅ [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
    - ✅ Default tests structure folder for unit and functional tests
- Security
    - ✅ [Trivy](https://aquasecurity.github.io/trivy/v0.40/getting-started/installation/)
    - ✅ [Bandit](https://pypi.org/project/bandit/)
    - ✅ [Horusec](https://horusec.io/docs/quick-start/installation/)
- Autoamtion commands
    - ✅ [Taskipy](https://github.com/taskipy/taskipy)
- PyPI
    - ✅ Scripts to build and publish to PyPI
- Docker
    - ✅ Scripts to build and publish to Docker Hub
- Documentation
    - ✅ [MkDocs](https://www.mkdocs.org/)
    - ✅ [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
    - ✅ [MkDocs Versioning with mike](https://github.com/jimporter/mike)
    - ✅ Scripts to generate SBOM (Software Bill of Materials)
    - ✅ Scripts to generate requirements.txt
- CI/CD
    - ✅ GitHub Actions to do CI/CD


## Tasks
This project uses [Taskipy](https://github.com/taskipy/taskipy) to automate common development tasks.

All tasks are defined in the `pypoject.toml` file.

Almost all tools used in this project uses `pyproject.toml` to store their configurations.

List of preset tasks:
````
pre-commit      Run all pre-commit tasks
pre-release     Run all pre-release tasks
-----------     ----------------------------------------
info            Show project info
meta            Update project properties
upgrade         Upgrade all dependencies
sec             Run all security checks
format          Run all formaters
lint            Run all linters
bom             Generate BOM
req             Generate requirements.txt
test            Run all tests
pypi-build      Build package for PyPI
pypi-auth       Authenticate to PyPI
pypi-pub        Publish package to PyPI
docker-list     List docker images
docker-build    Build docker image
docker-sec-scan Scan a docker image looking for vulenrabilities
docker-auth     Authenticate to Docker Hub
docker-latest   Tag a docker image as latest
docker-pub      Publish docker image to Docker Hub
docs            Run docs server
docs-list       List docs versions
docs-build      Add a new version to docs
docs-delete     Delete a version of the docs
docs-latest     Set the latest Version.
docs-purge      Purge all versions of the docs.
docs-pub        Publish documentation to the doc branch on GitHub.
clean           Clean all generated files
````

## Requirements
You must install manually the following tools:

- Install [Python](https://www.python.org/downloads/)
- Install [Poetry](https://python-poetry.org/docs/#installation)
- Install [Trivy](https://aquasecurity.github.io/trivy/v0.40/getting-started/installation/)
- Install [Horusec](https://horusec.io/docs/quick-start/installation/)
- Install [Docker](https://docs.docker.com/get-docker/)

Be sure you have installed all the requirements and that you on the desired python Version, you can check it with: 
    `python --version`

## Setup
```shell
# Clone the repository
git clone https://github.com/brunobotelhobr/My-IP-Calculator.git

# Check the python version, you must use the version that the project will use.
python -V

# Install the dependencies
pip install poetry
poetry shell
poetry install

# Check the taskipi commands:
task --list

# Update projetct metadata
task meta
```

## How Start?

### 1. Fork the project
```shell
# Clone the repository
git clone

# Check the python version, you must use the version that the project will use.
python -V

# Install the dependencies
pip install poetry
poetry shell
poetry install

# Check the taskipi commands:
task --list
```

### 2. Create a new branch with your changes
```shell
# Create a new branch
git checkout -b <branch-name>
```

### 3. Make the changes and commit
```shell
# Check for lint errors
task format
task lint

# Check for security errors
task sec

# Update the meta
task meta
task bom
task req

# Add the changes
git add .
```

### 4. Open a Pull Request
```shell
git commit -m "feat: add a new feature"
git push origin <branch-name>
```

## Hints
- How add a Dev Package
   -  `poetry add --dev <package-name>`
- How add a Prod Package
    - `poetry add <package-name>`
- How add a Package with extras
    - `poetry add <package-name> -E <extras>`
- How remove a Package
    - `poetry remove <package-name>`

## Call for Contributors
We invite you to contribute to this repository and help us make it even better. 
Whether it's bug fixes, new features, or documentation improvements, we welcome all contributions. 
Please read our documentation for guidelines on how to contribute. 
Happy coding!

check the [Documentation](https://brunobotelhobr.github.io/My-IP-Calculator/) for more details.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/brunobotelhobr)

