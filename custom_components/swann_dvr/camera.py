"""Swann CCTV Camera Platform."""

from homeassistant.components.camera import Camera
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback):
    """Set up Swann CCTV cameras."""
    config = entry.data
    host = config["host"]
    username = config["username"]
    password = config["password"]
    port = config["port"]

    cameras = []
    for channel in range(1, 9):
        for quality in [0, 1]:
            cameras.append(
                SwannCCTVCamera(
                    name=f"Camera {channel} {'High' if quality == 0 else 'Low'}",
                    stream_url=f"rtsp://{username}:{password}@{host}:{port}/ch{channel}/{quality}"
                )
            )

    async_add_entities(cameras)

class SwannCCTVCamera(Camera):
    """Representation of a Swann CCTV camera."""

    def __init__(self, name, stream_url):
        """Initialize the camera."""
        super().__init__()
        self._name = name
        self._stream_url = stream_url

    @property
    def name(self):
        """Return the name of the camera."""
        return self._name

    @property
    def is_on(self):
        """Return true if on."""
        return True

    async def async_camera_image(self):
        """Return a still image response from the camera."""
        # Add your method to fetch a still image from the camera
        return None

    async def async_stream_source(self):
        """Return the stream source."""
        return self._stream_url

    @property
    def supported_features(self):
        """Return supported features."""
        return 0
