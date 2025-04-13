from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_pdf_with_images(image_paths, output_filename):
    # A4 size in mm
    width, height = 210 * mm, 297 * mm  
    
    c = canvas.Canvas(output_filename, pagesize=(width, height))
    
    for index, image_path in enumerate(image_paths):
        c.drawImage(image_path, 0, 0, width=width, height=height)

        if index == 0:
            c.setFont("Helvetica-Bold", 10)
            c.setFillColorRGB(0, 0, 0)  # Black

            # Add text on the first page (image 1)
            c.drawString(176 * mm, height - 20.5 * mm, "annapurna")  # Branch Name
            c.drawString(165 * mm, height - 26.5 * mm, "11-04-2025")   # Date

            c.drawString(44 * mm, height - 45.5 * mm, "Shraddha Impex")
            c.drawString(45 * mm, height - 49.8 * mm, "308,fortune business centre,165,rnt marg,indore")
            c.drawString(46 * mm, height - 60.7 * mm, "Aarti khale")
            c.drawString(46 * mm, height - 66.9 * mm, "9876543210")
            c.drawString(46 * mm, height - 72.9 * mm, "91103004999")
            c.drawString(130 * mm, height - 66.9 * mm, "shradhaimpacs@yahoo.com")
            c.drawString(68.5 * mm, height - 99.4 * mm, "SI48/20-21")

            c.drawString(146.9 * mm, height - 99.4 * mm, "10.03.2021")
            c.drawString(149.2 * mm, height - 105.2 * mm, "Sugar")
            c.drawString(47.7 * mm, height - 110 * mm, "INR")
            c.drawString(46 * mm, height - 115.9 * mm, "60000000")
            c.drawString(146.9 * mm, height - 122.3 * mm, "17019910")
            c.drawString(50.5 * mm, height - 125.6 * mm, "India")
            c.drawString(150.9 * mm, height - 127.5* mm, "singapore")
            c.drawString(46 * mm, height - 136.5* mm, "pixa goan pty ltd")
            c.drawString(45 * mm, height - 144.5 * mm, "unit 11-h,19-21 george street north starthfeld,new souuth wales 2137,australia")
            c.drawString(61.2 * mm, height - 189.9 * mm, "3574")
            c.drawString(61.2 * mm, height - 197.2 * mm, "567324")
            c.drawString(61.2 * mm, height - 202.2 * mm, "78534")
            c.drawString(47.7* mm, height - 237.2 * mm, "INR")
            c.drawString(47.2 * mm, height - 243.2 * mm, "777777")
           
        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.1 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 42.6 * mm 
          number_box_y = height - 168.9* mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3               
            c.drawString(digit_x, digit_y, digit)

       
           # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 55.2 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 18.9 * mm
         date_box_height = 340.5 * mm
         date_box_y = height - 99.8 * mm - date_box_height

         c.setFont("Helvetica-Bold", 11)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 2  
            digit_y = date_box_y + date_box_height / 2 - 3         
            c.drawString(digit_x, digit_y, digit)
        # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 51.4 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 158.1 * mm
         date_box_height = 183.5 * mm
         date_box_y = height - 99.8 * mm - date_box_height

         c.setFont("Helvetica-Bold", 11)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 2  
            digit_y = date_box_y + date_box_height / 2 - 3         
            c.drawString(digit_x, digit_y, digit)
        # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 51.4 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 158.1 * mm
         date_box_height = 193.5 * mm
         date_box_y = height - 99.8 * mm - date_box_height

         c.setFont("Helvetica-Bold", 11)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 2  
            digit_y = date_box_y + date_box_height / 2 - 3         
            c.drawString(digit_x, digit_y, digit)
        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.1 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 47.6 * mm 
          number_box_y = height - 223.9* mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3               
            c.drawString(digit_x, digit_y, digit)
        if index == 0:
            # Calculate coordinates for text alignment
            text_x = 115.5 * mm
            text_y = height - 238.7 * mm
            
            # Split text into two lines
            text_lines = [
                "Seven crore seventy seven lakh",
                "seven hundred seventy seven only"
            ]
            line_height = 4 * mm  
            for i, line in enumerate(text_lines):
                c.drawString(
                    text_x,
                    text_y - (i * line_height),
                    line
                )
        if index == 0:
          tickbox_width = 4 * mm
          tickbox_height = 3 * mm
          tickbox_x = 76.9 * mm  # Starting X position (adjusted to match box near PC)
          tickbox_y = height - 29 * mm  # Y position (based on top line of the form)

          spacing = 45.2 * mm  # Horizontal spacing between the two tickboxes

          c.setFillGray(0.7)

          for i in range(2):
            x = tickbox_x + i * spacing
            # Fill box with gray
            c.rect(x, tickbox_y, tickbox_width, tickbox_height, stroke=1, fill=1)
            # Draw outer border
            c.rect(x, tickbox_y, tickbox_width, tickbox_height, stroke=1, fill=0)

         # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 1:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 55.3 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 15.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 233.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 12)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.9  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit)
        if index == 1:
            
           
         tickbox_width = 4 * mm
         tickbox_height = 4 * mm
         tickbox_x = 8 * mm  # X position stays constant for vertical boxes
         tickbox_y = height - 265.2 * mm  # Starting Y position (adjusted based on image)

         vertical_spacing = 5.5* mm  # Space between each checkbox vertically

         c.setFillGray(0.7)

         # Draw 5 vertical tickboxes
         for i in range(5):
           y = tickbox_y - i * vertical_spacing
           # Fill with black or gray
           c.rect(tickbox_x, y, tickbox_width, tickbox_height, stroke=1, fill=1)
           # Outer border with no fill
           c.rect(tickbox_x, y, tickbox_width, tickbox_height, stroke=1, fill=0)
        c.showPage()

    c.save()

# Run this when executing the script
if __name__ == "__main__":
    image_paths = [
        "packing-credit-0001.jpg",  # First image (text added)
        "packing-credit-0002.jpg"   # Second image (just added as-is)
    ]
    create_pdf_with_images(image_paths, "packing_credit16.pdf")
