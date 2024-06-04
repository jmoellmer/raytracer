from tuples.color import Color

class Canvas:

    def __init__(self, w, h, clr=Color(0.0, 0.0, 0.0)):
        self.w, self.h = w, h
        self._img = [
            [
                rgb for _ in range(w) 
                    for rgb in (clr.r, clr.g, clr.b)
            ] 
            for _ in range(h)
        ]
        
    def _byte(self, x):
        return round(255 * (0 if x < 0 else x))

    def _scale_and_format_rgb(self, r, g, b):
        return f"{self._byte(r)} {self._byte(g)} {self._byte(b)}"
        
    def write_pixel(self, x, y, color):
        x = x * 3
        self._img[y][x] = color.r
        self._img[y][x + 1] = color.g
        self._img[y][x + 2] = color.b

    def pixel_at(self, x, y):
        x = x * 3
        return Color(self._img[y][x],
                     self._img[y][x + 1],
                     self._img[y][x + 2])
    
    def canvas_to_ppm(self):
        ppm = [f"P3\n{self.w} {self.h}\n255"]
        self._convert_pixels_to_ppm_lines(ppm)
        return '\n'.join(ppm)

    def _convert_pixels_to_ppm_lines(self, ppm):
        line = ''
        for y in range(self.h):
            for x in range(self.w):
                color = self.pixel_at(x, y)
                color_str = self._scale_and_format_rgb(color.r, color.g, color.b)

                if len(line + color_str) >= 70:
                    ppm.append(line.strip())
                    line = ''
                    
                line += color_str + " "
        ppm.append(line.strip())
        ppm.append('')
    
    def save(self, file_name, ppm):
        with open(file_name, 'w') as file:
            file.write(ppm)