#!/bin/bash

echo "正在安装环境..."
install(){
    echo $(pip3 install -r pip-install)
}
install
echo "安装成功✅"

