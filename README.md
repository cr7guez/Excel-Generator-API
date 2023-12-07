# Web API Data Sync for Client List Automation

## Purpose

The **Web API Data Synchronization** script is a robust tool designed to automate the generation of Excel files through API connections to an external client database. Specifically crafted for the management of client lists from an external company, this automation ensures the creation of a fully functional and up-to-date Excel spreadsheet. It seamlessly integrates data from an old API version with a new one, providing an efficient solution for maintaining an accurate and comprehensive client list.

## How It Works

### Configuration

1. Begin by configuring the script with essential parameters such as API URLs, user credentials, and the destination path for the generated Excel file.

### API Interaction

2. The script initiates HTTP requests to both the old and new APIs, utilizing the provided URLs and authentication credentials. It verifies successful API responses (HTTP status code 200).

### Data Processing

3. Upon successful API responses, the script processes the JSON data obtained from both APIs, converting it into Pandas DataFrames for streamlined manipulation.

### Data Synchronization

4. Focused on a specified index column (e.g., "Client ID"), the script compares and merges data from the new API into the existing client information from the old API.

### Excel File Generation

5. The script concludes by sorting the synchronized data, resetting the index, and saving the consolidated DataFrame into an Excel file. This Excel file serves as a dynamic and current client list, combining information from both the old and new APIs.

## Usage

1. **Client List Automation:**
   - Tailor the script to your specific client list scenario by configuring API URLs, relevant columns, and the destination path for the Excel file.

2. **Execution:**
   - Run the script using a Python interpreter. The script automates the synchronization process, generating an updated Excel file with the latest and most accurate client information.

## Example Scenario

Imagine managing a client database sourced from an external company's API. As the external API evolves, maintaining an updated client list becomes crucial. This script serves as an automated solution, effortlessly integrating the latest client data into your existing Excel spreadsheet. The result is a comprehensive and functional client list, always reflecting the most recent information.

This tool is particularly valuable for businesses relying on external databases, ensuring that their client records are consistently accurate and in sync with the latest data.

**Author:** César Rodríguez
