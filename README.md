# USB Kill Switch (usbks)

A Python script that continuously monitors USB devices connected to the system and initiates a shutdown if any changes are detected.

## Dependencies

- [usbutils](https://github.com/gregkh/usbutils) (for `lsusb` command)

## Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/salaridoas/usbks.git /tmp/usbks
cd /tmp/usbks
```

### Step 2: Set Permissions and Move Files
```bash
chmod +x usbks.py
sudo mv usbks.py /usr/bin/usbks
sudo mv usbks.service /etc/systemd/system/
```

### Step 3: Configure the USB Kill Switch Service
```bash
sudo systemctl daemon-reload
sudo systemctl enable usbks.service
sudo systemctl start usbks.service
sudo systemctl status usbks.service
```

## Usage

Once the service is running, it will monitor USB devices and shut down the system if any changes are detected.

## Uninstallation Steps

To remove the USB Kill Switch from your system, follow these steps:

### Step 1: Stop the Service
```bash
sudo systemctl stop usbks.service
```

### Step 2: Disable the Service
```bash
sudo systemctl disable usbks.service
```

### Step 3: Remove Service and Executable
```bash
sudo rm /etc/systemd/system/usbks.service /usr/bin/usbks
```

## Disclaimer

Use this tool responsibly, as it may cause data loss if not used correctly. Ensure you understand the implications of automatically shutting down your system in response to USB device changes.
