# Final v2 render — 2026-11-08

User approved the current preview with ‘이대로 렌더해줘 brew install ffmpeg’.
Output: hurdling-club-final.mp4, H.264,1920×1080,30fps,600frames,20.000000seconds,6,012,567bytes. No audio stream.
Source: source/index.html with five DOM subcompositions. Original v1 remains in versions/v1 and video.mp4.

Rendered using installed HyperFrames0.9.21, quality delivery,1worker,strict,experimental-fast-capture=false. Native screenshot capture selected for HTML iframes. Internal headless render engine with hardware GPU;41.4seconds. Browser preview preference remains Aside; no interactive Chrome navigation used.
FFmpeg command was requested via Homebrew, but brew is not installed (command not found). Existing /tmp/hurdling-video-tools/node_modules/@ffmpeg-installer/darwin-arm64/ffmpeg and @ffprobe-installer/darwin-arm64/ffprobe were added to this command’s PATH. No Homebrew installation was claimed.

Verification: lint-v2.json zero errors/warnings; final-ffprobe.json exact duration/size/stream metadata; complete FFmpeg decode exited0. final-sheet.png samples actual encoded frames at1,3,5.5,6.5,6.833,7.5,10,13.667,16,19.967seconds. Visually inspected all10frames: fonts/screens/frame present,50→100% gauge and one confetti burst, aligned asset cards, final logo/mascot. No full automated layout audit claimed.
