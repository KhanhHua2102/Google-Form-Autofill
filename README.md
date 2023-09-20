<a name="readme-top"></a>

<h3 align="center">Google Form Autofill</h3>

### About The Project

This Python script automates the process of filling out a Google Form using Selenium and Chrome WebDriver. It takes input data from a CSV file, locates the form elements by their XPaths, and submits the form.

### Features:

- Automated form filling with Selenium and Chrome WebDriver.
- Input data from a CSV file, making it easy to customize and scale.
- Customizable XPaths for locating form elements.
- User-friendly and configurable script.

### Prerequisites:

- Python 3.x installed.
- Selenium library installed (you can install it using pip install selenium).
- Chrome WebDriver installed and its path configured.

### Usage:

- Clone this repository to your local machine.
- Install the required dependencies:

```
pip install selenium webdriver-manager requests

```

- Configured in the script.
- Place your input data in a CSV file named data.csv.
- Update the XPaths in the script to match the elements on your Google Form and any input text for text fields if needed:

```
fullXpath_inputData\n
```

Run the script:

```
python automate_form_fill.py.
```

### CSV Data Format:

Your CSV file (data.csv) should have columns with headers that match the XPath identifiers in your script. For example:

```
fullXpath\n
fullXpath*inputData\n
/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]\n
/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input_someInputText\n
```

### Customization:

- You can customize the XPaths in the script to match the structure of your Google Form.
- Change time.sleep() values to adjust the speed of the script.
- Define form fill repetition by adjusting the for loop.

### Built With

- [![Python][Python.com]][Python-url]
- [![Selenuim][Selenium.com]][Selenium-url]
- [![Chrome WebDriver][ChromeWebDriver.com]][ChromeWebDriver-url]

### Note:

This script is for educational and demonstrational purposes only. Ensure you have the necessary permissions to automate form submissions on the target website. Misuse of automation tools may violate terms of service.

### Contributing:

Contributions are welcome! If you have improvements, bug fixes, or feature additions, please open an issue or submit a pull request.

### License:

This project is licensed under the MIT License - see the LICENSE file for details.
