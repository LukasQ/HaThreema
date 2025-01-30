"""Threema notification integration."""
import logging
import voluptuous as vol

from homeassistant.components.notify import PLATFORM_SCHEMA, BaseNotificationService
import homeassistant.helpers.config_validation as cv
from .const import (
    CONF_API_KEY, CONF_THREEMA_ID, CONF_THREEMA_SECRET,
    CONF_THREEMA_PRIVATE_KEY, CONF_THREEMA_PUBLIC_KEY
)

from threema.gateway import SimpleGateway

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_THREEMA_ID): cv.string,
    vol.Required(CONF_THREEMA_SECRET): cv.string,
    vol.Required(CONF_THREEMA_PRIVATE_KEY): cv.string,
    vol.Required(CONF_THREEMA_PUBLIC_KEY): cv.string,
})

def get_service(hass, config, discovery_info=None):
    """Get the Threema notification service."""
    return ThreemaNotificationService(config)

class ThreemaNotificationService(BaseNotificationService):
    """Implementation of the notification service for Threema."""

    def __init__(self, config):
        """Initialize the service."""
        self._gateway = SimpleGateway(
            threema_id=config[CONF_THREEMA_ID],
            secret=config[CONF_THREEMA_SECRET],
            private_key=config[CONF_THREEMA_PRIVATE_KEY],
            public_key=config[CONF_THREEMA_PUBLIC_KEY],
        )

    async def async_send_message(self, message="", **kwargs):
        """Send a message via Threema."""
        target = kwargs.get("target")
        if not target:
            _LOGGER.error("No target Threema ID provided")
            return

        try:
            await self.hass.async_add_executor_job(self._gateway.send_text, target, message)
            _LOGGER.info("Message sent successfully to %s", target)
        except Exception as e:
            _LOGGER.error("Failed to send message via Threema: %s", str(e))
