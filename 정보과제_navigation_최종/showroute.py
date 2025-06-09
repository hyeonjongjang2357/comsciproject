from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#list로 경로 반환
route=['우암관_2층','예지관_2층']
navigation=Image.open('sshsmap.jpg')
navigation_np=np.array(navigation)
plt.imshow(navigation)
for i in range(len(route)-1):
    plt.imshow(np.array(Image.open(f'{route[i]}_{route[i+1]}.png')))
plt.axis('off')
plt.show()