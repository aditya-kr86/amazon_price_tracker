# Amazon Price Tracker

The **Amazon Price Tracker** is a Python program that helps users monitor the prices of their favorite products on Amazon. It notifies users when the price drops, ensuring they never miss a deal.

## Features

- Tracks the price of a specified product on Amazon.
- Sends notifications when the price falls below a defined threshold.
- Automates price checks at regular intervals.
- Easy-to-configure product URL and price thresholds.

## Getting Started

Follow these instructions to set up and run the Amazon Price Tracker on your local machine.

### Prerequisites

- [Python 3.x](https://www.python.org/) installed on your system.
- Required Python packages (listed in [requirements.txt](requirements.txt)).
- An email account (for receiving notifications).

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aditya-kr86/amazon_price_tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd amazon_price_tracker
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Open the `price-tracker.py` file.
2. Update the following variables:
   - `URL`: Replace it with the Amazon product URL you want to track.
   - `TARGET_PRICE`: Set the desired price threshold for notifications.
   - `EMAIL`: Configure your email address for alerts.
   - `SMTP_SERVER` and `SMTP_PORT`: Configure your email server settings.

### Usage

Run the script to start tracking the product price:
```bash
python price-tracker.py
```

The program will periodically check the product price and send an email if it drops below the target value.

## Contributing

Contributions are welcome! If you'd like to enhance this project or fix issues, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your changes"
   ```
4. Push your branch to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, feel free to reach out:

- **Author:** Aditya Kumar
- **GitHub:** [aditya-kr86](https://github.com/aditya-kr86)

---

Happy price tracking! 🛒
