from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_form_page_pdf(image_paths, output_filename):
    # A4 size in mm
    width, height = 210 * mm, 297 * mm  
    c = canvas.Canvas(output_filename, pagesize=(width, height))

    for index, image_path in enumerate(image_paths):
        c.drawImage(image_path, 0, 0, width=width, height=height)

        if index == 0:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)

            # Fill basic details on the first page
            c.drawString(89.8 * mm, height - 186.5 * mm, " Arti")
            c.drawString(63.6  * mm, height - 218.7 * mm, "2577445")# Branch Name
            c.drawString(67.5 * mm, height - 228.5 * mm, "19-04-2021") 
            c.drawString(103.5 * mm, height - 228.5 * mm, "28-04-2021")
            c.drawString(92.4  * mm, height - 243.7 * mm, "49000") 
            c.drawString(104.8 * mm, height - 257.7 * mm, "11-04-2021")
            
        if index == 1:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)
            
            c.drawString(75.8 * mm, height - 27.7 * mm, "Gopal") 
            c.drawString(51.8 * mm, height - 33.7 * mm, "Road no 1 bhawarkuaa,indore(M.P) 452001")
            c.drawString(47.8 * mm, height - 75.7 * mm, "Bank Of India")# Bank Name
            c.drawString(53.8 * mm, height - 80.7 * mm, "65,rnt marg,indore (m.p)")

            c.drawString(44.8 * mm, height - 42.7 * mm, "Indore") 
            c.drawString(61.8 * mm, height - 48.7 * mm, "7924882190") 
            c.drawString(47.8 * mm, height - 52.7 * mm, "shradhha@yahoo.com")
            c.drawString(61.8 * mm, height - 57.7 * mm, "Mohan")
            c.drawString(71.8 * mm, height - 62.7 * mm, "423301") 
            c.drawString(129.8 * mm, height - 42.7 * mm, "India") 
            c.drawString(133.8 * mm, height - 48.7 * mm, "32248") 
            c.drawString(129.8 * mm, height - 52.7 * mm, "www.abc.com")
            c.drawString(139.8 * mm, height - 57.7 * mm, "93469950766")
            c.drawString(127.8 * mm, height - 62.7 * mm, "233901") 
  
            c.drawString(42.8 * mm, height - 90.7 * mm, "Ujjain") 
            c.drawString(61.8 * mm, height - 94.7 * mm, "8789982190") 
            c.drawString(47.8 * mm, height - 98.7 * mm, "codex@yahoo.com")
            c.drawString(60.8 * mm, height - 103.7 * mm, "66423301") 
            c.drawString(129.8 * mm, height - 90.7 * mm, "India") 
            c.drawString(133.8 * mm, height - 94.7 * mm, "600301") 
            c.drawString(141.8 * mm, height - 103.7 * mm, "2323301") 
            c.drawString(70.8 * mm, height - 118.7 * mm, "SUGAR")
            c.drawString(125.8 * mm, height - 127.7 * mm, "INDORE")
            c.drawString(92.8 * mm, height - 137.7 * mm, "SINGAPORE") 
            
            c.drawString(62.8 * mm, height - 155.7 * mm, "45000") 
            c.drawString(133.8 * mm, height - 155.7 * mm, "4") 
            c.drawString(66.8 * mm, height - 183.7 * mm, "20000")
            c.drawString(133.8 * mm, height - 183.7 * mm, "2") 
            c.drawString(50.8 * mm, height - 170.7 * mm, "3")
            c.drawString(115.8 * mm, height - 170.7 * mm, "1500")
            c.drawString(166.8 * mm, height - 170.7 * mm, "5") 
            c.drawString(66.8 * mm, height - 207.7 * mm, "10000")
            c.drawString(133.8 * mm, height - 207.7 * mm, "7") 
        if index == 2:
               number_str = "1417121089238497506782574490"
               c.setFont("Helvetica-Bold", 10)    
             
               c.drawString(57.8 * mm, height - 117.7 * mm, "34796")
               c.drawString(137.8 * mm, height - 117.7 * mm, "50000")
               c.drawString(48.8 * mm, height - 122.7 * mm, "67087") 
               c.drawString(91.8 * mm, height - 117.7 * mm, "21-04-2021")  
               c.drawString(42.8 * mm, height - 132.7 * mm, "Indore")
               c.drawString(42.8 * mm, height - 137.7 * mm, "31-04-2021")
            
            
        if index == 1:
               number_str = "1417121089238497506782574490"
               c.setFont("Helvetica-Bold", 10)

              # Define custom X and Y positions for each digit
               digit_positions = [
                 (35 * mm, height - 246* mm),  # digit 1
                 (50 * mm, height - 246 * mm),  # digit 2
                 (70 * mm, height - 246 * mm),  # digit 3
                 (90 * mm, height - 246 * mm),  # digit 4
                 (110 * mm, height - 246 * mm),  # digit 5
                 (130 * mm, height - 246 * mm), # digit 6
                 (160 * mm, height - 246 * mm), # digit 7
                 (35 * mm, height - 251* mm),  # digit 1
                 (50 * mm, height - 251 * mm),  # digit 2
                 (70 * mm, height - 251 * mm),  # digit 3
                 (90 * mm, height - 251 * mm),  # digit 4
                 (110 * mm, height - 251 * mm),  # digit 5
                 (130 * mm, height - 251 * mm), # digit 6
                 (160 * mm, height - 251 * mm), # digit 7
                 (35 * mm, height - 256* mm),  # digit 1
                 (50 * mm, height - 256 * mm),  # digit 2
                 (70 * mm, height - 256 * mm),  # digit 3
                 (90 * mm, height - 256 * mm),  # digit 4
                 (110 * mm, height - 256 * mm),  # digit 5
                 (130 * mm, height - 256 * mm), # digit 6
                 (160 * mm, height - 256 * mm), # digit 7
                 (35 * mm, height - 261* mm),  # digit 1
                 (50 * mm, height - 261 * mm),  # digit 2
                 (70 * mm, height - 261 * mm),  # digit 3
                 (90 * mm, height - 261 * mm),  # digit 4
                 (110 * mm, height - 261 * mm),  # digit 5
                 (130 * mm, height - 261 * mm), # digit 6
                 (160 * mm, height - 261 * mm), # digit 7


                ]
               for digit, (x, y) in zip(number_str, digit_positions):
                c.drawString(x, y, digit)
        if index == 2:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)     
            c.drawString(167.8 * mm, height - 28.7 * mm, "Answer") 
            c.drawString(163.8 * mm, height - 38.7 * mm, "Answer") 
            c.drawString(137.8 * mm, height -43.7 * mm, "Answer") 
            c.drawString(144.8 * mm, height - 47.7 * mm, "Answer") 
            c.drawString(172.8 * mm, height - 50.7 * mm, "Answer") 
            c.drawString(168.8 * mm, height - 61.7 * mm, "Answer") 
            c.drawString(170.8 * mm, height - 74.7 * mm, "Answer")
            c.drawString(175.8 * mm, height - 102.7 * mm, "Answer") 
            c.drawString(107.8 * mm, height - 165.7 * mm, "Answer") 
            c.drawString(117.8 * mm, height - 170.7 * mm, "Answer") 
            c.drawString(135.8 * mm, height - 175.7 * mm, "Answer")
            c.drawString(135.8 * mm, height - 189.7 * mm, "Answer") 
            c.drawString(156.8 * mm, height - 199.7 * mm, "Answer") 
            c.drawString(98.8 * mm, height - 220.7 * mm, "Answer")
            c.drawString(113.8 * mm, height - 235.7 * mm, "Answer")    
            c.drawString(113.8 * mm, height - 240.7 * mm, "Answer") 
            c.drawString(120.8 * mm, height - 245.7 * mm, "Answer") 
            c.drawString(95.8 * mm, height - 254.7 * mm, "Answer") 
             
        c.showPage()  # Add this inside the loop

    c.save()

# Run this script
if __name__ == "__main__":
    image_paths = [
        "02 Form-0001.jpg",
        "02 Form-0002.jpg",
        "02 Form-0003.jpg"
    ]
    create_form_page_pdf(image_paths, "form-page8.pdf")


