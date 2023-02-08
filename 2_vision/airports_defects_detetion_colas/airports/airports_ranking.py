import numpy as np
import pandas as pd

def finding_airports(submission_file, airports_file, n=5):
    
    """
    Function to define the n airports with the most defects. 
    
    Input: 
        submission_file (csv) : csv file with the airports and their defects. 
        airport_file (csv) : csv file with the airport information. 
        n (integer : default = 5) : number of airports returned. 
        
    Output: 
        dataframe with n rows : total number of defects and airport name. 
        
    """
    
    submission = pd.read_csv("submission_1.csv")
    airports_info = pd.read_csv("aeroports.csv")
    
    new = submission["filename"].str.split("_", n = 1, expand = True)
    submission['filename'] = new[0]
    complete_info = submission.merge(airports_info, left_on="filename", right_on = "ID", how='left').drop(columns = ["ID", "Unnamed: 0", "geometry"])
    complete_info["TOTAL"] = complete_info["FISSURE"] + complete_info["REPARATION"] + complete_info["FISSURE LONGITUDINALE"] + complete_info["FAÏENCAGE"] + complete_info["MISE EN DALLE"]
    
    all_defect_airport = complete_info.groupby(by = ["TOPONYME"]).sum()
    sorted_all_defect_air = all_defect_airport.sort_values(by = "TOTAL", ascending = 0)
    
    return(sorted_all_defect_air[0:n])
    
    
    