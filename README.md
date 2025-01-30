# Threema Integration for Home Assistant

**Note:** This is an early version of the integration. I will not provide support or respond to issues.

This integration allows sending notifications via Threema from Home Assistant.

## Installation

1. Copy the `threema` folder into the `custom_components/` directory in your Home Assistant installation.
2. Restart Home Assistant.
3. Add the Threema integration via the user interface.

## Setup

### Obtaining API Keys, Threema ID, and Secrets

To use this integration, you need access to the Threema Gateway API:

1. Register at [Threema Gateway](https://gateway.threema.ch/).
2. Purchase a Threema Gateway account (suitable for businesses or developers sending automated messages).
3. After registration, you will receive the following credentials:
   - **API Key**: Used for authentication with the gateway.
   - **Threema ID**: Your unique Threema identifier for message exchange.
   - **Secret**: Required for API authentication.
   - **Private Key**: The private key for end-to-end encryption.
   - **Public Key**: The public key for communication.

### Adding the Threema SDK

Since the `threema-msgapi-sdk` library is not available on PyPI, you need to install it manually:

#### **Option 1: Install via pip**
If Home Assistant runs in a Python environment (venv), install the library manually:
```bash
pip install git+https://github.com/threema-ch/threema-msgapi-sdk-python.git
```

If running Home Assistant in Docker, execute:
```bash
docker exec -it homeassistant pip install git+https://github.com/threema-ch/threema-msgapi-sdk-python.git
```

#### **Option 2: Add the Library Locally**
1. Clone the repository:
   ```bash
   git clone https://github.com/threema-ch/threema-msgapi-sdk-python.git
   ```
2. Copy the `threema` folder into your custom components directory:
   ```
   /config/custom_components/threema/libs/threema/
   ```
3. Import the library in `notify.py`:
   ```python
   from custom_components.threema.libs.threema.gateway import SimpleGateway
   ```
4. Ensure `manifest.json` does **not** include a `requirements` entry.

### Configuration in Home Assistant

1. Navigate to **Settings** > **Devices & Services**.
2. Click on **Add Integration** and select **Threema**.
3. Enter the required credentials.
4. Save the configuration.

Once successfully configured, you can use Threema for notifications in automations or scripts.

## Usage

Example notification in a Home Assistant automation:

```yaml
alias: "Send test message"
trigger:
  - platform: state
    entity_id: binary_sensor.motion_sensor
    to: "on"
action:
  - service: notify.threema
    data:
      message: "Motion detected!"
      target: "*THREEMA_ID*"
```

Replace `*THREEMA_ID*` with the recipient's Threema ID.

## Troubleshooting

- Ensure that the credentials are entered correctly.
- Check that your Threema Gateway account is active and has sufficient credits.
- Review the Home Assistant log for errors (`Settings` > `System` > `Logs`).

## Disclaimer

This is an early version of the integration. I will not provide support or respond to issues.

