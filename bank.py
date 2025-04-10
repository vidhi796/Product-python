from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_pdf_with_images(image_paths, output_filename):
    # A4 size in mm (210mm x 297mm)
    width, height = 210 * mm, 297 * mm  
    
    # Create canvas with custom size
    c = canvas.Canvas(output_filename, pagesize=(width, height))
    
    for index, image_path in enumerate(image_paths):
        # Draw image covering entire page
        c.drawImage(image_path, 0, 0, width=width, height=height)
        # Add text ONLY on first page
        if index == 0:
        # Set text properties
          c.setFont("Helvetica-Bold", 10)
          c.setFillColorRGB(0, 0, 0)  # Black text

        # Adjust these coordinates as per your needs
          c.drawString(170.4 * mm, height - 19.3 * mm, "Vijay Nagar")
          c.drawString(44.6 * mm, height - 31.8 * mm, "Shraddha Impex")
          c.drawString(44.3 * mm, height - 37.5 * mm, "31740200000014")
          c.drawString(63.3 * mm, height - 43.5 * mm, "Agri Export")
          c.drawString(160.3 * mm, height - 44.3 * mm, "Sugar")
          c.drawString(48.5 * mm, height - 57.9 * mm, "USD")
          c.drawString(46.9 * mm, height - 64.7 * mm, "77777777")
          c.drawString(47.9 * mm, height - 71.7 * mm, "Farmex freshia trading llc")
          c.drawString(47.2 * mm, height - 79.4 * mm, "Po box 378993 ,alras  dearia, dubai,uae,trn:100200997730003")
          c.drawString(29.9 * mm, height - 94.4 * mm, "P0103")
          c.drawString(85.8 * mm, height - 94.4 * mm, "Advance for export")
          c.drawString(66.2 * mm, height - 200.9 * mm, "19256")
          c.drawString(65.5 * mm, height - 210.4 * mm, "12789")
          c.drawString(67 * mm, height - 219.4 * mm, "12345")
          c.drawString(173.9 * mm, height - 219.4 * mm, "19.89")
          
          
       # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 52.2 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 153.8 * mm
         date_box_height = 5.12 * mm
         date_box_y = height - 99.8 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.7  
            digit_y = date_box_y + date_box_height / 2 - 3         
            c.drawString(digit_x, digit_y, digit)

        if index == 0:
         # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 122.5 * mm 
          number_box_y = height - 137.9 * mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3              
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            )
        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 122.5 * mm 
          number_box_y = height - 145.3 * mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7  
            digit_y = number_box_y + number_box_height / 2 - 3              
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            )   

        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 122.5 * mm 
          number_box_y = height - 152.3 * mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7  
            digit_y = number_box_y + number_box_height / 2 - 3              
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            )   

        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 122.5 * mm 
          number_box_y = height - 159.3 * mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3              
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            )   

        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 122.5 * mm 
          number_box_y = height - 170.3 * mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3              
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            )   
       
        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 44.3 * mm 
          number_box_y = height - 181.3 * mm  # Convert from top to bottom
          number_box_height = 6.2 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7  
            digit_y = number_box_y + number_box_height / 2 - 3              
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            )   

        if index == 0:
          # Number to be spaced and boxed
          number_str = "31740200000014"
          number_box_count = len(number_str)
          total_number_box_width = 82.5 * mm
          individual_number_box_width = total_number_box_width / number_box_count

          number_box_x = 122.5 * mm 
          number_box_y = height - 145.3 * mm  # Convert from top to bottom
          number_box_height = 6.1 * mm

          c.setFont("Helvetica-Bold", 10)

          for i, digit in enumerate(number_str):
            digit_x = number_box_x + i * individual_number_box_width + 1.7 
            digit_y = number_box_y + number_box_height / 2 - 3               
            c.drawString(digit_x, digit_y, digit)

           # Draw each digit box
            c.rect(
             number_box_x + i * individual_number_box_width,
             number_box_y,
             individual_number_box_width,
             number_box_height,
             stroke=1,
             fill=0
            ) 
                
        if index == 0:
            # Calculate coordinates for text alignment
            text_x = 115.5 * mm
            text_y = height - 57.7 * mm
            
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
                      
                      # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 46.6 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 159.8 * mm
         date_box_height = 6.2 * mm
         date_box_y = height - 199.8 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.7
            digit_y = date_box_y + date_box_height / 2 - 3         
            c.drawString(digit_x, digit_y, digit)
            
                # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 46.4 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 159.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 206.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.7  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit)
            
        # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 0:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 55.4 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 20.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 235.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.7  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit)
            
        # Date Box Section (Cleanly spaced DDMMYYYY)
        if index == 1:
         date_str = "21042025"
         box_count = len(date_str)
         total_box_width = 55.3 * mm
         individual_box_width = total_box_width / box_count

         date_box_x = 20.8 * mm
         date_box_height = 6.5 * mm
         date_box_y = height - 235.2 * mm - date_box_height

         c.setFont("Helvetica-Bold", 10)

         for i, digit in enumerate(date_str):
            digit_x = date_box_x + i * individual_box_width + 1.7  
            digit_y = date_box_y + date_box_height / 2 - 3        
            c.drawString(digit_x, digit_y, digit)
        if index == 0:
            
            tickbox_width = 4 * mm  # 4.46 cm
            tickbox_height = 4 * mm  # 2.29 cm
            tickbox_x = 45.5 * mm  # Adjust X position as needed
            tickbox_y = height - 27.3 * mm  # Adjust Y position 
            
            c.setFillGray(0.7)
            
            # Draw 3 black-filled tickboxes with border
            for offset in [0, 55, 121.2]:
             c.rect(
                 tickbox_x + offset * mm,
                 tickbox_y,
                 tickbox_width,
                 tickbox_height,
                 stroke=1,
                 fill=1
                )

            # Draw rectangle for tick box
            c.rect(
                tickbox_x,
                tickbox_y,
                tickbox_width,
                tickbox_height,
                stroke=1,  # Border visibility
                fill=0    # No fill
            )
            # Second rectangle (10mm to the right)
            c.rect(
               tickbox_x + 55 * mm,  # Move right by 10mm
               tickbox_y,
               tickbox_width,
               tickbox_height,
               stroke=1,
              fill=0
            )
    
            # Third rectangle (20mm to the right from first)
            c.rect(
             tickbox_x + 121.2 * mm,  # Move right by 20mm
             tickbox_y,
             tickbox_width,
             tickbox_height,
             stroke=1,
             fill=0
            )
        # Start new page for next image
        c.showPage()
        
    # Save PDF
    c.save()

if __name__ == "__main__":
    image_paths = [
        "BOB-page-0001.jpg",
        "BOB-page-0002.jpg",
        "BOB-page-0003.jpg",
        "BOB-page-0004.jpg",
        "BOB-page-0005.jpg",
        "BOB-page-0006.jpg"
    ]
    create_pdf_with_images(image_paths, "output3.pdf")