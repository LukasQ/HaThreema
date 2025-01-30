"""Threema integration for Home Assistant."""
import logging

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "threema"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Threema component."""
    _LOGGER.info("Setting up Threema integration")
    return True
