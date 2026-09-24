# GNM Webcam Puppet Enhanced

## Key Features 

- GNM Head OBJ Export Support 
- MP4 Video Input Support 
- Recording Support 
- JSON Export Support 
- One OBJ Per Second Export Pipeline

Enhanced fork of the original GNM Webcam Puppet.

This fork adds a complete workflow for reconstructing and exporting GNM Head meshes from tracked facial motion.

---

## Major Feature: GNM Head OBJ Export Support

This fork can reconstruct GNM Head meshes directly from tracked animation data and export them as OBJ files.

Workflow:

MP4 Video
↓
Face Tracking
↓
Drive Head
↓
Fit Identity
↓
Save JSON
↓
GNM Head Reconstruction
↓
OBJ Export

The exported meshes are reconstructed using:

- gnm_head.bin
- gnm_head.json
- identity coefficients
- expression coefficients
- corrective coefficients

This feature is not available in the original project.

## Installation

Clone this repository:

```bash
git clone https://github.com/shimazakyo-sys/gnm-webcam-puppet.git
cd GNM-fork/web_puppet
```

Install dependencies:

```bash
npm install
```

Synchronize assets:

```bash
npm run sync-assets
```

Start the development server:

```bash
npm run dev
```

Open:

```text
http://localhost:5173/
```

in your browser.

---

## Quick Start 

1. Place an MP4 file into: 

```text 
web_puppet/public/video/ 
```

2. Start the application. 

3. Open: 

```text
http://localhost:5173/ 
```

4. Click **Drive Head**. 

5. Click **Fit Identity**. 

6. Click **Save JSON**. 

7. Generate OBJ files: 

```bash 
python generate_obj.py
```

Generated OBJ files will be written to:

obj/

Example OBJ outputs are available in:
 
samples/
``

---

## Repository Structure

```text
obj/
Generated OBJ files

samples/
Example OBJ outputs

web_puppet/public/video/
Place MP4 files here
```

## Additional Features

### MP4 Video Input

The original project requires a webcam.

This fork can use MP4 files as the tracking source.

Workflow:

MP4 Video
↓
Face Tracking
↓
GNM Head Animation

No webcam is required.

Place your MP4 files in:
 
web_puppet/public/video/
 
The latest MP4 file will be loaded automatically.

---

### Recording Support

The rendered GNM Head output can be recorded and saved.

Useful for:

- Animation previews
- Motion review
- Dataset generation

---

### JSON Export

Tracked GNM parameters can be exported to JSON.

Exported data includes:

- identity
- expression
- rotations
- translation
- correctives

The JSON files can later be used to reconstruct meshes.

---

## OBJ Export Pipeline

1. Load an MP4 video.
2. Run Drive Head.
3. Run Fit Identity.
4. Save tracking data to JSON.
5. Convert JSON data into GNM Head meshes.
6. Export OBJ files.

One OBJ is generated per second of source video.

Output:

```text
obj/
├─ frame_000.obj
├─ frame_001.obj
├─ frame_002.obj
└─ ...