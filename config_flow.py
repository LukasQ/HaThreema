"""Config flow for Threema integration."""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class ThreemaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Threema."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle user configuration."""
        if user_input is not None:
            return self.async_create_entry(title="Threema", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str,
                vol.Required("threema_id"): str,
                vol.Required("secret"): str,
                vol.Required("private_key"): str,
                vol.Required("public_key"): str,
            }),
        )
