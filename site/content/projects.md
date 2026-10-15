---
title: "프로젝트"
draft: false
---

## SimCheong Android 지원 확대

- **참여 시기:** 2026학년도 2학기
- **진행 상태:** 진행 중 — 기존 구조 분석 및 플랫폼 확장 방향 검토 단계
- **활동 형태:** 팀 캡스톤 프로젝트

### 프로젝트 목적

이전 학기 팀의 시각장애인 보행 보조 프로젝트를 인계받아, iOS 중심의 기존 시스템을 Android에서도 사용할 수 있도록 확장하는 것을 목표로 합니다.

### 인계받은 기존 구현

기존 저장소에는 Unity 기반의 공간 처리 구조와 CoreML을 이용한 객체 인식, iOS 음성 안내 코드 등이 포함되어 있습니다. 이는 인계받은 기존 구현이며, 이번 팀이 새로 개발한 결과와 구분합니다.

- [기존 프로젝트 설명과 소스 코드](https://github.com/yoosunu/SimCheong)
- [CoreML 객체 인식 연결 코드](https://github.com/yoosunu/SimCheong/blob/b1c12caa3a94bf6d43624f05618f9ff8539586ea/Assets/CoreMLBridge.cs)
- [iOS 음성 안내 연결 코드](https://github.com/yoosunu/SimCheong/blob/b1c12caa3a94bf6d43624f05618f9ff8539586ea/Assets/TTSBridge.cs)

### 이번 팀의 목표와 현재 단계

이번 팀은 기존 구조와 플랫폼 종속성을 분석하고, Android 대응을 위한 구조 개선과 최적화 방향을 검토하는 단계입니다. Android 지원과 성능 개선은 향후 구현·검증할 목표이며, 완료된 성과로 제시하지 않습니다.
