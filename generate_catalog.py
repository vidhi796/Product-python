import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, PageTemplate, Frame, Flowable
from reportlab.lib.styles import getSampleStyleSheet, TA_CENTER, TA_LEFT, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

PAGE_WIDTH, PAGE_HEIGHT = A4

def _product_page_layout(canvas_obj, doc):
    canvas_obj.saveState()
    
    # Set plain white background for all pages
    canvas_obj.setFillColor(colors.white)
    canvas_obj.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)

    # Removed header as per new product page layout
    # header_height = 1.5 * inch
    # canvas_obj.setFillColor(colors.HexColor('#2C3E50'))
    # canvas_obj.rect(0, PAGE_HEIGHT - header_height, PAGE_WIDTH, header_height, fill=1)
    
    # Removed logo as per new product page layout
    # try:
    #     logo_path = 'logo.png'
    #     if os.path.exists(logo_path):
    #         logo_width = 1.0 * inch
    #         logo_height = 1.0 * inch
    #         logo = Image(logo_path, width=logo_width, height=logo_height)
    #         logo_x = 0.5 * inch
    #         logo_y = PAGE_HEIGHT - header_height + (header_height - logo_height) / 2
    #         logo.drawOn(canvas_obj, logo_x, logo_y)
    # except Exception as e:
    #     print(f"Could not load logo: {e}")
    #     pass
    
    # Removed company name as per new product page layout
    # canvas_obj.setFillColor(colors.white)
    # canvas_obj.setFont('Helvetica-Bold', 24)
    # canvas_obj.drawString(1.8*inch, PAGE_HEIGHT - 1.0*inch, "COMPANY NAME")
    
    # Removed footer as per new product page layout
    # footer_height = 0.5 * inch
    # canvas_obj.setFillColor(colors.HexColor('#34495E'))
    # canvas_obj.rect(0, 0, PAGE_WIDTH, footer_height, fill=1)
    
    # Removed page number as per new product page layout
    # canvas_obj.setFillColor(colors.white)
    # canvas_obj.setFont('Helvetica', 10)
    # canvas_obj.drawRightString(PAGE_WIDTH - 0.5*inch, 0.25*inch, f"Page {doc.page}")
    
    canvas_obj.restoreState()

def _cover_page_layout(canvas_obj, doc):
    canvas_obj.saveState()

    # Set plain white background for the cover page
    canvas_obj.setFillColor(colors.white)
    canvas_obj.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1)

    # Company Name/Brand (RIMBERIO FURNITURE)
    canvas_obj.setFillColor(colors.HexColor('#5CB85C'))  # Green color for brand name
    canvas_obj.setFont('Helvetica', 14)
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 1.8 * inch, "RIMBERIO FURNITURE")

    # Main Title: PRODUCT CATALOG
    canvas_obj.setFillColor(colors.HexColor('#2C3E50'))  # Dark blue-gray
    canvas_obj.setFont('Helvetica-Bold', 60) # Increased font size
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 2.5 * inch, "PRODUCT") # Adjusted Y position
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 3.5 * inch, "CATALOG") # Adjusted Y position

    # Year: 2023 with green background
    year_text = "2023"
    year_font_size = 24
    canvas_obj.setFont('Helvetica', year_font_size)
    
    # Calculate text width to size the rectangle
    text_width = canvas_obj.stringWidth(year_text, 'Helvetica', year_font_size)
    rect_padding = 0.2 * inch
    rect_width = text_width + 2 * rect_padding
    rect_height = year_font_size * 1.5 # Approximate height for the rectangle
    
    # Position the rectangle and text, rotated
    canvas_obj.setFillColor(colors.HexColor('#5CB85C'))  # Green background for year
    # Rotate and draw rectangle
    canvas_obj.translate(PAGE_WIDTH - 0.75 * inch, PAGE_HEIGHT - 1.5 * inch) # Move origin to desired bottom-left of rotated object
    canvas_obj.rotate(90)
    canvas_obj.rect(0, 0, rect_height, -rect_width, fill=1, stroke=0) # Draw rectangle
    
    # Draw text on top of the rectangle
    canvas_obj.setFillColor(colors.white) # White text for the year
    canvas_obj.drawString(rect_height / 2 - text_width / 2, -rect_width + rect_padding, year_text) # Position text within rectangle
    
    canvas_obj.rotate(-90) # Rotate back
    canvas_obj.translate(-(PAGE_WIDTH - 0.75 * inch), -(PAGE_HEIGHT - 1.5 * inch)) # Move origin back

    # Add furniture image
    try:
        chair_img_path = 'img5.jpg' # Reverted to img5.jpg as ship_cover.jpg is not provided
        if os.path.exists(chair_img_path):
            chair_img = Image(chair_img_path, width=4.5*inch, height=5.5*inch) # Adjusted size back to furniture
            img_w, img_h = chair_img.wrapOn(canvas_obj, 4.5*inch, 5.5*inch)
            # Position the image centrally below the titles
            chair_img.drawOn(canvas_obj, (PAGE_WIDTH - img_w) / 2, PAGE_HEIGHT - 3.5 * inch - img_h - 0.5 * inch)
    except Exception as e:
        print(f"Could not load furniture image: {e}")
        pass

    # Website URL and address at the bottom
    canvas_obj.setFillColor(colors.HexColor('#2C3E50'))
    canvas_obj.setFont('Helvetica', 10) # Smaller font for footer text
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, 0.75 * inch, "www.reallygreatsite.com / @reallygreatsite")
    canvas_obj.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch, "123 Anywhere St., Any City") # Added address

    canvas_obj.restoreState()

