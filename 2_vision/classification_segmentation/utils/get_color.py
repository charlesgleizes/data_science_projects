import toml
"""
    bottom_right_coordinates(): 
        Usecase:Gets Hexode from toml style file
        Input:  _____
        Output: Returns Hexcode
"""

def primaryColor():
    dict_color = (toml.load(".streamlit/config.toml")["theme"])
    return dict_color["primaryColor"]
def secondaryColor():
    dict_color = (toml.load(".streamlit/config.toml")["theme"])
    return dict_color["secondaryBackgroundColor"]

def backgroundColor():
    dict_color = (toml.load(".streamlit/config.toml")["theme"])
    return dict_color["backgroundColor"]
def black():
    return "00000"
