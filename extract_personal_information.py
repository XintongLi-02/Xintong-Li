def extract_personal_information(file_path):
    """
    Read the specified JSON file to extract the user's personal information.

    Args:
        file_path (str): The path to the JSON file containing personal information.

    Returns:
        dict: A dictionary containing the extracted personal information.
    """
    import json

    # Initialize an empty dictionary to store the extracted personal information
    personal_info = {}

    # Read the JSON file and extract personal information
    with open(file_path, 'r') as file:
        data = json.load(file)
        
        # Extract multiple fields
        personal_info['Name'] = data.get('Name', '')
        personal_info['Email'] = data.get('Email', '')
        personal_info['Phone'] = data.get('Phone', '')
        personal_info['Education_Background'] = data.get('Education_Background', '')
        personal_info['Work_Experience'] = data.get('Work_Experience', '')
        personal_info['Research_Experience'] = data.get('Research_Experience', '')
        personal_info['Honors_Awards'] = data.get('Honors_Awards', '')
        personal_info['Project_Experience'] = data.get('Project_Experience', '')
        personal_info['Language'] = data.get('Language', '')
        personal_info['Extra_Curricular_Activities'] = data.get('Extra_Curricular_Activities', '')
        personal_info['Programming_Skills'] = data.get('Programming_Skills', '')

    return personal_info
