def get_text_user(data):
    """
    Get the text from the user
    """
    text = str()
    type_message = data["type"]
    
    if type_message == "text":
        text = (data["text"])["body"]
    elif type_message == "interactive":
        interactive_object = data["interactive"]
        type_interactive = interactive_object["type"]
        if type_interactive == "button_reply":
            text = (interactive_object["button_reply"])["title"]
        elif type_interactive == "list_reply":
            text = (interactive_object["list_reply"])["title"]
        else:
            text = "Interactive type not supported"
    else:
        text = "Message type not supported"
    
    return text