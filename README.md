# Dual-stream memory

Static homepage for the ICRA 2027 paper *Dual-Stream Memory for Vision-Language-Action Policies*. Authors stay anonymous while the paper is under double-anonymous review. Visual tokens follow fireworks-tech-graph Claude Official.

The GitHub Pages URL will be [https://jackdov9.github.io/dual-stream-memory/](https://jackdov9.github.io/dual-stream-memory/).

## Open locally

Open `index.html` in a browser. Relative asset paths work from a `file://` URL and from a local server.

To serve the directory:

```bash
python3 -m http.server 8080
```

Then open [http://127.0.0.1:8080/](http://127.0.0.1:8080/).

## Edit the page

Change copy and tables in `index.html`. Change layout and color tokens in `style.css`. Replace raster figures in `assets/`.

Result bars are regenerated with:

```bash
python3 scripts/homepage_bars.py
```

Piper clips use sixteen paths, four tasks times four methods:

|  | π₀.₅ | NativeMEM | FrameSamp+Modul | Ours |
|--|--|--|--|--|
| Pick×3 | `assets/videos/pickx3_pi05.mp4` | `pickx3_nativemem.mp4` | `pickx3_framesamp.mp4` | `pickx3_ours.mp4` |
| Swing×2 | `swingx2_pi05.mp4` | `swingx2_nativemem.mp4` | `swingx2_framesamp.mp4` | `swingx2_ours.mp4` |
| RePick | `repick_pi05.mp4` | `repick_nativemem.mp4` | `repick_framesamp.mp4` | `repick_ours.mp4` |
| Shell | `shell_pi05.mp4` | `shell_nativemem.mp4` | `shell_framesamp.mp4` | `shell_ours.mp4` |
