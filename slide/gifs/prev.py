import os
import glob
import imageio

source_folder = "slide/gifs/out"
destination_folder = "slide/gifs/prev"

os.makedirs(destination_folder, exist_ok=True)

gif_files = glob.glob(os.path.join(source_folder, '*.gif'))

for gif_file in gif_files:
   file_name = os.path.splitext(os.path.basename(gif_file))[0]
   
   gif = imageio.get_reader(gif_file)
   first_frame = gif.get_data(0)
   
   destination_path = os.path.join(destination_folder, f'{file_name}.png')
   
   imageio.imwrite(destination_path, first_frame)
   
   gif.close()