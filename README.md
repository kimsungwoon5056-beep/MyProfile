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

## 수정과 재배포

| 수정 대상 | 파일 |
|---|---|
| 이름·언어·메뉴·GitHub 링크 | `site/hugo.toml` |
| 운영 주소와 빌드 설정 | `site/pages.json` |
| 자기소개·관심 분야·학습 계획 | `site/content/about.md` |
| 캡스톤 소개와 본인 역할 | `site/content/projects.md` |
| 학습 글과 목록 | `site/content/posts/` |
| 이미지 등 정적 파일 | `site/static/` |
| 사이트 고유 스타일 | `site/assets/css/portfolio.css` |
| 메뉴·테마 버튼 등 템플릿 덮어쓰기 | `site/layouts/_partials/` |

`exampleSite`와 저장소 루트의 테마 파일은 원본 참고용입니다. 실제 배포 대상인 `site`를 수정합니다. 테마의 예시 글·예시 인물·예시 이미지는 `site`에서 삭제했으며 원본은 `exampleSite`에서 확인할 수 있습니다. `public`은 생성 결과이므로 직접 수정하지 않습니다.

수정 후 로컬에서 확인한 다음 저장소 루트에서 변경한 파일만 기록합니다. 예를 들어 소개 파일 수정은 다음과 같습니다.

```bash
git --no-pager diff -- site/content/about.md
git add site/content/about.md
git commit -m "소개 페이지의 실제 학습 경험 보완"
git push origin main
```

1. GitHub 저장소 Settings → Pages → Source를 GitHub Actions로 설정합니다.
2. [Actions](https://github.com/kimsungwoon5056-beep/MyProfile/actions)에서 push한 커밋의 build와 deploy 성공을 확인합니다.
3. 공개 사이트에서 변경한 페이지를 새로고침하고 실제 내용과 링크를 확인합니다.
4. 실패했다면 실패 단계의 로그를 확인하고 원인을 수정한 뒤 다시 커밋·push합니다.

제출할 때는 `git rev-parse HEAD`의 전체 SHA, 해당 커밋 URL과 Actions 실행 URL을 기록합니다. 보고서 작성 후 사이트를 수정했다면 보고서의 버전 정보와 캡처도 함께 갱신합니다.

## 출처와 이용 조건

| 자료 | 출처 | 사용과 고지 |
|---|---|---|
| Hugo Coder 테마 | https://github.com/luizdepra/hugo-coder | MIT. 루트 `LICENSE.md`와 테마 내부 고지를 유지합니다. |
| 테마 기본 아바타·아이콘·글꼴 | `site/themes/template` 및 `site/static/images/avatar.jpg` | 외부 테마에 포함된 자료입니다. 아바타는 본인 얼굴 사진이 아닌 장식용 실루엣입니다. 아이콘·글꼴의 라이선스는 테마의 `LICENSE.md`, `static/fonts/LICENSE.txt`, `assets/scss/font-awesome/LICENSE.txt`를 확인합니다. |
| SimCheong 설명과 코드 링크 | https://github.com/yoosunu/SimCheong | 이전 팀 자료의 출처 링크입니다. 해당 코드를 이 저장소에 복제하거나 개인 구현 성과로 표시하지 않습니다. 재사용 시 원저작자의 이용 조건을 별도로 확인합니다. |
| 소개·학습 목표·프로젝트 설명 | 본인 제공 정보 및 Codex의 문안 정리 지원 | AI 도움을 받아 작성했습니다. 담당 예정·향후 계획과 실제 완료 작업을 구분합니다. |
| 한국어 설정·메뉴·접근성 개선 코드와 문서 | 본인 과제 작업 및 Codex 지원 | AI가 설정·코드·문서 작성과 검증을 지원했습니다. 세부 사례와 본인의 판단·직접 확인 결과는 LMS 제출 보고서에 기록합니다. |

포트폴리오 본문·개인 자료 전체에 원본 테마의 MIT 라이선스가 자동으로 적용된다고 주장하지 않습니다. 외부 자료의 고지를 유지하고, 자료별 이용 조건을 확인합니다.

## 검증 기록

검사 절차와 실제 결과는 `verification/`에 기록합니다. 이는 AI가 도구로 검사한 기록이며 본인의 직접 검사와 구분합니다. PDF 보고서에는 본인이 직접 확인한 범위와 실제 결과를 별도로 적습니다.

### 생성 결과 경로 검사

위 빌드를 마친 뒤 저장소 루트에서 Python 3.9 이상으로 실행합니다. Windows Git Bash에서는 `python` 대신 `py`를 사용할 수 있습니다.

```bash
python verification/check_site.py public --base-url https://kimsungwoon5056-beep.github.io/MyProfile/
```

검사는 HTML과 CSS가 참조한 내부 파일, 앵커, 문서 언어와 이미지 alt 속성을 확인합니다. `issues`가 빈 목록이면 해당 정적 검사에서 문제가 발견되지 않은 것입니다. 외부 링크 응답, JavaScript 실행, 화면 배치와 확대, 색상 대비는 브라우저에서 별도로 확인해야 합니다. 검사 실패 시 종료 코드가 1이므로 출력된 경로를 수정한 뒤 같은 명령으로 재검사합니다.

### 배포 전 자동 검사

main을 push하면 Hugo 빌드와 프로젝트 경로 보정 다음에 검사 도구의 회귀 검사 6건과 실제 생성 결과 검사가 실행됩니다. 둘 중 하나라도 실패하면 산출물 업로드와 배포 단계로 진행하지 않습니다. 검사 결과는 Actions의 `Test site checker`와 `Check generated site before publication` 로그에 표시됩니다. 이 검사는 화면 배치·화면 모드·브라우저 조작의 직접 검사를 대신하지 않습니다.

검사 도구만 확인하려면 저장소 루트에서 실행합니다.

```bash
python -m unittest discover -s verification -p 'test_*.py' -v
```

정상 하위 경로·한글 앵커·CSS 참조는 허용하고, 없는 파일·없는 앵커·배포 경로 밖 주소·개인 PC 주소·HTTP 주소·빈 링크·잘못된 언어·누락된 alt가 발견되는지 확인합니다. 임시 폴더의 검사 전용 예시를 사용하므로 실제 사이트 파일을 바꾸지 않습니다.


### 유효 커밋 집계의 재현

저장소 루트에서 최종 제출할 SHA 또는 `HEAD`를 지정합니다. 결과 파일은 저장소 밖의 원하는 위치에 저장할 수 있습니다.

```bash
python verification/audit_commits.py --ref HEAD --output ../MyProfile-commit-audit.json
```

결과의 `final_sha`가 실제 집계 끝점입니다. 전체 수에서 초기 ZIP 등록과 빈 변경·자체 변경이 없는 병합·생성 결과만의 변경을 보수적으로 제외하고 나머지는 `candidate`로 표시합니다. 후보를 최종 인정 개수로 자동 확정하지 않습니다. 각 커밋의 diff와 과제 기준을 직접 대조해야 합니다. 검증 기록의 스냅샷은 기록된 SHA까지만 포함하므로 제출 전 다시 실행합니다.
