from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import os

def get_next_filename(base_filename="Sales_Contract"):
    count = 1
    while os.path.exists(f"{base_filename}_{count}.pdf"):
        count += 1
    return f"{base_filename}_{count}.pdf"

def create_pdf():
    pdf_file = get_next_filename()
    c = canvas.Canvas(pdf_file, pagesize=A4)
    width, height = A4
    
    # Add Logo in Center
    logo_path = "exp.jpg"  # Ensure this file exists
    logo_width, logo_height = 80, 50
    c.drawImage(logo_path, (width / 2) - (logo_width / 2), height - 70, width=logo_width, height=logo_height)

    # Website Name (Left Side)
    c.setFont("Helvetica", 10)
    c.drawString(20, height - 40, "Website: www.shraddhaimpex.in")  

    # Company Name (Right Side)
    c.setFont("Helvetica-Bold", 16)
    c.drawRightString(width - 40, height - 40, "SHRADDHA IMPEX")

    # Seller’s Address Below Company Name
    c.setFont("Helvetica", 10)
    seller_address = ["308, Fortune Business Center", "Indore, M.P., India"]
    y_position = height - 55
    for line in seller_address:
        c.drawRightString(width - 40, y_position, line)
        y_position -= 12

    # Header Line
    c.line(20, y_position - 5, width - 20, y_position - 5)
    y_position -= 25

    # Centered Sales Contract Title
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width / 2, y_position, "SALES CONTRACT")

    # Contract Number & Date Below Title
    y_position -= 20
    c.setFont("Helvetica", 12)
    c.drawString(20, y_position, "Contract No: SI/COL/19/21-22")
    c.drawRightString(width - 40, y_position, "Date: 07.06.2021")

    # Notify Parties Section
    y_position -= 30
    seller_x = 20
    notify1_x = width / 2 - 90
    notify2_x = width - 140

    c.setFont("Helvetica-Bold", 12)
    c.drawString(seller_x, y_position, "Seller:")
    c.drawString(notify1_x, y_position, "Consignee:")
    c.drawString(notify2_x, y_position, "Notify:")

    y_position -= 15
    c.setFont("Helvetica", 10)
    seller_address = ["SHRADDHA IMPEX", "308, Fortune Business Center", "Indore, M.P., India"]
    notify1_address = ["SMART DRAGON LANKA PVT LTD", "Colombo 03, Sri Lanka"]
    notify2_address = ["DEVI GLOBAL HK LTD", "Centre, HK"]

    for i in range(max(len(seller_address), len(notify1_address), len(notify2_address))):
        if i < len(seller_address):
            c.drawString(seller_x, y_position, seller_address[i])
        if i < len(notify1_address):
            c.drawString(notify1_x, y_position, notify1_address[i])
        if i < len(notify2_address):
            c.drawString(notify2_x, y_position, notify2_address[i])
        y_position -= 15

    # Space Between Sections
    y_position -= 20

    # Product Table
    product_data = [["Product", "Quantity", "Price", "Amount"],
                    ["INDIAN WHITE SUGAR S30", "270 MTs", "USD 465 per Metric Ton", "USD 125010"]]
    product_table = Table(product_data, colWidths=[190, 90, 170, 90])
    product_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    product_table.wrapOn(c, width, height)
    product_table.drawOn(c, 20, y_position - 30)

    y_position -= 70  # Ensuring space between tables

    # Additional Details Table
    table_data = [["Details", "Information"],
                  ["Packing", "50 Kg Liner PP Bags"],
                  ["Loading Port", "Any Indian Port"],
                  ["Destination Port", "Colombo, Sri Lanka"],
                  ["Shipment", "On or before 20 June 2021"],
                  ["Documents", "Invoice, Packing List, Bill of Lading, Certificate of Origin"],
                  ["Seller’s Bank", "Bank of Baroda, RNT Road Branch, Indore, India"],
                  ["Account No", "314XXXXXXXXX"],
                  ["Arbitration", "As per the laws of India"]]
    details_table = Table(table_data, colWidths=[200, 340])
    details_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    details_table.wrapOn(c, width, height)
    details_table.drawOn(c, 20, y_position - 140)

    y_position -= 170  # Reduced space

    # Terms & Conditions Section
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20, y_position, "Terms & Conditions:")
    y_position -= 15
    c.setFont("Helvetica", 10)
    terms = [
        "1. The seller is not responsible for delays due to customs procedures.",
        "2. Payment terms should be strictly followed as per the contract.",
        "3. Any disputes shall be resolved as per the laws of India.",
        "4. Quality and quantity claims must be made within 7 days of delivery."
    ]
    for term in terms:
        c.drawString(20, y_position, term)
        y_position -= 12  # Compact spacing

    y_position -= 20  # Reduced space

    # Acceptance Section
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, y_position, "ACCEPTANCE")
    
    # Signature Section with Image
    y_position -= 25
    c.setFont("Helvetica-Bold", 10)
    # c.drawString(20, y_position, "Accepted By:")
    
    y_position -= 15
    c.drawString(20, y_position, "Seller:")
    c.drawString(width / 2 - 50, y_position, " Consignee:")
    c.drawString(width - 180, y_position, "Notify Party:")

    # Add Signature Image (Adjusted to prevent overlap)
    signature_path = "seal_sign.png"  # Ensure this file exists
    c.drawImage(signature_path, 20, y_position - 40, width=80, height=30)

    # # Footer
    # c.line(20, 40, width - 20, 40)
    # c.setFont("Helvetica", 8)
    # c.drawString(20, 28, "Website: www.shraddhaimpex.in")
    # c.drawRightString(width - 20, 28, "Page 1")
    
    c.save()
    print(f"PDF saved as {pdf_file}")

create_pdf()
