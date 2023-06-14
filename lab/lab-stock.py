import os

from rich.console import Console


C = Console()


def list_devices(ableton_path: str):
    """
    List all devices in the directory.
    """
    devices_path = os.path.join(ableton_path, "Resources", "Core Library", "Devices")

    res = {}
    for subdir in os.listdir(devices_path):
        subdir_list = [
            dir
            for dir in os.listdir(os.path.join(devices_path, subdir))
            if dir != "Ableton Folder Info"
        ]

        res[subdir] = subdir_list

    return res


if __name__ == "__main__":
    # ableton_path = "C:\\ProgramData\\Ableton\\Live 11 Suite"
    # C.print(list_devices(ableton_path))

    home_dir = os.path.expanduser("~")
    ableton_db_path = os.path.join(
        home_dir, "AppData", "Local", "Ableton", "Live Database"
    )

    C.print(os.listdir(ableton_db_path)[-1])
