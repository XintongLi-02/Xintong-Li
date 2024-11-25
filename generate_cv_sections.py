def generate_cv_sections(personal_info):
    """
    Create separate sections for contact details, Education Background, Work Experience, Research Experience, Honors Awards, Project Experience, Language, Extra-Curricular Activities, and Programming Skills based on the extracted personal information.

    Args:
        personal_info (dict): A dictionary containing the user's personal information, including Name, Email, Phone, and other relevant details.

    Returns:
        dict: A dictionary containing separate sections for different categories based on the user's personal information.
    """
    cv_sections = {
        'Contact Details': {
            'Name': personal_info.get('Name', ''),
            'Email': personal_info.get('Email', ''),
            'Phone': personal_info.get('Phone', '')
        },
        'Education Background': {'Education': personal_info.get('Education_Background', '')},
        'Work Experience': {'Work': personal_info.get('Work_Experience', '')},
        'Research Experience': {'Research': personal_info.get('Research_Experience', '')},
        'Honors Awards': {'Awards': personal_info.get('Honors_Awards', '')},
        'Project Experience': {'Project': personal_info.get('Project_Experience', '')},
        'Language': {'Languages': personal_info.get('Language', '')},
        'Extra-Curricular Activities': {'Activities': personal_info.get('Extra_Curricular_Activities', '')},
        'Programming Skills': {'Skills': personal_info.get('Programming_Skills', '')}
    }

    return cv_sections
