# robosys2019_assignment

長坂 拓海

2020年1月24日
学籍番号 17C1108

---

## プログラムの内容

* ROSとOpenCVを利用したエッジ検出，及び円検出アプリです．
* 必須パッケージはrospy，cv_bridge，cv_cameraです．web_video_serverの使用を推奨します．
* 動作確認はUbuntu 18.04，ROS_melodic上で行いました．
---

## 使い方

* /cv_camera/image_rawからImage型のメッセージをサブスクライブし，/img_cannyにキャニー法を用いてエッジ検出した結果，/img_circleにハフ変換を用いて円検出を行った結果をパブリッシュします．
* 実行結果の確認はweb_video_server等で行うことが出来ます．
---

## 動画
https://youtu.be/x1tVxp-x8Bg

---

## 参考文献

* RaspberryPiで学ぶROSロボット入門【日経BP社】
 * https://github.com/ryuichiueda/pimouse_vision_control （MITライセンス）
 * 10章の顔検出プログラムを参考に，OpenCVによる処理をエッジ検出と円検出に変更しました．
 * また，グレースケール画像，カラー画像を同様の関数でパブリッシュ出来るようにしました．
 
---
