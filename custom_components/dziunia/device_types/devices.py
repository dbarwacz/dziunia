from enum import Enum
from typing import Type
from typing import Union

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class Device_type(Enum):
    EMU_1_40_v4_15val = "EMU 1/40 | Firmware Version 4 | 15 Values"


def get_class_from_enum(
        enum_or_str: Union[Device_type, str]
) -> Type[DataUpdateCoordinator] | None:
    """You input a device type enum, you get the corresponding Class object
    Sice we have to expect a whole host of different python versions, you may even input a string
    and it will be converted to the corresponding enum value"""

    from custom_components.dziunia.device_types.emu_1_40_v4_15val import (
        Emu_1_40_V4_15val,
    )
    from custom_components.dziunia.can_client import EmuApiError

    template_mapping = {
        Device_type.EMU_1_40_v4_15val: Emu_1_40_V4_15val,
    }

    value_to_name = {e.value: e.name for e in Device_type}

    # If input is a string, determine if it's an enum name or enum value
    if isinstance(enum_or_str, str):
        if enum_or_str in Device_type.__members__:
            # Input string is an enum name
            enum_or_str = Device_type[enum_or_str]
        elif enum_or_str in value_to_name:
            # Input string is an enum value
            enum_or_str = Device_type[value_to_name[enum_or_str]]
        else:
            raise EmuApiError(f"Unknown device type {enum_or_str}")

    return template_mapping.get(enum_or_str)


def get_enum_from_version_and_sensor_count(
        version: int, sensor_count: int
) -> Device_type | None:
    """You have a version number and you know how many sensor values you get from the API, but you don't know what
    device this is? Boy, do I have the right method for you!"""
    device_type_matrix = {
        (4, 15): Device_type.EMU_1_40_v4_15val,
    }
    return device_type_matrix.get((version, sensor_count), None)
