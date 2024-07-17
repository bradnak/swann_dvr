"""Config flow for Swann CCTV integration."""
from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class SwannCCTVConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Swann CCTV."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            host = user_input["host"]
            username = user_input["username"]
            password = user_input["password"]
            port = user_input["port"]

            # TODO: Validate the input (e.g., try to connect to the DVR)
            # For now, let's assume the input is always valid.

            return self.async_create_entry(
                title="Swann CCTV",
                data={"host": host, "username": username, "password": password, "port": port}
            )

        return self._show_config_form(errors)

    @callback
    def _show_config_form(self, errors):
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host"): str,
                vol.Required("username"): str,
                vol.Required("password"): str,
                vol.Required("port", default=554): int,
            }),
            errors=errors,
        )
