# Base Images
## 从天池基础镜像构建
From registry.cn-shanghai.aliyuncs.com/tcc-public/pytorch:latest-py3

## 把当前文件夹里的文件构建到镜像的根目录下
ADD . /
WORKDIR /

## 指定默认工作目录为根目录（需要把run.sh和生成的结果文件都放在该文件夹下，提交后才能运行）

## 使用pip安装包
RUN pip install requests
RUN pip install tqdm
RUN pip install demjson
RUN pip install pandas

## 设定权限并运行run.sh
RUN sudo chmod 777 /
CMD ["/bin/bash", "run.sh"]