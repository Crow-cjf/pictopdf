from fpdf import FPDF
from PIL import Image
import os

path = input("请输入文件路径：\n")
if not path:
    path = os.getcwd()
PDF = FPDF(unit="mm",format="A4")
PDF.set_auto_page_break(0)
name = path.split("\\")[-1]
images = os.listdir(path)
images.sort()
w_li = 190
h_li = 277
dpi = 300
for image in images:
    if ".jpg" in image or ".png" in image:
        PDF.add_page()
        img = Image.open(path+"\\"+image)
        width = img.width * 25.4 / dpi
        height = img.height * 25.4 / dpi
        mul = round(min(w_li / width,h_li / height),2)
        PDF.image(os.path.join(path,image),w=width*mul,h=height*mul)
        PDF.set_y(-10)
        PDF.set_font('Arial', 'I')
        PDF.cell(0, 10, 'Page ' + str(PDF.page_no()), 0, 0, 'C')
PDF.output(os.path.join(path,name+".pdf"),"F")
print('转换完成！')
