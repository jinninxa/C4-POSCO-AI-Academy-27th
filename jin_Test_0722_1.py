#!/usr/bin/env python
# coding: utf-8

# # [Github] 우분투 깃허브 연동
# 
# ###### 참조: https://kangmyoungseok.github.io/etc/Github-Setting/
# ###### 
# 
# 
# ### 0. Access Token 생성
# 
# ### 1. GitHub Repository 다운로드
# mkdir github  
# cd github  
# git clone https://github.com/jinninxa/C4-POSCO-AI-Academy-27th.git
# 
# 
# ### 2. (1.)에서 만든 Repository로 디렉토리 이동
# cd github/C4-POSCO-AI-Academy-27th  
# git status
# 
# 
# ### 3. GitHub와 로컬 서버 연결
# git config --global user.name [이름]  
# git config --global user.email [이메일]  
# 
# git config --global --list  
# + 위의 명령이 잘 입력되었는지 확인
# 
# 
# ### 4. GitHub 서버로 업로드
# git pull
# + 팀원들이 GitHub에 최신화한 내용 반영
# + push 전 반드시 실행 !!!!
# 
# git status
# 
# git add [파일이름]  
# git commit -m "파일 업로드"  
# git push  
# + Username: 깃허브 아이디
# + Password: Access Token
