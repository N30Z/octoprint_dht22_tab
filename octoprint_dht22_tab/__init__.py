import octoprint.plugin
import requests

class DHT22TabPlugin(octoprint.plugin.StartupPlugin,
                     octoprint.plugin.TemplatePlugin,
                     octoprint.plugin.AssetPlugin,
                     octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.BlueprintPlugin):

    def on_after_startup(self):
        self._logger.info("DHT22 Tab Plugin started")

    def get_template_configs(self):
        return [
            dict(type="navbar", template="dht22_navbar.jinja2"),
            dict(type="settings", template="dht22_settings.jinja2"),
            dict(type="tab", name="DHT22", template="dht22_tab.jinja2", custom_bindings=False)
        ]

    def get_assets(self):
        return {
            "js": ["js/dht22_tab.js"],
            "css": ["css/dht22_tab.css"]
        }

    def get_settings_defaults(self):
        return dict(
            refresh_rate=10,
            arduino_ip="192.168.178.57"
        )

    @octoprint.plugin.BlueprintPlugin.route("/arduino_data", methods=["GET"])
    def get_arduino_data(self):
        arduino_ip = self._settings.get(["arduino_ip"])
        try:
            response = requests.get(f"http://{arduino_ip}")
            response.raise_for_status()
            data = response.text
            self._logger.info(data)
            return data, 200
        except requests.RequestException as e:
            self._logger.error("Failed to fetch data from Arduino: %s", e)
            return str(e), 500

__plugin_name__ = "DHT22 Tab"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_implementation__ = DHT22TabPlugin()
