"""Test VoIP select."""

from homeassistant.components.voip.devices import VoIPDevice
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant


async def test_pipeline_select(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    voip_device: VoIPDevice,
) -> None:
    """Test pipeline select.

    Functionality is tested in assist_pipeline/test_select.py.
    This test is only to ensure it is set up.
    """
    state = hass.states.get("select.sip_192_168_1_210_5060_assistant")
    assert state is not None
    assert state.state == "preferred"


async def test_vad_sensitivity_select(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    voip_device: VoIPDevice,
) -> None:
    """Test VAD sensitivity select.

    Functionality is tested in assist_pipeline/test_select.py.
    This test is only to ensure it is set up.
    """
    state = hass.states.get("select.sip_192_168_1_210_5060_finished_speaking_detection")
    assert state is not None
    assert state.state == "default"
