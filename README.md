# 스즈메 Discord Bot

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.12.0-3776AB?style=flat&logo=python&logoColor=yellow">
  </a>
  <a href="https://github.com/Rapptz/discord.py/">
     <img src="https://img.shields.io/badge/discord-py-blue.svg" alt="discord.py">
  </a>
  <a href="https://github.com/STROAD/school-bot/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/STROAD/school-bot" alt="license: MIT">
  </a>
</p>

스즈메 Discord Bot은 [Python](https://www.python.org) 3.12.0에서 [discord.py](https://github.com/Rapptz/discord.py) 라이브러리를 사용하여 만들어진 디스코드 봇 입니다.
(버전 : v0.1)

LoL 전적검색, 유튜브 음악 재생 등이 가능합니다.

## 주요기능

- LoL 전적검색
  ![lol](https://github.com/ehdgnsl01/Discord-Chat-Bot/assets/70877444/1e540af8-7c2b-4cbe-9f92-ce098a1f50de)
- 유튜브 음악 재생
  ![music](https://github.com/ehdgnsl01/Discord-Chat-Bot/assets/70877444/15a3ed31-1df5-426b-b1f0-0937a013374f)

## 설치

1. [Python](https://www.python.org)(3.12.0) 설치

2. Repository clone  
   이 레포지트리를 clone합니다.  
   `$ git colne https://github.com/ehdgnsl01/Discord-Chat-Bot.git`

3. 봇 구동에 필요한 라이브러리 설치

   ```
   pip install discord.py
   pip install requests
   pip install yt_dlp
   pip install PyNaCl
   pip install discord.py[voice]
   pip install python-dotenv
   pip install youtube_dl
   ```

4. 파일 수정

   1. data.py 파일에 자신의 봇 토큰, 인증키 등을 입력하여 주세요.
   2. data.py는 Cogs폴더 안에도 있습니다. 똑같이 입력해주세요.

5. 봇 실행  
   main.py 파일을 실행해주세요.

## 라이선스

이 프로젝트는 MIT License를 사용합니다.  
자세한 내용은 [LICENSE.md](LICENSE) 파일을 참고해 주세요.

오픈소스는 [Copying.md](Copying) 파일을 참고해주세요.
