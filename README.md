# Saku-mahjong
A reinforcement learning Japanese mahjong AI. Saku is "咲く" in Japanese, it origins from comic "咲-Saki".

# Data
Data comes from:[haifu](http://totutohoku.b23.coreserver.jp/hp/HAIHU.htm)

Data is in following format:
```
    30符 一飜ツモ 門前清模和 
    [1東]2m5m6m6m9m9m2p4p1s5s7s8s西
    [2南]1m2m8m2p2p4p8p1s1s9s東南南
    [3西]1m5m6m8m9m1p7p2s3s3s6s6s西
    [4北]1m3m4m5m2p3p3p5p7p5s北北白
    [表ドラ]南 [裏ドラ]2p
    * 1G発 1d1s 2N 2d8p 3G北 3d1p 4G4p 4d白 1G発 1d西 2G7p 2d9s 3G3s 3d2s 4G3m
    * 4d5s 1G7m 1d5s 2G6p 2d東 3G2s 3D2s 4G中 4D中 1G2s 1D2s 2G5s 2d8m 3G8m
    * 3d西 4G4m 4d1m 1G西 1D西 2G7s 2d7p 3G1s 3D1s 4G9s 4D9s 1G4m 1d4p 2G9p
    * 2D9p 3G6p 3d北 4N 4d7p 1G4s 1d2p 2G2m 2d2m 3G9s 3D9s 4G1p 4d4m 1G4m 1d4s
    * 2G4p 2d2m 3G7m 3d1m 4G西 4D西 1G6p 1D6p 2G1p 2d1m 3G7m 3d8m 4G中 4D中
    * 1G6m 1d7s 2G2m 2D2m 3G7p 3d7p 4G東 4D東 1G3s 1D3s 2G5p 2d1p 3G7s 3D7s
    * 4G中 4D中 1G南 1d8s 2G9m 2D9m 1N 1d7m 2G発 2d7s 3G7m 3d7m 4G8s 4D8s 1G中
    * 1D中 2G3m 2d5s 3G8s 3D8s 4G9p 4D9p 1G6p 1D6p 2G9s 2D9s 3G5p 3A
```
We can know that

| Character | Meaning in Mahjong |
| :-------: | :----------------: |
|     G     |        ツモ        |
|     d     |       手出し       |
|     D     |      ツモ切り      |
|     N     |        ポン        |
|     C     |        チー        |
|     K     |        カン        |
|     R     |       リーチ       |
|     A     |       上がる       |


