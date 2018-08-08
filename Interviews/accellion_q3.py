"""

Accellion Coding Question 3
Anthony Tam
anthonytam2018@gmail.com

"""

class CropRatio:

	# Based on input crops below, output should return 0.9. 
	# Debug the code.

    def __init__(self):
        self.crops = {}
        self.total_weight = 0

    def add(self, name, crop_weight):
        if not name in self.crops:
            self.crops[name] = crop_weight
        else:
        	self.crops[name] += crop_weight

    def proportion(self, name):
        if not name in self.crops:
        	return
        for k, v in self.crops.items():
        	self.total_weight  += v
        return (self.crops[name]/self.total_weight)

#To see the output, uncomment the lines below:
crop_ratio = CropRatio()
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)

print(crop_ratio.proportion('Wheat'))