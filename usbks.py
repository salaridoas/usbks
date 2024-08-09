import subprocess
import time
import logging

# Configure logging with 24-hour time format
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)


def get_usb_devices() -> str:
    result = subprocess.run(["lsusb"], capture_output=True, text=True)
    return result.stdout.strip()


def detect_changes(previous_devices: str, current_devices: str) -> None:
    if previous_devices != current_devices:
        logging.warning("Change detected in USB devices.")
        subprocess.run(["shutdown", "now"])
        logging.info("Executed the script due to detected changes.")


def main():
    previous_devices = get_usb_devices()

    while True:
        logging.debug("Checking for USB device changes...")
        time.sleep(3)
        current_devices = get_usb_devices()
        detect_changes(previous_devices, current_devices)
        previous_devices = current_devices
        logging.debug("No changes detected.")


if __name__ == "__main__":
    main()
