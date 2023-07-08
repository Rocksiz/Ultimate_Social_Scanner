## The Ultimate Social Scanner

The Ultimate Social Scanner is a Python script that allows you to check the availability of a username on various social media websites. It helps you identify if a username is already taken on popular social media platforms.

### Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `requests` library
- `concurrent.futures` module
- `json` module
- `xml.etree.ElementTree` module
- `tabulate` library

You can install the necessary dependencies using the following command:

```shell
pip install requests tabulate
```

### Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

   ```shell
   python social_scanner.py
   ```

4. You will be prompted to enter a username to check. Enter the desired username and press Enter.
5. The script will start scanning various social media websites to check the availability of the username.
6. Once the scanning is complete, the script will display a table of responding websites, if any.
7. You will be presented with the following options:

   - Make a new search: Enter `1` to check another username.
   - Save the result: Enter `2` to save the results in different file formats (JSON, XML, or TXT).
   - Exit: Enter `0` to exit the script.

### Saving Results

When prompted to save the results, you can choose from the following options:

1. JSON: The results will be saved as a JSON file (`{username}_results.json`).
2. XML: The results will be saved as an XML file (`{username}_results.xml`).
3. TXT: The results will be saved as a plain text file (`{username}_results.txt`).
4. Go back: Enter `99` to return to the main menu without saving the results.
5. Exit: Enter `0` to exit the script.

### Disclaimer

This script is provided as-is and does not guarantee the accuracy or availability of usernames on social media platforms. It solely relies on the response status codes received from the websites. The script should be used for informational purposes only.

Please note that excessive and frequent requests to websites may violate their terms of service. Use this script responsibly and with caution.

---

Made with ❤️ by Rocksiz
