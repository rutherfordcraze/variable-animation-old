# Animate along one axis of a variable font

# Width & height of the canvas
w, h = (1000, 500)

# Grey values of background and text
bg = 0
txt = 0.95

# Font size & details
fsize = 200
fontName = ".SFNSDisplay"
axisName = 'wght'
axisMin = 1
axisMax = 1000

# No. of frames
frames = 60

textContent = "Hangeul"


# ------------------------------


for frame in range(frames):
    newPage(w,h)
    frameDuration(0.05)
    fill(bg)
    rect(0,0,w,h)
    fill(txt)

    dx = pi * frame / frames
    delta = pow(sin(dx), 3)
    axisValue = delta * (axisMax - axisMin) + axisMin
    
    font(fontName, fsize)
    
    kwargs = {axisName: axisValue}
    fontVariations(**kwargs)
    text(textContent, (w/2, h/2-fsize/4), align="center")
    

saveImage("export.gif")