import cv2
img=cv2.imread("Virat.jpg")
org_height,org_width=img.shape[:2]
clone=img.copy()
zoom_out=clone.copy()
zoom=1.0
cv2.namedWindow("Virat Kohli")
def mouse_event(event, x, y, flags, param):
    global zoom,clone,zoom_out
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags>0: zoom=zoom*1.2
        else: zoom=zoom/1.2

    zoom=max(1.0,min(zoom,10.0))

    win_width=int(org_width/zoom)
    win_height=int(org_height/zoom)

    x1=max(0,min(x-(win_width//2),org_width-win_width))
    y1=max(0,min(y-(win_height//2),org_height-win_height))
    x2=x1+win_width
    y2=y1+win_height

    org=clone[y1:y2,x1:x2]
    if org.size>0:
        zoom_out = cv2.resize(org, (org_width, org_height), interpolation=cv2.INTER_LINEAR)
    #cv2.imshow("Spidey",zoom_out)

cv2.setMouseCallback("Virat Kohli",mouse_event,"Virat Kohli")
while True:
    cv2.imshow("Virat Kohli",zoom_out)
    key=cv2.waitKey(1)
    if key==ord('q'):break
cv2.destroyAllWindows()