import sys
import os

# GNM の Python モジュールのパスを追加
gnm_python_path = os.path.join("C:/GNM-fork/GNM/python")
sys.path.append(gnm_python_path)

from gnm.head import GNMHead

import json
import numpy as np
from pathlib import Path
from gnm.head import GNMHead  # GNM公式Python API

def save_obj(path, vertices, faces):
    with open(path, "w") as f:
        for v in vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for tri in faces:
            f.write(f"f {tri[0]+1} {tri[1]+1} {tri[2]+1}\n")

def main():
    # JSON 読み込み
    with open("frames.json", "r") as f:
        frames = json.load(f)

    # GNMヘッドモデル読み込み
    gnm = GNMHead.from_pretrained("gnm_head")  # 公式モデル

    # 出力フォルダ
    out_dir = Path("output_obj")
    out_dir.mkdir(exist_ok=True)

    # triangulation（GNMヘッドの顔ポリゴン）
    faces = gnm.topology.faces

    # 各フレームを OBJ に変換
    for i, frame in enumerate(frames):
        identity = np.array(frame["identity"], dtype=np.float32)
        expression = np.array(frame["expression"], dtype=np.float32)
        rotations = np.array(frame["rotations"], dtype=np.float32)
        translation = np.array(frame["translation"], dtype=np.float32)
        correctives = np.array(frame["correctives"], dtype=np.float32)

        # GNMヘッドで 3D 頂点を生成
        vertices = gnm.forward(
            identity=identity,
            expression=expression,
            rotation=rotations,
            translation=translation,
            correctives=correctives
        ).vertices

        # OBJ 保存
        save_obj(out_dir / f"frame_{i:04d}.obj", vertices, faces)

    print("OBJ 出力完了！")

if __name__ == "__main__":
    main()
