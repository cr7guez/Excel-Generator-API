# Generate Excel files from API connection
# Author: César Rodríguez
# Date: 06/10/2023
# Version: 1.0.0

import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

def get_and_update_list(old_url, new_url, destination_path, index_column):
    # Enter the username for the old API here:
    user_old = "enter username for old API here"
    # Enter the password for the old API here:
    password_old = "enter password for old API here"

    # Enter the username for the new API here:
    user_new = "enter username for new API here"
    # Enter the password for the new API here:
    password_new = "enter password for new API here"

    # Make HTTP request with basic authentication for the old API
    response_old = requests.get(old_url, auth=HTTPBasicAuth(user_old, password_old))

    # Make HTTP request with basic authentication for the new API
    response_new = requests.get(new_url, auth=HTTPBasicAuth(user_new, password_new))

    # Check if requests were successful
    if response_old.status_code == 200 and response_new.status_code == 200:
        data_old = json.loads(response_old.text)
        data_new = json.loads(response_new.text)

        df_old = pd.DataFrame(data_old)
        df_new = pd.DataFrame(data_new)

        if index_column in df_new.columns:
            # Remove duplicate rows based on the index_column in df_new
            df_new = df_new.drop_duplicates(subset=index_column)

            # Set the index in both DataFrames based on the index_column
            df_old.set_index(index_column, inplace=True)
            df_new.set_index(index_column, inplace=True)

            # Sort the DataFrame by the "CC (Client Facturació)" or "CC (Client Comercial)" column
            df_old = df_old.sort_values(by=index_column)

            # Update data from the old API with data from the new API
            df_old.update(df_new)

            # Reset the index so that "CC" is a column again
            df_old.reset_index(inplace=True)

            # Save the updated DataFrame to an Excel file
            df_old.to_excel(destination_path, index=False)

            print(f"The file has been updated and saved to: {destination_path}")
        else:
            print(f"The column {index_column} does not exist in the data from the new API.")
    else:
        print(f"Error in one of the APIs: Old ({response_old.status_code}), New ({response_new.status_code})")

# For billing clients
old_billing_url = "enter the old API URL for billing here"
new_billing_url = "enter the new API URL for billing here"
billing_columns = ["CC (Client Facturació)", "Email"]
destination_path_billing = "enter the destination path for the billing file here"

# Call the function to get and update the billing clients list
get_and_update_list(old_billing_url, new_billing_url, destination_path_billing, "CC (Client Facturació)")

# For commercial clients
old_commercial_url = "enter the old API URL for commercial clients here"
new_commercial_url = "enter the new API URL for commercial clients here"
commercial_columns = ["CC (Client Comercial)", "Email1", "Email2", "Email3", "Email4", "Email5"]
destination_path_commercial = "enter the destination path for the commercial file here"

# Call the function to get and update the commercial clients list
get_and_update_list(old_commercial_url, new_commercial_url, destination_path_commercial, "CC (Client Comercial)")
