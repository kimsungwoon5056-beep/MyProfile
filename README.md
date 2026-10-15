# 김성운의 포트폴리오

전북대학교 컴퓨터인공지능학부 학생 김성운의 학습과 프로젝트를 소개하는 Hugo 사이트입니다.

- 공개 사이트: https://kimsungwoon5056-beep.github.io/MyProfile/
- 저장소: https://github.com/kimsungwoon5056-beep/MyProfile
- 소개: https://kimsungwoon5056-beep.github.io/MyProfile/about/
- 프로젝트: https://kimsungwoon5056-beep.github.io/MyProfile/projects/
- 학습 기록: https://kimsungwoon5056-beep.github.io/MyProfile/posts/

## 도구와 설치

사이트의 빌드에는 **Hugo Extended 0.167.0**을 사용합니다. 일반 Hugo 대신 Extended 배포본을 설치합니다. Git은 소스 다운로드와 커밋·push에 사용하며, 로컬 사이트 확인에는 Python이나 Node.js가 필요하지 않습니다.

1. [Git 공식 사이트](https://git-scm.com/downloads)에서 운영체제에 맞는 Git을 설치합니다.
2. [Hugo 0.167.0 공식 릴리스](https://github.com/gohugoio/hugo/releases/tag/v0.167.0)에서 운영체제와 CPU에 맞는 Extended 압축 파일을 받아 압축을 풉니다. Windows x64 파일명은 `hugo_extended_0.167.0_windows-amd64.zip`입니다.
3. `hugo.exe`가 있는 폴더를 PATH에 추가하고 새 터미널에서 `hugo version`을 실행합니다. 출력에 `v0.167.0`과 `extended`가 있는지 확인합니다.

Git Bash 등 터미널에서 다음 순서로 사이트를 받습니다. 테마는 `site/themes/template`에 포함되어 있어 테마 submodule을 추가할 필요가 없습니다.

```bash
git clone https://github.com/kimsungwoon5056-beep/MyProfile.git
cd MyProfile/site
hugo version
hugo --gc --minify --config hugo.toml,pages.json --destination ../public --enableGitInfo=false
```

생성된 `public/index.html`은 정적 결과물입니다. 운영 주소 아래의 자산 경로를 사용하므로 로컬 파일을 더블클릭하는 방법 대신 아래 개발 서버를 사용합니다.

## 로컬 미리보기

`MyProfile/site` 폴더에서 실행합니다.

```bash
hugo server --config hugo.toml,pages.json --baseURL http://localhost:1313/MyProfile/ --appendPort=false --enableGitInfo=false
```

브라우저에서 http://localhost:1313/MyProfile/ 을 엽니다. 종료는 Ctrl+C입니다. localhost 주소는 로컬 확인용이며 공개 배포의 baseURL은 `site/pages.json`에 지정된 HTTPS 주소입니다.

## 자동 배포 환경

`.github/workflows/hugo-pages.yml`은 main push를 받아 사이트를 빌드하고 GitHub Pages에 배포합니다. 현재 지정값은 Python 3.12, Node.js 24, Go 1.27.1, Hugo Extended 0.167.0, Dart Sass 1.105.0입니다. 의존성 준비와 경로 보정은 `.github/pages_build.py`가 수행합니다. 준비 스크립트 버전은 3.1입니다.

새 ZIP으로 처음 준비할 때는 Python 3.9 이상에서 제공된 `prepare_github_pages.py`를 사용했습니다. 이 저장소를 clone한 뒤에는 준비 스크립트를 다시 실행할 필요가 없습니다.
