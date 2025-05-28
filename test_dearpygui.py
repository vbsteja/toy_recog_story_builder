import dearpygui.dearpygui as dpg
import array
# import av
import cv2

dpg.create_context()
ctr = 0
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Read a frame from the webcam
ret, frame = cap.read()
width, height = frame.shape[1], frame.shape[0]
if not ret:
    print("Failed to read from webcam")
    exit()
# Convert the frame to RGB format
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# Create a raw texture from the RGB frame and reshape it to RGB array
frame_rgb = array.array('f', frame_rgb.flatten() / 255.0)
raw_data = frame_rgb

with dpg.texture_registry():
    dpg.add_raw_texture(width=width, height=height, default_value=raw_data, format=dpg.mvFormat_Float_rgb, tag="texture_tag") # type: ignore


def update_dynamic_texture(frame):
    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Create a raw texture from the RGB frame
    frame_rgb =array.array('f', frame_rgb.flatten() / 255.0)
    dpg.set_value("texture_tag", frame_rgb)  # Update the texture with new data
    for i in range(0,height*width*3):
        raw_data[i] = frame_rgb[i]
    # dpg.set_frame_callback( update_dynamic_texture)  # Schedule for next frame

with dpg.window(label="Tutorial"):
    dpg.add_image("texture_tag")
    # dpg.set_frame_callback(ctr, update_dynamic_texture)  # Initial call to update the texture
    #callback
    # dpg.set_frame_callback(update_dynamic_texture)  # Update the texture every frame


dpg.create_viewport(title='Custom Title', width=width, height=height)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read from webcam")
        break
    # Update the texture with the new frame
    update_dynamic_texture(frame)
    
    dpg.render_dearpygui_frame()
    # Uncomment the next line to limit the frame rate to ~30 FPS
    # dpg.set_frame_callback(dpg.get_frame_count() + 1, update_dynamic_texture)  # ~30 FPS
# dpg.set_frame_callback(dpg.get_frame_count(), update_dynamic_texture)  # ~30 FPS
# dpg.start_dearpygui()
cap.release()
dpg.destroy_context()