# Threema Integration for Home Assistant

This integration allows sending notifications via Threema from Home Assistant - End-to-End encrypted.
**IMPORTANT:** This is a early alpha version of the inmtegration. Try it on your own risk - no support available at the moment. 

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

