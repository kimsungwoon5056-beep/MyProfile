---
title: "GitHub Pages 배포 실패와 복구 기록"
description: "배포 단계 시간 초과(#18)와 진행 중 배포로 인한 실패(#19)를 관찰하고 복구·재검증한 과정"
date: 2026-10-16T02:30:00+09:00
draft: false
---

2026년 10월 16일 새벽, 연속으로 push한 두 커밋의 자동 배포가 실패했습니다. 빌드와 검사는 모두 통과했는데 마지막 배포 단계에서만 실패한 사례라서, 로그에서 확인한 사실과 복구 과정을 정리했습니다. 시각은 한국 시간이며 [Actions 실행 이력](https://github.com/kimsungwoon5056-beep/MyProfile/actions)과 배포 기록에서 확인했습니다.

## 관찰한 현상

| 실행 | 커밋 | 결과 |
|---|---|---|
| [#18](https://github.com/kimsungwoon5056-beep/MyProfile/actions/runs/38769538880) | `8fa5722` | build 성공(01:30), deploy 단계가 01:30:54부터 10분 29초 동안 진행되다 `Timeout reached, aborting!`으로 실패 |
| [#19](https://github.com/kimsungwoon5056-beep/MyProfile/actions/runs/38769827390) | `80fb483` | build 성공(01:41), deploy가 `due to in progress deployment. Please cancel 8fa5722… first` 오류(HTTP 400)로 실패. 01:47 직접 **Re-run failed jobs**로 다시 실행했지만 같은 오류 |

공개 사이트는 그동안 마지막으로 성공한 #17 버전으로 정상 표시되었습니다. 실패한 것은 새 버전으로 바꾸는 단계뿐이었습니다.

## 원인 판단

- #19의 오류 문장은 이전 커밋 `8fa5722`의 Pages 배포가 아직 진행 중이라서 새 배포를 만들 수 없다는 뜻이었습니다.
- #18 작업은 01:41에 시간 초과로 종료됐지만, GitHub Pages 쪽에는 그 배포가 한동안 진행 중으로 남아 있었습니다. Actions 작업이 끝난 것과 Pages 배포가 정리된 것은 별개의 상태라는 점을 확인했습니다.
- 워크플로의 `concurrency: github-pages`(`cancel-in-progress: false`) 설정 때문에 #19 build는 #18이 끝날 때까지 기다렸다가 01:41에 시작했습니다.
- #18 배포가 왜 10분 안에 끝나지 않았는지는 공개 로그만으로는 확인할 수 없었습니다. 같은 내용을 담은 `80fb483`이 이후 정상 배포되었으므로 사이트 파일 자체의 문제로 보지는 않았습니다.

## 조치와 재검증

1. 실패 직후 다시 실행하면 같은 이유로 막힌다는 것을 #19 재실행(01:47)에서 확인했습니다.
2. 시간이 지난 뒤 Actions 화면에서 직접 **Run workflow**를 눌러 같은 커밋 `80fb483`으로 수동 실행한 [#20](https://github.com/kimsungwoon5056-beep/MyProfile/actions/runs/38774612085)이 02:07에 build·deploy 모두 성공했습니다.
3. 수동 실행만으로는 push 자동 배포를 증명할 수 없어서, 다음 수정 커밋 `f21015d`를 push했고 [#21](https://github.com/kimsungwoon5056-beep/MyProfile/actions/runs/38776672685)이 push 이벤트로 자동 시작되어 약 50초 만에 배포까지 성공했습니다. 이후 push한 #22도 성공했습니다.
4. 공개 사이트에서 #21에 포함된 변경(프로젝트 페이지 문장 갱신)이 실제로 보이는 것을 확인했습니다.

## 배운 점과 남은 한계

- 빌드 성공과 배포 성공은 다른 단계이며, 실패한 단계의 로그 요약(Annotations) 문장을 먼저 읽는 것이 원인을 좁히는 가장 빠른 방법이었습니다.
- 앞선 배포가 정리되지 않은 상태에서 재실행을 반복해도 해결되지 않습니다. 진행 중인 배포가 끝나기를 기다리거나 정리된 뒤 다시 실행해야 합니다.
- 다음에 같은 문제가 생기면 저장소의 Deployments 화면에서 이전 배포 상태를 먼저 확인하겠습니다. 배포 단계 시간 제한(`deploy-pages`의 `timeout`)을 늘리는 방법도 있지만, 원인을 확인하지 못한 상태에서 설정을 바꾸지는 않았습니다.

로그 조회와 이 글의 정리에는 AI(Codex, Claude Code)의 지원을 받았습니다. 실행 번호·시각·오류 문장은 GitHub의 실제 기록에서 옮겼습니다.