class ProductDetailFlowable(Flowable):
    def __init__(self, product_data, styles):
        Flowable.__init__(self)
        self.product_data = product_data
        self.styles = styles
        self.name = product_data[0]
        self.description = product_data[1]
        self.specifications = product_data[2]
        self.hs_code = product_data[3] # Store HS Code
        self.image_path = product_data[9]
        self.price = product_data[10] if len(product_data) > 10 else "N/A"
        self.second_image_path = product_data[11] if len(product_data) > 11 else None

        # Define desired ratios for element sizing
        self._main_image_width_ratio = 0.45  # Increased main image width
        self._main_image_aspect_ratio = 0.85  # Slightly taller than wide for main image
        self._text_area_width_ratio = 0.45  # Matches main image width for text
        self._second_image_width_ratio = 0.45  # Increased width for the second image
        self._second_image_height_ratio = 0.85  # Slightly shorter than full height

        # Store paragraph objects with enhanced styles for better headings
        self.price_para = Paragraph(f'{self.price}', styles['ProductPrice'])
        self.name_para = Paragraph(f'<b>{self.name.upper()}</b>', styles['ProductName'])
        self.desc_para = Paragraph(f'{self.description}', styles['ProductDescription'])
        self.specs_para_title = Paragraph('<font color="#2C3E50" size="14"><b>Specifications:</b></font>', styles['ProductSpecsTitle'])
        self.specs_para = Paragraph(f'{self.specifications}', styles['ProductNormal'])
        self.hs_code_para = Paragraph(f'<font color="#34495E" size="11"><b>HS Code:</b> {self.hs_code}</font>', styles['ProductNormal'])

    def wrap(self, availWidth, availHeight):
        # Store actual available dimensions from the frame
        self.actual_avail_width = availWidth
        self.actual_avail_height = availHeight

        # Calculate actual dimensions for elements based on available space and ratios
        self.main_image_width = self.actual_avail_width * self._main_image_width_ratio
        self.main_image_height = self.main_image_width * self._main_image_aspect_ratio

        self.text_area_width = self.actual_avail_width * self._text_area_width_ratio

        self.second_image_width = self.actual_avail_width * self._second_image_width_ratio
        self.second_image_height = self.actual_avail_height * self._second_image_height_ratio

        # The flowable reports its desired size as the full available frame
        return availWidth, availHeight

    def draw(self):
        canvas_obj = self.canv

        # Coordinates for positioning within the current frame (0,0 is bottom-left of frame)
        # All positions are relative to the bottom-left of the frame.

        # --- Main Product Image (Left Column) ---
        main_image_padding_top = 0.1 * inch # Reduced padding from top of frame
        main_image_padding_left = 0.05 * self.actual_avail_width # Padding from left of frame, now relative to available width
        
        main_image_x = main_image_padding_left
        main_image_y = self.actual_avail_height - self.main_image_height - main_image_padding_top

        if os.path.exists(self.image_path):
            try:
                product_img = Image(self.image_path, width=self.main_image_width, height=self.main_image_height)
                product_img.drawOn(canvas_obj, main_image_x, main_image_y)
            except Exception as e:
                print(f"Could not load main image {self.image_path}: {e}")
                canvas_obj.setFillColor(colors.HexColor('#F5F5F5'))
                canvas_obj.rect(main_image_x, main_image_y,
                              self.main_image_width, self.main_image_height, fill=1)
                canvas_obj.setStrokeColor(colors.HexColor('#E8E8E8'))
                canvas_obj.setLineWidth(0.5)
                canvas_obj.rect(main_image_x, main_image_y,
                              self.main_image_width, self.main_image_height, fill=0)

        # --- Text Content (Below Main Image on Left) ---
        text_padding_top_from_image = 0.45 * inch # Increased gap below main image
        current_text_y = main_image_y - text_padding_top_from_image
        text_x_offset = main_image_x # Aligned with main image

        # Price
        price_w, price_h = self.price_para.wrapOn(canvas_obj, self.text_area_width, self.actual_avail_height)
        self.price_para.drawOn(canvas_obj, text_x_offset, current_text_y - price_h)
        current_text_y -= (price_h + 0.05 * inch) # Reduced spacing

        # Product Name
        name_w, name_h = self.name_para.wrapOn(canvas_obj, self.text_area_width, self.actual_avail_height)
        self.name_para.drawOn(canvas_obj, text_x_offset, current_text_y - name_h)
        current_text_y -= (name_h + 0.05 * inch) # Further reduced spacing

        # Product Description
        desc_w, desc_h = self.desc_para.wrapOn(canvas_obj, self.text_area_width, self.actual_avail_height)
        self.desc_para.drawOn(canvas_obj, text_x_offset, current_text_y - desc_h)
        current_text_y -= (desc_h + 0.4 * inch) # Increased spacing after description to prevent overlap

        # Specifications Title
        specs_title_w, specs_title_h = self.specs_para_title.wrapOn(canvas_obj, self.text_area_width, self.actual_avail_height)
        self.specs_para_title.drawOn(canvas_obj, text_x_offset, current_text_y - specs_title_h)
        current_text_y -= (specs_title_h + 0.1 * inch)

        # Specifications Text
        specs_w, specs_h = self.specs_para.wrapOn(canvas_obj, self.text_area_width, self.actual_avail_height)
        self.specs_para.drawOn(canvas_obj, text_x_offset, current_text_y - specs_h)
        current_text_y -= (specs_h + 0.1 * inch) # Spacing after specs

        # HS Code
        hs_code_w, hs_code_h = self.hs_code_para.wrapOn(canvas_obj, self.text_area_width, self.actual_avail_height)
        self.hs_code_para.drawOn(canvas_obj, text_x_offset, current_text_y - hs_code_h)

        # --- Second Image (Right Column) ---
        horizontal_gap_between_images = 0.05 * self.actual_avail_width # Gap between the two image columns, now relative to available width
        second_image_x = main_image_x + self.main_image_width + horizontal_gap_between_images
        second_image_y = (self.actual_avail_height - self.second_image_height) / 2 # Vertically centered in frame

        if os.path.exists(self.second_image_path):
            try:
                second_img = Image(self.second_image_path, width=self.second_image_width, height=self.second_image_height)
                second_img.drawOn(canvas_obj, second_image_x, second_image_y)
            except Exception as e:
                print(f"Could not load second image {self.second_image_path}: {e}")
                canvas_obj.setFillColor(colors.HexColor('#F5F5F5'))
                canvas_obj.rect(second_image_x, second_image_y, self.second_image_width, self.second_image_height, fill=1)
                canvas_obj.setStrokeColor(colors.HexColor('#E8E8E8'))
                canvas_obj.setLineWidth(0.5)
                canvas_obj.rect(second_image_x, second_image_y, self.second_image_width, self.second_image_height, fill=0)

