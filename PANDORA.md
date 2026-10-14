import os
import shutil
from google.colab import drive

# 1. 自分のGoogleドライブをColabにマウントする
drive.mount('/content/drive')

# 2. 整理したいフォルダのパスを指定する
target_dir = '/content/drive/My Drive/ダウンロード'

# フォルダがない場合は作成する
if not os.path.exists(target_dir):
  os.makedirs(target_dir)
  print(f'「{target_dir}」が見つからなかったので作成しました。')
  print(
      'このフォルダの中に画像をいくつか入れてから、もう一度実行してみてください！'
  )
else:
  files = os.listdir(target_dir)
  print(f'対象フォルダ内のファイル数: {len(files)}件\n')

  for filename in files:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
      sub_dir = os.path.join(target_dir, '画像フォルダ')
    elif filename.lower().endswith(('.pdf', '.txt', '.docx')):
      sub_dir = os.path.join(target_dir, 'ドキュメントフォルダ')
    else:
      sub_dir = os.path.join(target_dir, 'その他フォルダ')

    if not os.path.exists(sub_dir):
      os.makedirs(sub_dir)

    src_path = os.path.join(target_dir, filename)
    dest_path = os.path.join(sub_dir, filename)

    if os.path.isfile(src_path):
      shutil.move(src_path, dest_path)
      print(f'【移動】 {filename} -> {sub_dir} へ')

  print('ファイルの整理が完了しました！')

import os
import shutil
from google.colab import drive

import qrcode

# QRコードにしたい文字やURL
url = "https://www.google.com"

# QRコードの作成と保存
img = qrcode.make(url)
img.save("my_qr.png")
print("QRコードを作りました！")

# 簡易電卓アプリ
print("足し算をします")
a = int(input("数字を1つ入れてね: "))
b = int(input("もう1つの数字を入れてね: "))
print(f"結果は {a + b} です！")


