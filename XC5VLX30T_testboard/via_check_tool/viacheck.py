import argparse
import re

def parse_kicad_file(file_path, layer_names):
    vias = []
    segments = []
    polygons = []
    
    with open(file_path, 'r') as file:
        inside_via = False
        inside_segment = False
        inside_polygon = False
        position = None
        start, end, layer = None, None, None
        polygon_points = []
        
        for line in file:
            line = line.strip()
            
            # Detect start of a via entry
            if line.startswith("(via"):
                inside_via = True
                position = None
            
            elif inside_via and line.startswith("(at"):
                match = re.search(r'\(at ([\d.]+) ([\d.]+)\)', line)
                if match:
                    position = (float(match.group(1)), float(match.group(2)))
            
            elif inside_via and line.startswith("(layers"):
                inside_via = False
                if position:
                    vias.append(position)
            
            # Detect start of a segment entry
            elif line.startswith("(segment"):
                inside_segment = True
                start, end, layer = None, None, None
            
            elif inside_segment and line.startswith("(start"):
                match = re.search(r'\(start ([\d.]+) ([\d.]+)\)', line)
                if match:
                    start = (float(match.group(1)), float(match.group(2)))
            
            elif inside_segment and line.startswith("(end"):
                match = re.search(r'\(end ([\d.]+) ([\d.]+)\)', line)
                if match:
                    end = (float(match.group(1)), float(match.group(2)))
            
            elif inside_segment and line.startswith("(layer"):
                match = re.search(r'\(layer "([^"]+)"\)', line)
                if match:
                    layer = match.group(1)
            
            elif inside_segment and line == ")":
                inside_segment = False
                if start and end and layer:
                    segments.append((start, end, layer))

            # Detect start of a filled polygon entry
            elif line.startswith("(filled_polygon"):
                inside_polygon = True
                polygon_points = []
            
            elif inside_polygon and line.startswith("(layer"):
                match = re.search(r'\(layer "([^"]+)"\)', line)
                if match:
                    layer = match.group(1)
            
            elif inside_polygon and line.startswith("(xy"):
                match = re.findall(r'\(xy ([\d.]+) ([\d.]+)\)', line)
                if match:
                    for x, y in match:
                        polygon_points.append((float(x), float(y)))
            
            elif inside_polygon and line == ")":
                inside_polygon = False
                if polygon_points and layer:
                    polygons.append((polygon_points, layer))
    
    # Function to check if a point is inside a polygon using ray casting
    def is_point_in_polygon(point, polygon):
        x, y = point
        num_points = len(polygon)
        j = num_points - 1
        inside = False
        for i in range(num_points):
            xi, yi = polygon[i]
            xj, yj = polygon[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
                inside = not inside
            j = i
        return inside

    # Validate vias
    invalid_vias = []
    for via_position in vias:
        valid = False
        # Check for L1 segment connection
        for segment in segments:
            seg_start, seg_end, seg_layer = segment
            if seg_layer == layer_names[0] and (seg_start == via_position or seg_end == via_position):
                valid = True
                break
        # If no L1 segment found, check for polygon coverage
        if not valid:
            for polygon_points, poly_layer in polygons:
                if poly_layer == layer_names[0] and is_point_in_polygon(via_position, polygon_points):
                    valid = True
                    break
        if not valid:
            invalid_vias.append(via_position)

    # Print the results
    print(f"\n{'Position':<20} {'Validity':<10}")
    for via_position in vias:
        position_str = f"({via_position[0]}, {via_position[1]})"
        validity = "Valid" if via_position not in invalid_vias else "Invalid"
        print(f"{position_str:<20} {validity:<10}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse KiCad PCB file for via and segment information")
    parser.add_argument("pcbfile", type=str, help="Path to the KiCad PCB file")
    parser.add_argument("layers", nargs=4, help="Four layer names: L1, L2, L3, L4")
    args = parser.parse_args()
    
    parse_kicad_file(args.pcbfile, args.layers)
