pi = 3.141592

def triangle_area(base,height):
    if base <= 0 or height <= 0:
        raise ValueError("밑변과 높이는 양수여야 합니다.")
    return base*height/2

def circle_area(radius):
    if radius <= 0:
        raise ValueError("반지름은 양수여야 합니다.")
    return radius*radius*pi
def rectangular_prism_surface_area(length,width,height) :
    if length <= 0 or width <= 0 or height <= 0 :
        raise ValueError("모든 변의 길이는 양수여야 합니다.")
    return 2*(length*width+width*height+height*length)
