from tuples.color import Color

class Canvas:
    def __init__(self, w, h, bg_color=Color(0, 0, 0)):
        self.w, self.h = w, h
        self._img = [
            [bg_color for _ in range(w)] for _ in range(h)
        ]

    def write_pixel(self, x, y, color):
        if 0 <= x < self.w and 0 <= y < self.h:
            # Flip y to match Cartesian plane orientation
            #self._img[self.h - y - 1][x] = color
            self._img[y][x] = color
        else:
            raise ValueError(f"Pixel ({x}, {y}) is out of bounds")
        
    def pixel_at(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            #return self._img[self.h - y - 1][x]
            return self._img[y][x]
        else:
            raise ValueError(f"Pixel ({x}, {y}) is out of bounds")
        
    def _byte(self, x):
        return round(255 * max(0, x))
    
    def _color_string(self, color):
        return f"{self._byte(color.r)} {self._byte(color.g)} {self._byte(color.b)}"
    
    def canvas_to_ppm(self):
        ppm_header = f"P3\n{self.w} {self.h}\n255\n"
        ppm_body = []

        line = ''
        for row in self._img:
            for color in row:
                color_str = self._color_string(color)
                
                if len(line) + len(color_str) >= 70:
                    ppm_body.append(line.strip())
                    line = ''
                
                line += color_str + ' '

        ppm_body.append(line.strip())

        ppm = ppm_header + '\n'.join(ppm_body) + '\n'
        return ppm

    def save(self, file_name, ppm):
        with open(file_name, 'w') as file:
            file.write(ppm)
    


        