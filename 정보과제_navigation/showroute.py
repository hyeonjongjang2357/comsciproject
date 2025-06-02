#%%
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#list로 경로 반환
route=[]
navigation=Image.open('sshsmap.jpg')
route_test=Image.open('route_test2.jpg')
navigation_np=np.array(navigation)
route_test=np.array(route_test)
plt.axis('off')
plt.imshow(navigation)
plt.imshow(route_test)
plt.show()

# %%