def generate_product_catalog(output_filename="product_catalog.pdf"):
    doc = SimpleDocTemplate(output_filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Set document margins to match ProductDetailFlowable's content margins
    doc.leftMargin = 0.7 * inch
    doc.rightMargin = 0.7 * inch
    doc.topMargin = 0.3 * inch
    doc.bottomMargin = 0.7 * inch

    # Define custom styles for a professional look
    styles.add(ParagraphStyle(
        name='ProductPrice',
        parent=styles['h1'],
        alignment=TA_LEFT,
        fontSize=40,
        leading=45,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#E74C3C')  # Strong red for price
    ))
    
    styles.add(ParagraphStyle(
        name='ProductName',
        parent=styles['h2'],
        alignment=TA_LEFT,
        fontSize=32,
        leading=36,
        textColor=colors.HexColor('#2C3E50'),  # Dark blue-gray
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='ProductDescription',
        parent=styles['Normal'],
        alignment=TA_LEFT,
        fontSize=11,
        leading=14,
        fontName='Helvetica',
        textColor=colors.HexColor('#34495E')  # Darker blue-gray
    ))
    
    styles.add(ParagraphStyle(
        name='ProductSpecsTitle',
        parent=styles['h3'],
        alignment=TA_LEFT,
        fontSize=15,
        leading=18,
        textColor=colors.HexColor('#2C3E50'),  # Dark blue-gray
        fontName='Helvetica-Bold'
    ))
    
    styles.add(ParagraphStyle(
        name='ProductNormal',
        parent=styles['Normal'],
        alignment=TA_LEFT,
        fontSize=11,
        leading=14,
        fontName='Helvetica',
        textColor=colors.HexColor('#34495E')  # Darker blue-gray
    ))

    # --- Header and Footer will be applied via the onPage callback ---
    # Need to set up a PageTemplate for SimpleDocTemplate to use the _product_page_layout
    doc.addPageTemplates([
        PageTemplate(id='CoverPage', frames=[
            Frame(doc.leftMargin, doc.bottomMargin,
                  PAGE_WIDTH - doc.leftMargin - doc.rightMargin,
                  PAGE_HEIGHT - doc.topMargin - doc.bottomMargin,
                  id='cover_frame', showBoundary=0)
        ], onPage=_cover_page_layout), # Cover page layout
        PageTemplate(id='AllPages', frames=[
            Frame(doc.leftMargin, doc.bottomMargin,
                  PAGE_WIDTH - doc.leftMargin - doc.rightMargin,
                  PAGE_HEIGHT - doc.topMargin - doc.bottomMargin,
                  id='normal_frame', showBoundary=0)
        ], onPage=_product_page_layout) # Product page layout
    ])

    # Product Data (already updated in previous steps)
    products = [
        ["Chickpeas",
         "Chickpeas, also known as garbanzo beans, are a type of legume native to the Middle East and Mediterranean.",
         "**Variety**: There are different varieties of chickpeas, such as kabuli chickpeas and desi chickpeas. Kabuli chickpeas are larger and have a lighter color, while desi chickpeas are smaller and have a darker color. "
         "**Size**: Chickpeas are typically graded by size, with options such as 7mm, 8mm, 9mm, etc., based on the diameter of the chickpea. "
         "**Color**: Chickpeas can vary in color, with options ranging from light beige to dark brown. "
         "**Moisture Content**: The moisture content of chickpeas is crucial for storage and quality, usually around 10-12%.",
         "0713.20", "1000", "KG", "20FT", "Bags", "25KG", "img1.jpg", "$1200", "img4.jpg"],
        ["Raw Sugar",
         "Raw sugar is an unrefined form of sugar that is commonly exported for various commercial purposes. It is derived from freshly harvested sugarcane or sugar beets and undergoes minimal processing before export",
         "Technical Specifications for Raw Sugar Export: - Type: Icumsa 600-1200 - Polarization: 99.80% minimum - Moisture: 0.08% maximum - Color: Crystal white - Packaging: 50kg bags - Granulation: Medium to fine",
         "17011400", "21", "tons", "20ft", "boxes", "2000.00", "raw.jpeg", "$850", "raw2.jpg"],
        ["Refined Sugar",
         "Refined white sugar is a highly processed sugar type that has been purified to remove impurities and colored components. It is commonly used in food and beverage production for sweetening purposes due to its pure white color and consistent sweetness. This product is packaged in various forms such as granules or cubes for retail and commercial use.",
         "Refined white sugar typically has a purity level of 99.9%, granulation size of 0.35-0.85 mm, moisture content below 0.06%, and a color of 45 ICUMSA (International Commission for Uniform Methods of Sugar Analysis). It is commonly packed in 50 kg bags and exported in large quantities worldwide.",
         "17019990", "28", "tons", "20ft", "crates", "560.00", "refined.jpg", "$900", "refined2.png"]
    ]

    # Add the cover page explicitly first
    doc.pageTemplate = 'CoverPage' # Set the page template for the first page
    story.append(Spacer(1, 0.1 * inch)) # Small spacer to ensure something is added for the frame to render
    
    # Force a page break to the 'AllPages' template for subsequent product pages
    story.append(PageBreak())
    doc.pageTemplate = 'AllPages' # Switch to the product page template for the rest of the document

    # Iterate through products and add ProductDetailFlowable for each
    for i, product in enumerate(products):
        if i > 0:
            story.append(PageBreak()) # Subsequent products use the same 'AllPages' template

        product_flowable = ProductDetailFlowable(product, styles)
        story.append(product_flowable)

    # Build the PDF
    doc.build(story)

if __name__ == "__main__":
    i = 1
    while True:
        output_filename = f"{i}.pdf"
        if not os.path.exists(output_filename):
            break
        i += 1

    generate_product_catalog(output_filename)
    print(f"Product catalog PDF generated successfully as {output_filename}")