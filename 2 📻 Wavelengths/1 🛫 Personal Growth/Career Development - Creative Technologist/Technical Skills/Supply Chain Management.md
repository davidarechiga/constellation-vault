# Supply Chain Management

### Supply Chain Assessment (OBJ 1.2, 1.5 & 1.6)
Secure working in an insecure environment involves mitigating the risks of the supply chain

An organization must ensure that the operation of every element (hardware, firmware, driver, OS, and application) is consistent and tamper resistant to establish a **trusted computing environment**

**Due Diligence -**  a legal principle identifying a subject has used best practice or reasonable care when setting up, configuring, and maintaining a system.
Properly resourced cybersecurity program
Security assurance and risk management processes
Product support life cycle
Security controls for confidential data
Incident response and forensics assistance
General and historical company information

Due diligence should apply to all suppliers and contractors

Trusted Foundry - a microprocessor manufacturing utility that is part of a validated supply chain (one where hardware and software does not deviate from it’s documented function)
Trusted Foundry Program is operated by the Department of Defense (DOD)

Hardware Source Authenticity - The Process of ensuring that hardware is procured tamper-free from trustworthy suppliers
**Greater risk** of inadvertently obtaining **counterfeited** or **compromised** devices when purchasing from second-hand or aftermarket sources

### Root of Trust (OBJ 3.2)

Hardware Root of Trust (ROT)
A cryptographic module embedded within a computer system that can endorse trusted execution and attest to boot settings and metrics

A hardware root of trust is used to scan the boot metrics and OS files to verify their signatures, which we can then use to sign a digital report

Trusted Platform Module
A specification for hardware-based storage of digital certificates, keys, hashed passwords, and other user and platform identification information

A TPM can be managed in Windows via the **tpm.msc** console or though group policy

Hardware Security Module (HSM)
An application for generating and storing cryptographic keys that is less susceptible to tampering and insider threats than software-based storage

Anti-tamper
Methods that make it difficult for an attacker to alter the authorized execution of software

Anti-tamper mechanisms include a field programmable gate array (FPGA) and a physically inclinable function (PUF)

![[Screen Shot 2020-11-18 at 12.02.43 PM.png]]


### Trusted FIrmware (OBJ 3.2)

A **firmware** **exploit** gives an attacker an opportunity to run any code at the highest level of CPU privilege

UEFI
A type of system firmware providing support for 64-bit CPU operation at boot, full GUI and mouse operation at boot, and better boot security
SECURE BOOT
A UEFI feature that presents unwanted process from executing during the boot operation
Measured Boot
A UEFI feature that gathers secure metrics to validate the bot process in an attestation report 
Attestation
A claim that the data presented in the repot is valid by digitally signing it using the TPM’s private key
eFUSE
A means for software or firmware to permanently alter the state of a transistor on a computer chip
Trusted Firmware Updates
A firmware update that is digitally signed by the vendor and trusted by the system before the installation
Self-Encrypting Drives
A disk drive where the controller can automatically encrypt data that is written to it

### Secure Processing (OBJ 3.2)
Secure Processing
A mechanism for ensuring the confidentiality, integrity and availability of software code and data as it is executed in volatile memory

Processor Security Extensions
Low-Level CPU changes and instructions that enable secure processing

AMD 
Secure memory Encryption (SME)
Secure Encrypted Virtualization (SEV)
Intel
Trusted Execution Technology (TXT)
Software Guard Extensions (SGX)

Trusted Execution
The CPU’s security extensions invoke a TPM and secure boot attestation to ensure that a trusted operating system is running

Secure Enclave
The extensions allow a trusted process to create an encrypted container for sensitive data

Atomic Execution
Certain operations that should only be performed once or not at all, such as initializing a memory location

Bus Encryption
Data is encrypted by an application prior to being placed on the data bus

Ensure that the device at the end of the bus is trusted to decrypt the data