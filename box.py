from reportlab.lib import colors   
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet

def create_invoice_packing_list(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    elements.append(Spacer(1, 10))  # Adjust spacing for proper placement
    
    def draw_box(canvas, doc):
        x_start = 10 * mm
        y_start = 260 * mm  # Adjusted to leave space for heading
        box_width = 190 * mm
        box_height = 255 * mm
        
        canvas.setStrokeColor(colors.black)
        canvas.rect(x_start, y_start - box_height, box_width, box_height)
        
        # Draw heading above the box
        canvas.setFont("Helvetica-Bold", 14)
        canvas.drawCentredString(x_start + (box_width / 2), y_start + 10, "INVOICE CUM PACKING LIST")
        
        # Define custom line heights based on reference structure
        heights = [
            30,  # Row 1
            30,  # Row 2
            10,  # Row 3
            20,  # Row 4
            20,  # Row 5
            90,  # Row 6
            10,  # Row 7
            20,  # Row 8
            25   # Row 9
        ]
        
        y_position = y_start
        for index, height in enumerate(heights):
            y_position -= (height * mm)
            canvas.line(x_start, y_position, x_start + box_width, y_position)
            
            # Split right side of rows 1, 2, 3, 4
            if index in [0, 1, 2, 3]:  
                right_x = x_start + (box_width / 2)  
                canvas.line(right_x, y_position + (height * mm), right_x, y_position)
            
            # Fully split left side of Row 4
            if index == 3:  
                left_x_mid = x_start + (box_width / 4)  # Left side 50-50 split
                canvas.line(left_x_mid, y_position + (height * mm), left_x_mid, y_position)  # Vertical split
                mid_y = y_position + (height / 2 * mm)
                canvas.line(x_start, mid_y, right_x, mid_y)  # Horizontal split
            
            # Split first row into two horizontal sections only on the right side
            if index == 0:
                half_y = y_position + (height / 2 * mm)
                right_x = x_start + (box_width / 2)
                canvas.line(right_x, half_y, x_start + box_width, half_y)
                
            
            # Split second row into two unequal horizontal sections only on the right side
            if index == 1:
                upper_section_y = y_position + (height * 0.25 * mm)
                right_x = x_start + (box_width / 2)
                canvas.line(right_x, upper_section_y, x_start + box_width, upper_section_y)

            
            # Split 5th and 6th rows into 5 columns with the first two being wider
            if index in [4, 5]:  
                col_widths = [0.15, 0.45, 0.15, 0.15, 0.10]  # First two columns wider
                current_x = x_start
                col_x_positions = []
                for i in range(4):  # Draw 4 vertical lines to make 5 sections
                    current_x += col_widths[i] * box_width
                    col_x_positions.append(current_x)
                    canvas.line(current_x, y_position + (height * mm), current_x, y_position)
                
                # Split 6th row's 3rd, 4th, and 5th columns into 35% upper and 65% lower
                if index == 5:
                    split_y = y_position + (height * 0.15 * mm)  # 35% upper, 65% lower
                    for col_x in col_x_positions[2:]:  # Apply to 3rd, 4th, 5th columns
                        canvas.line(col_x - (col_widths[col_x_positions.index(col_x)] * box_width), split_y, col_x, split_y)
            
            # Split 9th row (index 8) into 35% left and 65% right
            if index == 8:
                split_x = x_start + (box_width * 0.65)  # 35% width position
                canvas.line(split_x, y_position + (height * mm), split_x, y_position)  # Draw vertical split
    
    doc.build(elements, onFirstPage=draw_box)
    
# Generate PDF
create_invoice_packing_list("invoice_packing_list21.pdf")