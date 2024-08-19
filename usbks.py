#!/usr/bin/env python3
import subprocess
import time
import logging
import argparse


def configure_logging(verbose: bool) -> None:
    if verbose:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%H:%M:%S",
        )
    else:
        logging.basicConfig(level=logging.WARNING)


def get_usb_devices() -> str:
    result = subprocess.run(["lsusb"], capture_output=True, text=True)
    return result.stdout.strip()


def detect_changes(previous_devices: str, current_devices: str) -> None:
    if previous_devices != current_devices:
        logging.warning("Change detected in USB devices.")
        subprocess.run(["shutdown", "now"])
        logging.info("Executed the script due to detected changes.")


def main(verbose: bool, interval: int):
    configure_logging(verbose)

    previous_devices = get_usb_devices()

    while True:
        time.sleep(interval)
        logging.info("Checking for USB device changes...")
        current_devices = get_usb_devices()
        detect_changes(previous_devices, current_devices)
        previous_devices = current_devices
        logging.info("No changes detected.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Monitor USB devices and shutdown on changes."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        default=3,
        help="Time interval in seconds to check for changes (default: 3)",
    )
    args = parser.parse_args()

    main(args.verbose, args.time)
