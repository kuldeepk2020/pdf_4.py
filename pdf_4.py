import streamlit as st
import requests

def main():
    st.title("Resume Viewer")

    # Google Drive file ID and direct download URL
    file_id = '1DiILJMwYGelZvXtlxg8LMoeI2PL-UQBt'
    download_url = f'https://drive.google.com/uc?export=download&id=1DiILJMwYGelZvXtlxg8LMoeI2PL-UQBt'

    try:
        # Fetch the PDF file from Google Drive
        response = requests.get(download_url)
        response.raise_for_status()
        pdf_bytes = response.content

        # Display the PDF file
        st.write("Showing PDF file:")
        st.download_button("Download PDF", pdf_bytes, file_name="Kuldeep_Yadav_Resume_OLD_5.pdf")
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching PDF file: {e}")

if __name__ == "__main__":
    main()





