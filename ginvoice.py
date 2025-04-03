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
        # left_x_mid = x_start + (box_width / 2)  # Initialize before the loop
        
        for index, height in enumerate(heights):
            y_position -= (height * mm)
            canvas.line(x_start, y_position, x_start + box_width, y_position)
            
            # Split right side of rows 2, 3, 4
            if index in [0,1, 2, 3]:  
                right_x = x_start + (box_width / 2)  
                canvas.line(right_x, y_position + (height * mm), right_x, y_position)
            
            # Add EXPORTER heading and details in the first row on the left side
            if index == 0:
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(x_start + 5, y_position + (height - 5) * mm, "EXPORTER")
                canvas.setFont("Helvetica-Bold", 9)
                exporter_details = [
                    "SHRADDHA IMPEX",
                    "308, THIRD FLOOR, FORTUNE BUSINESS CENTER,",
                    "165 R.N.T. MARG,",
                    "INDORE-452001, M.P., INDIA"
                ]
                
                text_y = y_position + (height - 10) * mm
                for line in exporter_details:
                    canvas.drawString(x_start + 5, text_y, line)
                    text_y -= 4 * mm  # Line spacing
                    
            # Add Invoice No. & Date above the horizontal line in row 1 (right side)
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(right_x + 5, y_position + (height - 5) * mm, "Invoice No. & Date:")
                canvas.setFont("Helvetica-Bold", 9)
                canvas.drawString(right_x + 100, y_position + (height - 5) * mm, "SI 19/21-22  Dated  24.05.2021")
                
                # Add I.E. Code No. below the first horizontal line in row 1 (right side)
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(right_x + 5, y_position + (height - 10) * mm, "I.E. Code No.:")
                canvas.setFont("Helvetica-Bold", 9)
                canvas.drawString(right_x + 80, y_position + (height - 10) * mm, "1103004999")
                
            # Add Buyer's Order No. & Date in row 2 (right side below the horizontal line)
            # if index == 1:
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(right_x + 5, y_position + (height - 20) * mm, "Buyer's Order No. & Date:")
                canvas.setFont("Helvetica-Bold", 9)
                canvas.drawString(right_x + 130, y_position + (height - 20) * mm, "SI/SG/02/21-22  23.04.2021")
                
            # Add CONSIGNEE heading and details in the second row on the left side
            if index == 1:
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(x_start + 5, y_position + (height - 5) * mm, "CONSIGNEE:")
                canvas.setFont("Helvetica-Bold", 9)
                consignee_details = [
                    "ALLIANCE DIVINE IMPEX PTE LTD",
                    "No 160 Kallang Way #01-02",
                    "Singapore 349246"
                ]
                
                text_y = y_position + (height - 10) * mm
                for line in consignee_details:
                    canvas.drawString(x_start + 5, text_y, line)
                    text_y -= 4 * mm  # Line spacing
                
                # Add NOTIFY information on the right side above horizontal line
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(right_x + 5, y_position + (height - 5) * mm, "NOTIFY: SAME AS CONSIGNEE")
                
                
                # Add Country of Origin below horizontal line on the right side
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(right_x + 5, y_position + (height * 0.25 - 5) * mm, "Country Of Origin : INDIA")
                
                # Add Pre-carriage and Place of Receipt in the third row on the left side
            if index == 2:
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(x_start + 5, y_position + (height - 5) * mm, "Pre-carriage By:")
                canvas.drawString(x_start + (box_width / 4) + 5, y_position + (height - 5) * mm, "Place of Receipt:")
                
                # Add Country of Final Destination in the third row on the right side
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(right_x + 5, y_position + (height - 5) * mm, "Country Of Final Destination : SINGAPORE")
                
                # Fully split left side of Row 3
            if index == 2:  
                left_x_mid = x_start + (box_width / 4)  # Left side 50-50 split
                canvas.line(left_x_mid, y_position + (height * mm), left_x_mid, y_position)  # Vertical split
                mid_y = y_position + (height / 2 * mm)
                
            
            # Add VESSEL / VOYAGE and TERMS OF DELIVERY in the fourth row on the left side
            if index == 3:
            # Left Side Content
             canvas.setFont("Helvetica-Bold", 9)
             canvas.drawString(x_start + 5, y_position + (height - 5) * mm, "VESSEL/VOYAGE:")
             canvas.drawString(x_start + (box_width / 4) + 5, y_position + (height - 5) * mm, " Port of Loading:")
             canvas.drawString(x_start + (box_width / 4) + 5, y_position + (height - 9) * mm, " NHAVA SHEVA")
             canvas.drawString(x_start + 5, y_position + (height - 14) * mm, "Port of Discharge:")
             canvas.drawString(x_start + 5, y_position + (height - 18) * mm, "SINGAPORE")
             canvas.drawString(x_start + (box_width / 4) + 5, y_position + (height - 14) * mm, " FINAL DESTINATION:")
             canvas.drawString(x_start + (box_width / 4) + 5, y_position + (height - 18) * mm, " SINGAPORE")
             
            # Right Side Content
             right_x = x_start + (box_width / 2)
             canvas.setFont("Helvetica-Bold", 9)   
            # TERMS OF DELIVERY  
             canvas.drawString(right_x + 5, y_position + (height - 5) * mm, "TERMS OF DELIVERY : CH (INCO TERMS 2010)")
             canvas.setFont("Helvetica-Bold", 9)
             payment_text = "Terms of Payment:"
             canvas.drawString(right_x + 5, y_position + (height - 14) * mm, payment_text)
             payment_text = " 10% Advance and balance on scan copy of documents."
             canvas.drawString(right_x + 5, y_position + (height - 18) * mm, payment_text)
            # Vertical split (left-right)
             canvas.line(right_x, y_position + (height * mm), right_x, y_position)
            # Horizontal split (lower part)
             lower_split_y = y_position + (height * 0.5 * mm)
             canvas.line(x_start, lower_split_y, right_x, lower_split_y)

            if index == 4:
                col_widths = [0.20, 0.40, 0.14, 0.13, 0.16]
                headers = ["Sr No & Marks", "Description of Goods", "No. of Units", "Rate per Unit(USD)", "Amount(USD)"]
                current_x = x_start
                y_pos = y_position + (height - 5) * mm

                # Center-aligned headers
                for i, header in enumerate(headers):
                    col_width = col_widths[i] * box_width
                    header_width = canvas.stringWidth(header, "Helvetica-Bold", 10)
                    x_center = current_x + (col_width - header_width) / 2
                    canvas.drawString(x_center, y_pos, header)
                    current_x += col_width

            # Add column headers in the fifth row            

            if index == 5:
                canvas.setFont("Helvetica-Bold", 9)
                
                col_widths = [0.20, 0.40, 0.15, 0.15, 0.15]
                box_width = 190 * mm
                
                # Sr No & Marks 
                marks_data = [
                    "05 X 20' FCL",
                    "Container & Seal nos.:-",
                    "As per attached sheet"
                ]
                
                # Description of Goods 
                desc_data = [
                    "2700 BAGS",
                    "INDIAN WHITE CANE SUGAR S30 ICUMSA",
                    "LESS THEN 100",
                    "HS CODE : 17019910",
                    "PACKED IN LINER PP BAGS 50 KG NET WEIGHT",
                    "TOTAL NET WEIGHT : 135.000 MTS",
                    "TOTAL GROSS WEIGHT: 135.430 MTS"
                ]
                
                units_data = ["2700 BAGS"]
                rate_data = ["470.00","", "", "", "", "", "", "", "TOTAL :"]
                amount_data =["63450.00","", "", "", "", "","", "", "63,450.00"]

                
                text_y = y_position + (height - 8) * mm
                line_height = 8 * mm
        
                # Sr No & Marks  (15%)
                x_col1 = x_start + 5
                for line in marks_data:
                    canvas.drawString(x_col1, text_y, line)
                    text_y -= line_height
                
                # Description  (45%)
                text_y = y_position + (height - 10) * mm
                x_col2 = x_start + (0.20 * box_width) + 5
                for line in desc_data:
                    canvas.drawString(x_col2, text_y, line)
                    text_y -= line_height
                
                # Units  (15%)
                text_y = y_position + (height - 20) * mm
                x_col3 = x_start + (0.60 * box_width) + 5
                for line in units_data:
                    canvas.drawString(x_col3, text_y, line)
                    text_y -= line_height
                
                # Rate (15%)
                text_y = y_position + (height - 20) * mm
                x_col4 = x_start + (0.75 * box_width) + 5
                for line in rate_data:
                    canvas.drawString(x_col4, text_y, line)
                    text_y -= line_height
                
                # Amount (10%)
                text_y = y_position + (height - 20) * mm
                x_col5 = x_start + (0.90 * box_width) + 5
                for line in amount_data:
                    canvas.drawString(x_col5, text_y, line)
                    text_y -= line_height
                    

            # ... (existing code)

            if index == 6:
           # Add "Amount Chargeable" in words
             canvas.setFont("Helvetica-Bold", 10)
             chargeable_text = "Amount Chargeable: (In words) CIF US$ Sixty Three Thousand Four Hundred and Fifty Only."
             canvas.drawString(x_start + 5, y_position + (height - 5) * mm, chargeable_text)

            if index == 7:
         # Add BIN No., Drawback, MEMS, ALQ details
             canvas.setFont("Helvetica-Bold", 9)
             details = [
                  "BIN No.: AJWFS9154KFT001",
                  "Drawback Sr. No.:",
                  "Benefit under MEMS scheme:",
                  "Shipment under ALQ scheme:"
                  ]
             text_y = y_position + (height - 4) * mm
             for line in details:
              canvas.drawString(x_start + 5, text_y, line)
              text_y -= 4 * mm  # Adjust spacing

         #... (existing code for index == 8 - Declaration)
                
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
                upper_section_y = y_position + (height * 0.35 * mm)
                right_x = x_start + (box_width / 2)
                canvas.line(right_x, upper_section_y, x_start + box_width, upper_section_y)
            
                
            # Split 5th and 6th rows into 5 columns with the first two being wider
            if index in [4, 5]:  
                col_widths = [0.20, 0.40, 0.12, 0.16, 0.20]  # First two columns wider
                current_x = x_start
                col_x_positions = []
                for i in range(4):  # Draw 4 vertical lines to make 5 sections
                    current_x += col_widths[i] * box_width
                    col_x_positions.append(current_x)
                    canvas.line(current_x, y_position + (height * mm), current_x, y_position)
                    

            if index == 8:
                # DECLARATION SECTION (9th Row)
                canvas.setFont("Helvetica-Bold", 10)
                canvas.drawString(x_start + 5, y_position + (height - 5) * mm, "DECLARATION:")

                canvas.setFont("Helvetica-Bold", 9)
                # First line of declaration
                canvas.drawString(
                    x_start + 5, 
                    y_position + (height - 11) * mm, 
                    "WE DECLARE THAT THIS INVOICE SHOWS THE ACTUAL PRICE OF GOODS "
                )
                # Second line of declaration
                canvas.drawString(
                    x_start + 5, 
                    y_position + (height - 16) * mm, 
                    "DESCRIBED AND THAT ALL PARTICULARS ARE TRUE & CORRECT."
                )

                
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
create_invoice_packing_list("invoice_packing_list5.pdf")
