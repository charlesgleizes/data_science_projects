import math

"""
    top_left_coordinates(lat, lon): 
        Usecase:Computes top left corner coordinate of image, fifty meters east and 50 m north
                of inital coordinate.
        Input:  lat (float)
                    - Lattidue 
                lon (float)
                    - Longitude
        Output: Returns top left corner coordinate 

"""
def top_left_coordinates(lat, lon):
    #Earth’s radius, sphere
    R=6378137

    #offsets in meters
    dn = 50
    de = -50

    #Coordinate offsets in radians
    dLat = dn/R
    dLon = de/(R*math.cos(math.pi*lat/180))

    #OffsetPosition, decimal degrees
    latO = lat + dLat * 180/math.pi
    lonO = lon + dLon * 180/math.pi 
    
    return [latO, lonO]


"""
    bottom_right_coordinates(lat, lon): 
        Usecase:Computes bottom right corner coordinate of image, fifty meters west and 50 m south
                of inital coordinate.
        Input:  lat (float)
                    - Lattidue 
                lon (float)
                    - Longitude
        Output: Returns bottom right corner coordinate 
"""

def bottom_right_coordinates(lat, lon):
    #Earth’s radius, sphere
    R=6378137

    #offsets in meters
    dn = -50
    de = 50

    #Coordinate offsets in radians
    dLat = dn/R
    dLon = de/(R*math.cos(math.pi*lat/180))

    #OffsetPosition, decimal degrees
    latO = lat + dLat * 180/math.pi
    lonO = lon + dLon * 180/math.pi 
    
    return [latO, lonO]
