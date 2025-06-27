# Instagram Automation Script

This script automates logging into Instagram using a dummy account, searching for the "cbitosc" account, following it, and extracting data such as the account name, bio, and followers count.

## Features

- **Automated Login**: Uses Selenium to log into Instagram.
- **Search and Follow**: Searches for the specified account and follows it.
- **Data Extraction**: Extracts the account name, bio, and number of followers.
- **Logging**: Logs each step of the process and any errors encountered.
- **Headless Mode**: Runs Chrome in headless mode for faster execution.

## demo video





https://github.com/user-attachments/assets/751d811e-0c4e-4460-ab77-cbbee971ceb3




4. **Download ChromeDriver:**

    - Ensure you download the correct version of ChromeDriver that matches your Chrome browser version.
    - Add ChromeDriver to your PATH.

## Usage

1. **Update Credentials:**

    - In `instagram_automation.py`, replace `'your_dummy_username'` and `'your_dummy_password'` with your account information.

2. **Run the Script:**

    ```bash
    python instagram_automation.py
    ```

3. **Output:**

    - The script will generate a `cbitosc_data.txt` file containing the extracted account information.
    - A `automation.log` file will record the process logs and any errors.

## Example

```bash
python instagram_automation.py
