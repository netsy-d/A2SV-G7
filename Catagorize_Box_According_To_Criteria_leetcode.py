class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        box_dimension =""
        box_mass = ""
        volume = length * height * width
        if length >= 10000 or height >= 10000 or width >=10000  or volume >=1000000000:
            box_dimension = "Bulky"
        if mass >= 100:
            box_mass = 'Heavy'
        if  box_dimension=="Bulky" and box_mass == "Heavy":
            return"Both"
        elif box_dimension and box_mass == "":
            return box_dimension
        elif box_mass and box_dimension == "":
            return box_mass
        else:
             return "Neither"
