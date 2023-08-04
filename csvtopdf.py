from fpdf import FPDF
import streamlit as st
import pandas as pd

# reading csv file
dataframe = pd.read_csv("003 topics.csv")

# setting pdf setting and creating pdf object in pdf variable
pdf = FPDF(orientation="P", unit="mm", format="A4")

# page not break automatically
pdf.set_auto_page_break(auto=False)

# Generating first page only with heading
for index, row in dataframe.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 254) # red, green blue for at 254 respectively
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1, border=0)

    # generating lines
    pdf.line(10, 21, 200, 21)
    # first line distance from upper border to line
    dist = 21

    # generating lines
    for i in range(26):
        dist = dist + 10
        pdf.line(10, dist, 200, dist)

    # adding footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=15)
    pdf.set_text_color(100, 100, 100)#gray
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

    # row pages tell how much pages a single topic has
    # so it creates mulitple pages for single topic

    # generating other pages under a single heading page
    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=15)
        pdf.set_text_color(100, 100, 100)  # gray
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

        # first line distance from page upper border
        dist = 11
        # generating lines
        for i in range(26):
            dist = dist + 10
            pdf.line(10, dist, 200, dist)

# creating the file
pdf.output("output.pdf")


"""for x in range(3): # print 0, 1, 2
    print(x)

my_range = range(3)
to create a range with items 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, and 21, you would do the following:
range(10, 22)
he numbers in all the above ranges increase by 1. In other words, the step of those ranges is 1, but you can change the step by adding a third argument to the range class as follows:
range(10, 22, 3)
That range would produce a range with items 10, 13, 16, and 19, so at a step of three. 
print(my_range)# prints range(0,3)
print(list(my_range)) # print [0, 1 ,2]
A4 total height is 298 mm

*****better method to generate full page lines
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)
            
            20 is distance of first line to page top 
            298 is total page size ie linees are extended up to 298
            10mm is the distance bw each line"""