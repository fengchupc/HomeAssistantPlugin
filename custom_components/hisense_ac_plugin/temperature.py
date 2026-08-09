from __future__ import annotations

from typing import Any


def resolve_current_temperature(device: Any) -> tuple[float | None, str | None]:
    """Resolve the best available current temperature value for the device.

    The control panel temperature is preferred when exposed by the device. If it is
    unavailable, fall back to the indoor unit temperature. The function returns both
    the numeric value and the source key for debugging purposes.
    """

    if device is None:
        return None, None

    candidates = ["t_temp_in", "f_temp_in", "f_temp", "t_temp"]
    for key in candidates:
        value = device.get_status_value(key)
        if value in (None, ""):
            continue
        try:
            return float(value), key
        except (TypeError, ValueError):
            continue

    return None, None
