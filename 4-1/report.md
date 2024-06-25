# Exp4-1 MD5散列值碰撞

## 实验步骤

1. 从书中的网址下载可执行文件 `fastcoll_v1.0.0.5.exe` 

2. 运行指令 `fastcoll_v1.0.0.5.exe -p fastcoll_v1.0.0.5.exe -o m1.exe m2.exe` ，得到两个输出文件 `m1.exe` 和 `m2.exe`

3. 运行指令 `certutil -hashfile m1.exe MD5` 和 `certutil -hashfile m2.exe MD5` 得到如下两个输出：

   ```
   MD5 的 m1.exe 哈希:
   7c92d2a5cb429f820e8fde3e708ffe96
   CertUtil: -hashfile 命令成功完成。
   
   MD5 的 m2.exe 哈希:
   7c92d2a5cb429f820e8fde3e708ffe96
   CertUtil: -hashfile 命令成功完成。
   ```

   可以发现两个文件的MD5值是相同的。

4. 运行指令 `certutil -hashfile m1.exe SHA1` 和 `certutil -hashfile m2.exe SHA1` ，可以得到如下两个输出：

   ```
   SHA1 的 m1.exe 哈希:
   6b7ba10cc4553411a5af753239535683d2f30284
   CertUtil: -hashfile 命令成功完成。
   
   SHA1 的 m2.exe 哈希:
   f2bfb758482fd9b646123be4b32ac7b29cf58343
   CertUtil: -hashfile 命令成功完成。
   ```

   可以发现这两个文件的SHA1值还是不同的。

## 实验现象

![image-20240625220915917](/Users/fangkechen/GitHub/CyberSecurityExp/4-1/assets/image-20240625220915917.png)