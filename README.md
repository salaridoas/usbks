# USB Kill Switch (usbks)

A Python script that continuously monitors USB devices connected to the system and initiates a shutdown if any changes are detected.

## Dependencies

- [usbutils](https://github.com/gregkh/usbutils) (lsusb)

## Installation

### Linux (Using Python Virtual Environment)

1. **Clone the Repository and Set Up Virtual Environment**:
   ```bash
   git clone https://github.com/salaridoas/usbks.git /tmp/usbks
   cd /tmp/usbks
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pyinstaller
   ```

2. **Create Executable Binary and Move Files**:
   ```bash
   pyinstaller --onefile usbks.py
   sudo mv dist/usbks /usr/bin/
   sudo mv usbks.service /etc/systemd/system/
   ```

3. **Manage the USBKS Service**:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable usbks.service
   sudo systemctl start usbks.service
   sudo systemctl status usbks.service
   ```

## Usage

Once the service is running, it will monitor USB devices and shut down the system if any changes are detected.

## Deinstallation

To remove the USB Kill Switch from your system, follow these steps:

   ```bash
   sudo systemctl stop usbks.service
   sudo systemctl disable usbks.service
   sudo rm /etc/systemd/system/usbks.service
   sudo rm /usr/bin/usbks
   ```

## Disclaimer

Use this tool responsibly, as it may cause data loss if not used correctly.
