import numpy as np
from PIL import Image
import seam_carving

src = np.array(Image.open('iguana.png'))
src_h, src_w, _ = src.shape
dst = seam_carving.resize(
    src, (src_w - 200, src_h),
    energy_mode='backward',   # Choose from {backward, forward}
    order='width-first',  # Choose from {width-first, height-first}
    keep_mask=None
)
Image.fromarray(dst).show()