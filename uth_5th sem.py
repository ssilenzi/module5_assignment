import numpy as np # linear algebra

def update(alpha, theta,x,y):
    if(alpha < theta):
        d = x / np.cos(alpha)
    elif(alpha > theta):
        d = y / np.sin(alpha)
    else:
        d = np.sqrt(x**2 + y**2)
    return(d)

# Returns the distance to the closest intersection of a beam
# and the map borders. The beam starts at (x, y) and has
# the angle alpha to the positive x-axis.
# The borders are given by map_limits = [x_min, x_max, y_min, y_max].
def distance_to_closest_border(x, y, alpha, map_limits):
    
    if(alpha <= (np.pi/2)): #1st quadrant
        b = abs(map_limits[1] - x)
        h = abs(map_limits[3] - y)
        theta = abs(np.arctan(h/b)) # threshold
        d = update(alpha,theta,b,h)
        
    elif(alpha <= np.pi): #2nd quadrant
        b = abs(map_limits[0] - x)
        h = abs(map_limits[3] - y)
        theta = np.arctan(h/b) # threshold
        alpha = (np.pi) - alpha
        d = update(alpha,theta,b,h)
        
    elif(alpha <= (3*np.pi/2)): #3rd quadrant
        b = abs(map_limits[0] - x)
        h = abs(map_limits[2] - y)
        theta = np.arctan(h/b) # threshold
        alpha = (3 * np.pi/2) - alpha
        alpha = (np.pi/2) - alpha
        d = update(alpha,theta,b,h)
        
    else: #4th quadrant
        b = abs(map_limits[1] - x)
        h = abs( map_limits[2] - y)
        theta = np.arctan(h/b)# threshold
        alpha = (2*np.pi) - alpha
        d = update(alpha,theta,b,h)
        
    return(d)


if __name__=="__main__":
    #distance_to_closest_border(x, y, alpha, map_limits)
    print(distance_to_closest_border(1.0, 1.5, 1.5708, [-2.5,2.5,-2.5,2.5]))
