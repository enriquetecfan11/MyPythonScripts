import streamlit as st
import pandas as pd
import os

def main():
    # Get a list of all csv files in the csv-export
    csv_files = os.listdir('csv-export')
    csv_files = [file for file in csv_files if file.endswith('.csv')]

    # Create a selectbox for the user to select a csv file
    selected_csv = st.selectbox('Select a CSV file', csv_files)

    # Read the selected csv file using pandas
    df = pd.read_csv(f'csv-export/{selected_csv}')

    # Display the dataframe
    st.write(df)

if __name__ == "__main__":
    main()