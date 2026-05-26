import re

with open('index.html', 'r') as f:
    content = f.read()

lines = content.split('\n')

script_start = None
script_end = None
for i, line in enumerate(lines):
    if '<script>' in line and 'DOMContentLoaded' not in line and i > 140:
        script_start = i
    if '</script>' in line and i > 200 and script_start is not None and script_end is None:
        script_end = i
        break

print(f"Canvas script: lines {script_start+1} to {script_end+1}")

with open('/tmp/newscript.txt', 'r') as f:
    new_script = f.read()

if script_start is not None and script_end is not None:
    new_lines = lines[:script_start] + new_script.split('\n') + lines[script_end+1:]
    content = '\n'.join(new_lines)
    print("Canvas script replaced successfully")
else:
    print("ERROR: Could not find canvas script boundaries")
    exit(1)

content = content.replace('v.playbackRate=0.75', 'v.playbackRate=0.5')
print("Video speed updated to 0.5x")

old_service_css = '.service-video-section{position:relative;min-height:60vh;display:flex;align-items:center;justify-content:center;overflow:hidden;text-align:center}'
new_service_css = '.service-video-section{position:relative;min-height:50vh;display:flex;align-items:center;justify-content:center;overflow:hidden;text-align:center;margin-bottom:2px}'
content = content.replace(old_service_css, new_service_css)
print("Service section CSS updated for T-shape")

old_bg_video = '.service-bg-video{position:absolute;top:50%;left:50%;min-width:100%;min-height:100%;width:auto;height:auto;transform:translate(-50%,-50%) translateZ(0);z-index:0;object-fit:cover;will-change:transform}'
new_bg_video = '.service-bg-video{position:absolute;top:0;left:0;width:100%;height:100%;transform:translateZ(0);z-index:0;object-fit:cover;will-change:transform;object-position:center center}'
content = content.replace(old_bg_video, new_bg_video)
print("Video alignment CSS updated")

with open('index.html', 'w') as f:
    f.write(content)

print("Done! All changes applied to index.html")
print(f"New file has {len(content.split(chr(10)))} lines")
