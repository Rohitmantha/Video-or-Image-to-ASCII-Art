from PIL import Image,ImageDraw
def imgtoascii(path,count,role):

    img=Image.open(path).convert('RGB')
    width,height=img.size
    print(width,height)
    img=img.resize((int(width/4),int(height/14)))
    pix=img.load()
    width,height=img.size

    chars="$@B%6&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    l=len(chars)
    outputimg=Image.new("RGB",(width*6,height*17))
    d=ImageDraw.Draw(outputimg)

    for i in range(height):
        for j in range(width):
            r,g,b=pix[j,i]
            t=int((r+g+b)/3)
            ind=int((t/255)*l)
            d.text((j*6,i*17),chars[ind-1],(r,g,b))
    if(role==1):
        outputimg.save("./%d_output_ascii.jpg"%count)
    else:
        outputimg.save("./.temp/asciiframes/%d_output.jpg"%count)

