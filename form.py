from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_form_pdf(image_paths, output_filename):
    # A4 size in mm
    width, height = 210 * mm, 297 * mm  
    c = canvas.Canvas(output_filename, pagesize=(width, height))

    for index, image_path in enumerate(image_paths):
        c.drawImage(image_path, 0, 0, width=width, height=height)

        if index == 0:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)

            # Fill basic details on the first page
            c.drawString(89.8 * mm, height - 194.5 * mm, "chetna joshi")  # Branch Name
            c.drawString(67.5 * mm, height - 246.5 * mm, "19-04-2021") 
            c.drawString(103.5 * mm, height - 246.5 * mm, "28-04-2021") # Date
            c.drawString(63.6  * mm, height - 232.7 * mm, "2577445")# Account Number
        if index == 1:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)
            
            c.drawString(92.4  * mm, height - 28.7 * mm, "45000") 
            c.drawString(98.6  * mm, height - 47.7 * mm, "25-09-2021")
            c.drawString(47.8 * mm, height - 206.7 * mm, "Bank Of India")# Bank Name
            c.drawString(50.8 * mm, height - 211.7 * mm, "65,rnt marg,indore (m.p)")
            c.drawString(75.8 * mm, height - 66.7 * mm, "Gopal") 
            c.drawString(51.8 * mm, height - 71.7 * mm, "Road no 1 bhawarkuaa,indore(M.P) 452001")
            c.drawString(75.8 * mm, height - 108.7 * mm, "308,fortune business centre,165,rnt marg,Indore,(m.p)") 
            c.drawString(125.4  * mm, height - 150.7 * mm, "Alliance divine impex pte ltd") 
            c.drawString(50.4  * mm, height - 155.7 * mm, "No 160 kallang way, 01-02, Singapore 349246") 
            c.drawString(44.8 * mm, height - 80.7 * mm, "Indore") 
            c.drawString(61.8 * mm, height - 85.7 * mm, "7924882190") 
            c.drawString(47.8 * mm, height - 89.7 * mm, "shradhha@yahoo.com")
            c.drawString(61.8 * mm, height - 94.7 * mm, "Mohan")
            c.drawString(71.8 * mm, height - 99.7 * mm, "423301") 
            c.drawString(129.8 * mm, height - 80.7 * mm, "India") 
            c.drawString(133.8 * mm, height - 85.7 * mm, "32248") 
            c.drawString(129.8 * mm, height - 89.7 * mm, "www.abc.com")
            c.drawString(139.8 * mm, height - 94.7 * mm, "93469950766")
            c.drawString(127.8 * mm, height - 99.7 * mm, "233901") 
            c.drawString(44.8 * mm, height - 118.7 * mm, "Bhopal") 
            c.drawString(61.8 * mm, height - 123.7 * mm, "7924882190") 
            c.drawString(47.8 * mm, height - 127.7 * mm, "shradhha@yahoo.com")
            c.drawString(61.8 * mm, height - 132.7 * mm, "Arti")
            c.drawString(71.8 * mm, height - 137.7 * mm, "728310") 
            c.drawString(129.8 * mm, height - 118.7 * mm, "India") 
            c.drawString(133.8 * mm, height - 123.7 * mm, "69820") 
            c.drawString(129.8 * mm, height - 127.7 * mm, "www.xyz.com")
            c.drawString(139.8 * mm, height - 132.7 * mm, "8820345899")
            c.drawString(127.8 * mm, height - 137.7 * mm, "723301")  
            c.drawString(42.8 * mm, height - 220.7 * mm, "Ujjain") 
            c.drawString(61.8 * mm, height - 225.7 * mm, "8789982190") 
            c.drawString(47.8 * mm, height - 230.7 * mm, "codex@yahoo.com")
            c.drawString(60.8 * mm, height - 235.7 * mm, "66423301") 
            c.drawString(127.8 * mm, height - 220.7 * mm, "India")
            c.drawString(133.8 * mm, height - 225.7 * mm, "82190")  
            c.drawString(140.8 * mm, height - 235.7 * mm, "99820") 
            c.drawString(44.8 * mm, height - 164.7 * mm, "Nagpur") 
            c.drawString(61.8 * mm, height - 169.7 * mm, "928882107") 
            c.drawString(47.8 * mm, height - 174.7 * mm, "shradhha@yahoo.com")
            c.drawString(61.8 * mm, height - 178.7 * mm, "Raj")
            c.drawString(71.8 * mm, height - 183.7 * mm, "796085")
            c.drawString(129.8 * mm, height - 164.7 * mm, "Singapore") 
            c.drawString(133.8 * mm, height - 169.7 * mm, "670034") 
            c.drawString(129.8 * mm, height - 174.7 * mm, "www.bhg.com")
            c.drawString(139.8 * mm, height - 178.7 * mm, "8456889031")
            c.drawString(127.8 * mm, height - 183.7 * mm, "60500") 
            c.drawString(69.8 * mm, height - 244.7 * mm, "Sugar") 
            c.drawString(126.8 * mm, height - 253.7 * mm, "India") 
            c.drawString(92.8 * mm, height - 263.7 * mm, "Singapore")
        if index == 2:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)
            
            c.drawString(62.8 * mm, height - 42.7 * mm, "45000") 
            c.drawString(133.8 * mm, height - 42.7 * mm, "4") 
            c.drawString(66.8 * mm, height - 85.7 * mm, "20000")
            c.drawString(133.8 * mm, height - 85.7 * mm, "2") 
            c.drawString(50.8 * mm, height - 57.7 * mm, "3")
            c.drawString(115.8 * mm, height - 57.7 * mm, "1500")
            c.drawString(166.8 * mm, height - 57.7 * mm, "5")  
            c.drawString(57.8 * mm, height - 238.7 * mm, "34796")
            c.drawString(137.8 * mm, height - 238.7 * mm, "50000")
            c.drawString(47.8 * mm, height - 243.7 * mm, "67087") 
            c.drawString(91.8 * mm, height - 238.7 * mm, "21-04-2021")  
            c.drawString(41.8 * mm, height - 252.7 * mm, "Indore")
            c.drawString(40.8 * mm, height - 257.7 * mm, "11-04-2021")
            c.drawString(167.8 * mm, height - 148.7 * mm, "Answer") 
            c.drawString(158.8 * mm, height - 159.7 * mm, "Answer") 
            c.drawString(134.8 * mm, height - 163.7 * mm,"Answer") 
            c.drawString(140.8 * mm, height - 168.7 * mm, "Answer") 
            c.drawString(171.8 * mm, height - 172.7 * mm, "Answer") 
            c.drawString(167.8 * mm, height - 181.7 * mm, "Answer") 
            c.drawString(167.8 * mm, height - 195.7 * mm, "Answer") 
            c.drawString(167.8 * mm, height - 217.7 * mm, "Answer") 
        if index == 2:
               number_str = "1417121089238497506782574490"
               c.setFont("Helvetica-Bold", 10)

              # Define custom X and Y positions for each digit
               digit_positions = [
                 (35 * mm, height - 125* mm),  # digit 1
                 (50 * mm, height - 125 * mm),  # digit 2
                 (70 * mm, height - 125 * mm),  # digit 3
                 (90 * mm, height - 125 * mm),  # digit 4
                 (110 * mm, height - 125 * mm),  # digit 5
                 (130 * mm, height - 125 * mm), # digit 6
                 (160 * mm, height - 125 * mm), # digit 7
                 (35 * mm, height - 130* mm),  # digit 1
                 (50 * mm, height - 130 * mm),  # digit 2
                 (70 * mm, height - 130 * mm),  # digit 3
                 (90 * mm, height - 130 * mm),  # digit 4
                 (110 * mm, height - 130 * mm),  # digit 5
                 (130 * mm, height - 130 * mm), # digit 6
                 (160 * mm, height - 130 * mm), # digit 7
                 (35 * mm, height - 135* mm),  # digit 1
                 (50 * mm, height - 135 * mm),  # digit 2
                 (70 * mm, height - 135 * mm),  # digit 3
                 (90 * mm, height - 135 * mm),  # digit 4
                 (110 * mm, height - 135 * mm),  # digit 5
                 (130 * mm, height - 135 * mm), # digit 6
                 (160 * mm, height - 135 * mm), # digit 7
                 (35 * mm, height - 140* mm),  # digit 1
                 (50 * mm, height - 140 * mm),  # digit 2
                 (70 * mm, height - 140 * mm),  # digit 3
                 (90 * mm, height - 140 * mm),  # digit 4
                 (110 * mm, height - 140 * mm),  # digit 5
                 (130 * mm, height - 140 * mm), # digit 6
                 (160 * mm, height - 140 * mm), # digit 7


                ]
               for digit, (x, y) in zip(number_str, digit_positions):
                c.drawString(x, y, digit)
        if index == 3:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColorRGB(0, 0, 0)
            
            c.drawString(106.8 * mm, height - 66.7 * mm, "Answer") 
            c.drawString(118.8 * mm, height - 71.7 * mm, "Answer") 
            c.drawString(134.8 * mm, height - 75.7 * mm,"Answer") 
            c.drawString(140.8 * mm, height - 88.7 * mm, "Answer") 
            c.drawString(155.8 * mm, height - 99.7 * mm, "Answer") 
            c.drawString(115.8 * mm, height - 120.7 * mm, "Answer") 
            c.drawString(125.8 * mm, height - 136.7 * mm, "Answer") 
            c.drawString(125.8 * mm, height - 141.7 * mm, "Answer")
            c.drawString(125.8 * mm, height - 146.7 * mm, "Answer") 
            c.drawString(125.8 * mm, height - 151.7 * mm, "Answer")         
                   
             
        c.showPage()  # Add this inside the loop

    c.save()

# Run this script
if __name__ == "__main__":
    image_paths = [
        "01 Form-0001.jpg",
        "01 Form-0002.jpg",
        "01 Form-0003.jpg",
        "01 Form-0004.jpg"
    ]
    create_form_pdf(image_paths, "form9.pdf")


