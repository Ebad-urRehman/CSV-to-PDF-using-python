from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
# p is portraiat format

# till now pdf is an object in python

# adding page to pdf object
pdf.add_page()
# setting font and formatting
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Aslam u Alaikum!", align="L",
         ln=1, border=1)

# now a blank page pdf is been formed by below statement
pdf.output("output.pdf")


"""\
               .cell arguments 
w for width tells that how much is cell width set to 0 means full page 10 means 10
h for height of cell height set to 0 results in a line over the text
txt is the text in the cell
ln behave as breakline after previous cell when set to 1 when set to 0 it added the new cell after the previous cell width ends 
border when set to 0 cell border not appear, it appears when border =1 
           .set_font arguments
family is font style
style can be bold italic B or I
size is size of text in cells added after that line
"""