from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_export_bill_pdf(image_paths, output_filename):
    # A4 size in mm
    width, height = 210 * mm, 297 * mm  
    c = canvas.Canvas(output_filename, pagesize=(width, height))

    for index, image_path in enumerate(image_paths):
        c.drawImage(image_path, 0, 0, width=width, height=height)

        if index == 0:
            c.setFont("Helvetica-Bold", 10)
            c.setFillColorRGB(0, 0, 0)

            # Fill basic details
            c.drawString(181.8 * mm, height - 20.5 * mm, "Industrial est")  # Branch Name
            c.drawString(170.5 * mm, height - 26.5 * mm, "19-04-2021")  # Date
            c.drawString(30.6  * mm, height - 75.7 * mm, "2577445")
            c.drawString(112.8 * mm, height - 75.7 * mm, "Bank Of India")
            c.drawString(114.7 * mm, height - 99.5 * mm, "SGD")
            c.drawString(45.7 * mm, height - 121.5 * mm, "SGD")
            c.drawString(45.7 * mm, height - 128.5 * mm, "78300")
            c.drawString(114.9 * mm, height - 120.5 * mm, "Seventy eight thousand three hundred only")
            c.drawString(50.4 * mm, height - 138.5 * mm, "Sugar")
            c.drawString(50.4 * mm, height - 143.5 * mm, "Nhava")
            c.drawString(34.3 * mm, height - 197.5 * mm, "Aarti Khale")
            c.drawString(34 * mm, height - 203.1 * mm, "9876543210")
            c.drawString(34 * mm, height - 209.9 * mm, "shradhaimpacs@yahoo.com")
            c.drawString(133.7 * mm, height - 197.6 * mm, "Singapore")
            c.drawString(142.7 * mm, height - 137.6 * mm, "17011390")
            c.drawString(51.7 * mm, height - 153.6 * mm, "465690")
            c.drawString(51.7 * mm, height - 159.6 * mm, "17-09-2021")
            c.drawString(51.7 * mm, height - 163.6 * mm, "INDIA")
            c.drawString(153.7 * mm, height - 159.6 * mm, "INNSA1")
            c.drawString(46.7 * mm, height - 99.6 * mm, "3578")
            c.drawString(145.7 * mm, height - 99.6 * mm, "4278")
            c.drawString(33.7 * mm, height - 108.6 * mm, "6538")
            c.drawString(45.7 * mm, height - 236.6 * mm, "9743")
            c.drawString(132.7 * mm, height - 203.6 * mm, "codex@yahoo.com")
            c.drawString(143.7 * mm, height - 143.6 * mm, "Singapore")
            c.drawString(93.7 * mm, height - 148.6 * mm, "6788")
            
        if index == 0:
            # Calculate coordinates for text alignment
            text_x = 34.1 * mm
            text_y = height - 177.7 * mm
            
            # Split text into two lines
            text_lines = [
                "Shradhha impex",
                "308,fortune business centre,165,rnt marg,",
                "Indore,(m.p) 452001",
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )   
        if index == 0:
            # Calculate coordinates for text alignment
            text_x = 134.7 * mm
            text_y = height - 177.7 * mm
            
            # Split text into two lines
            text_lines = [
                "Alliance  divine impex pte ltd",
                "No 160 kallang way, 01-02",
                "Singapore 349246"
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )  
        if index == 0:
            # Calculate coordinates for text alignment
            text_x = 44.7 * mm
            text_y = height - 219.7 * mm
            
            # Split text into two lines
            text_lines = [
                "Bank of india",
                "No 130 Rnt Marg, 01-02",
                "Indore (M.P)"
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )
            if index == 0:
               number_str = "141712101"
               c.setFont("Helvetica-Bold", 10)

              # Define custom X and Y positions for each digit
               digit_positions = [
                 (40 * mm, height - 260 * mm),  # digit 1
                 (60 * mm, height - 260 * mm),  # digit 2
                 (90 * mm, height - 260 * mm),  # digit 3
                 (110 * mm, height - 260 * mm),  # digit 4
                 (130 * mm, height - 260 * mm),  # digit 5
                 (150 * mm, height - 260 * mm), # digit 6
                 (160 * mm, height - 260 * mm), # digit 7
                 (180 * mm, height - 260 * mm), # digit 8
                 (200 * mm, height - 260 * mm), # digit 9
                ]
               for digit, (x, y) in zip(number_str, digit_positions):
                c.drawString(x, y, digit)
            if index == 0:
               number_str = "141712101"
               c.setFont("Helvetica-Bold", 10)

              # Define custom X and Y positions for each digit
               digit_positions = [
                 (40 * mm, height - 265 * mm),  # digit 1
                 (60 * mm, height - 265 * mm),  # digit 2
                 (90 * mm, height - 265 * mm),  # digit 3
                 (110 * mm, height - 265 * mm),  # digit 4
                 (130 * mm, height - 265 * mm),  # digit 5
                 (150 * mm, height - 265 * mm), # digit 6
                 (160 * mm, height - 265 * mm), # digit 7
                 (180 * mm, height - 265 * mm), # digit 8
                 (200 * mm, height - 265 * mm), # digit 9
                ]
               for digit, (x, y) in zip(number_str, digit_positions):
                c.drawString(x, y, digit)
         
            # DATE box (DDMMYYYY) bottom
            date_str = "20042021"
            box_count = len(date_str)
            total_width = 55.2 * mm
            box_w = total_width / box_count
            date_box_x = 18.9 * mm
            date_box_y = height - 274.8 * mm - 6.1 * mm

            c.setFont("Helvetica-Bold", 11)
            for i, digit in enumerate(date_str):
                x = date_box_x + i * box_w + 2
                y = date_box_y + 6.1 * mm / 2 - 3
                c.drawString(x, y, digit)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 47 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm, 3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm, 3 * mm, 3 * mm]
           spacings = [0, 40 * mm, 58 * mm, 49 * mm]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(4):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 53 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm, 3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm, 3 * mm, 3 * mm]
           spacings = [0, 40 * mm, 58 * mm, 49 * mm]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(4):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 58 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm, 3 * mm]
           spacings = [0, 40 * mm, 58 * mm]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(3):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 65 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [175, 25 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 85 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [190, 23 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 93 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm,3 * mm]
           heights = [3 * mm, 3 * mm,3 * mm]
           spacings = [241, 23 * mm,16 * mm ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(3):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 0:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 133 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [120, 35 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
       
        if index == 1:
            c.setFont("Helvetica-Bold", 10)
            c.setFillColorRGB(0, 0, 0)

            # Fill basic details
            c.drawString(60.8 * mm, height - 90.5 * mm, "678332")  
            c.drawString(60.5 * mm, height - 95.5 * mm, "3784")  
            c.drawString(60.5 * mm, height - 102.5 * mm, "2123")
            c.drawString(37.5 * mm, height - 133.5 * mm, "Bank Of India") 
            c.drawString(50.5 * mm, height - 140.5 * mm, "31040000045021")
            c.drawString(60.5 * mm, height - 108.5 * mm, "47248") 
            c.drawString(125.5 * mm, height - 113.5 * mm, "21111")
            c.drawString(131.5 * mm, height - 122.5 * mm, "63797")
            c.drawString(46.5 * mm, height - 168.5 * mm, "77777")
            c.drawString(35.5 * mm, height - 148.5 * mm, "5697")
        if index == 1:
            # Calculate coordinates for text alignment
            text_x = 111.5 * mm
            text_y = height - 168.7 * mm
            
            # Split text into two lines
            text_lines = [
                "seventy seven lakh seven hundred seventy seven"
                
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )
        if index == 1:
            # Calculate coordinates for text alignment
            text_x = 10.5 * mm
            text_y = height - 198.7 * mm
            
            # Split text into two lines
            text_lines = [
                "Shipping documents received late due to customs clearance delays."
                
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )
        if index == 1:
            # Calculate coordinates for text alignment
            text_x = 10.5 * mm
            text_y = height - 230.7 * mm
            
            # Split text into two lines
            text_lines = [
                "Please credit proceeds to our EEFC account and notify us via email upon completion."
                
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )
                
         # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 1:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 55.3 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 17.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 270.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 11)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.9  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit) 
         # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 1:
         date_str = "21072021"
         box_count = len(date_str)
         total_box_width = 52.3 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 157.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 87.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.5  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit)  
         # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 1:
         date_str = "11042023"
         box_count = len(date_str)
         total_box_width = 52.3 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 157.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 93.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.5  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit) 
        if index == 1:
          # Number to be spaced and boxed
          number_str = "31040000002130"
          number_box_count = len(number_str)
          total_number_box_width = 82.1 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 40.6 * mm 
          number_box_y = height - 53.9* mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3               
            c.drawString(digit_x, digit_y, digit)
        if index == 1:
          # Number to be spaced and boxed
          number_str = "31040000002130"
          number_box_count = len(number_str)
          total_number_box_width = 82.1 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 40.6 * mm 
          number_box_y = height - 65.9* mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3               
            c.drawString(digit_x, digit_y, digit)
        if index == 1:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 26 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [215, 28 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 1:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 33 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [215, 28 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 1:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 45 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm,3 * mm,3 * mm]
           heights = [3 * mm, 3 * mm,3 * mm, 3 * mm]
           spacings = [113, 15 * mm,20*mm,18*mm ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(4):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        
        if index == 1:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 70 * mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [235, 32 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 1:
           tickbox_x = 6 * mm  # Starting X position
           tickbox_y = height - 208* mm  # Y position from top of the page

           # Define individual width, height, and spacing for each box
           widths = [3 * mm, 3 * mm]
           heights = [3 * mm, 3 * mm]
           spacings = [215, 37 * mm, ]  # Space from starting X or previous box

           c.setFillGray(0.7)
           current_x = tickbox_x

           for i in range(2):
             current_x += spacings[i]  # Move X by custom spacing
             # Draw filled box
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=1)
             # Draw outer border
             c.rect(current_x, tickbox_y, widths[i], heights[i], stroke=1, fill=0)
        if index == 1:  
         tickbox_width = 3* mm
         tickbox_height = 3 * mm
         tickbox_x = 5 * mm  # X position stays constant for vertical boxes
         tickbox_y = height - 115.2 * mm  # Starting Y position (adjusted based on image)

         vertical_spacing = 7* mm  # Space between each checkbox vertically

         c.setFillGray(0.7)

         # Draw 5 vertical tickboxes
         for i in range(2):
           y = tickbox_y - i * vertical_spacing
           # Fill with black or gray
           c.rect(tickbox_x, y, tickbox_width, tickbox_height, stroke=1, fill=1)
           # Outer border with no fill
           c.rect(tickbox_x, y, tickbox_width, tickbox_height, stroke=1, fill=0) 
        
         # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 2:
         date_str = "21072021"
         box_count = len(date_str)
         total_box_width = 52.3 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 20 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 200.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.5  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit) 
        if index == 2:  
         tickbox_width = 3* mm
         tickbox_height = 3 * mm
         tickbox_x = 8 * mm  # X position stays constant for vertical boxes
         tickbox_y = height - 228.2 * mm  # Starting Y position (adjusted based on image)

         vertical_spacing = 4* mm  # Space between each checkbox vertically

         c.setFillGray(0.7)

         # Draw 5 vertical tickboxes
         for i in range(4):
           y = tickbox_y - i * vertical_spacing
           # Fill with black or gray
           c.rect(tickbox_x, y, tickbox_width, tickbox_height, stroke=1, fill=1)
           # Outer border with no fill
           c.rect(tickbox_x, y, tickbox_width, tickbox_height, stroke=1, fill=0) 
        c.showPage()

    c.save()

# Run this script
if __name__ == "__main__":
    image_paths = [
        "export-bills-form_page-0001.jpg",
        "export-bills-form_page-0002.jpg",
        "export-bills-form_page-0003.jpg"
    ]
    create_export_bill_pdf(image_paths, "export_bill_filled8.pdf")

